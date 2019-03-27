package main

import (
	"database/sql"
	"fmt"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"

	_ "github.com/go-sql-driver/mysql"
)

var db *sql.DB
var err error

type quiz struct {
	ID           int    `json:"quizid"`
	QID          int    `json:"questionqid"`
	Name         string `json:"quizname"`
	GID          int    `json:"genreid"`
	QuestionType string `json:"single"`
	Question     string `json:"question"`
	OptionA      string `json:"optiona"`
	OptionB      string `json:"optionb"`
	OptionC      string `json:"optionc"`
	OptionD      string `json:"optiond"`
	AnswerA      bool   `json:"answera"`
	AnswerB      bool   `json:"answerb"`
	AnswerC      bool   `json:"answerc"`
	AnswerD      bool   `json:"answerd"`
	Image        string `json:"img"`
	Audio        string `json:"aud"`
	ImgURL       string `json:"url"`
}

type sendque struct {
	QID          int    `json:"qid"`
	QuestionType string `json:"single"`
	Question     string `json:"question"`
	OptionA      string `json:"optiona"`
	OptionB      string `json:"optionb"`
	OptionC      string `json:"optionc"`
	OptionD      string `json:"optiond"`
	AnswerA      bool   `json:"answera"`
	AnswerB      bool   `json:"answerb"`
	AnswerC      bool   `json:"answerc"`
	AnswerD      bool   `json:"answerd"`
	Image        string `json:"img"`
	Audio        string `json:"aud"`
	ImgURL       string `json:"url"`
}

type sendQuiz struct {
	QuizID   int    `json:"id"`
	QuizName string `json:"name"`
}

type user struct {
	ID       int    `json:"id"`
	Type     string `json:"type"`
	Username string `json:"username"`
	Password string `json:"password"`
}

type scoreboard struct {
	UID   int `json:"userid"`
	QID   int `json:"quizid"`
	Score int `json:"score"`
}

type genres struct {
	ID    string `json:"id"`
	Genre string `json:"genres"`
}

type respond struct {
	Msg    string `json:"msg"`
	Logged uint   `json:"logged"`
	User   string `json:"user"`
	Name   string `json:"name"`
	ID     int    `json:"id"`
	Score  int    `json:"score"`
}

type status struct {
	Success bool   `json:"success"`
	Msg     string `json:"msg"`
}

func createTables() {
	db, err = sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/")
	if err != nil {

		panic(err)
	}
	defer db.Close()

	_, err = db.Exec("CREATE DATABASE IF NOT EXISTS quizapp")
	if err != nil {
		panic(err)
	}

	db, err = sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/quizapp")
	if err != nil {
		panic(err)
	}

	_, err = db.Exec("CREATE TABLE IF NOT EXISTS users(user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, user_type VARCHAR(50),username VARCHAR(50) UNIQUE,password VARCHAR(1500))")
	if err != nil {
		panic(err)
	}

	_, err = db.Exec("CREATE TABLE IF NOT EXISTS scoreboard(user_id INT NOT NULL,quiz_id INT NOT NULL,genre_id INT NOT NULL, score INT NOT NULL,PRIMARY KEY(user_id,quiz_id,genre_id),FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE)")
	if err != nil {
		panic(err)
	}

	_, err = db.Exec("CREATE TABLE IF NOT EXISTS genres(genre_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,genre_name VARCHAR(50))")
	if err != nil {
		panic(err)
	}

	_, err = db.Exec("CREATE TABLE IF NOT EXISTS quizzes(quiz_id INT ,que_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,quiz_name VARCHAR(50),genre_id INT NOT NULL,question_type VARCHAR(50),question_statement VARCHAR(500), optiona VARCHAR(50),optionb VARCHAR(50), optionc VARCHAR(50), optiond VARCHAR(50),ansa BOOL,ansb BOOL,ansc BOOL,ansd BOOL,img VARCHAR(50),aud VARCHAR(50),img_url VARCHAR(10000),FOREIGN KEY(genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE)")
	if err != nil {
		panic(err)
	}

}

func createGenre(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	var gen genres
	err = c.BindJSON(&gen)
	if err != nil {
		panic(err)
	}
	var cnt int
	var sendmsg status
	err = db.QueryRow("SELECT COUNT(*) FROM genres WHERE genre_name=?", gen.Genre).Scan(&cnt)
	fmt.Println(cnt)
	if cnt == 0 {
		_, err = db.Query("INSERT INTO genres(genre_name) VALUES(?)", gen.Genre)
		if err != nil {
			sendmsg.Success = false
			sendmsg.Msg = "Could not access database"
		} else {
			sendmsg.Success = true
			sendmsg.Msg = "Genre created successfully"
		}
	} else {
		sendmsg.Success = false
		sendmsg.Msg = "A genre with the given genrename already exists"
	}
	c.JSON(200, sendmsg)
}

func getGenres(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	rows, err1 := db.Query("SELECT genre_id,genre_name FROM genres")
	if err1 != nil {
		panic(err1)
	}
	var gen []genres

	for rows.Next() {
		var genrename genres
		err = rows.Scan(&genrename.ID, &genrename.Genre)
		gen = append(gen, genrename)
	}

	c.JSON(200, gen)
}

func updateGenre(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	id := c.Params.ByName("genreId")

	type updgen struct {
		Genrename string `json:"genrename"`
	}

	var gen updgen
	err = c.BindJSON(&gen)
	if err != nil {
		panic(err)
	}
	var sendmsg status
	_, err2 := db.Query("UPDATE genres SET genre_name = ? WHERE genre_id=?", gen.Genrename, id)
	if err2 != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not access database"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Updated succesfully"
	}
	c.JSON(200, sendmsg)
}

func deleteGenre(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	genreid := c.Params.ByName("genreId")
	var sendmsg status
	_, err1 := db.Query("DELETE FROM genres WHERE genre_id =?", genreid)
	if err1 != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not delete from db"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Deleted successfully"
	}
	c.JSON(200, sendmsg)
}

func updateQuiz(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	quizid := c.Params.ByName("quizId")
	genreid := c.Params.ByName("genreId")

	type updqui struct {
		Quizname string `json:"quizname"`
	}

	var qui updqui
	err = c.BindJSON(&qui)
	var sendmsg status
	_, err2 := db.Query("UPDATE quizzes SET quiz_name = ? WHERE quiz_id=? AND genre_id=?", qui.Quizname, quizid, genreid)
	if err2 != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not update in db"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Updated successfully"
	}
	c.JSON(200, sendmsg)
}

func deleteQuiz(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	quizid := c.Params.ByName("quizId")
	var sendmsg status
	_, err = db.Query("DELETE FROM quizzes WHERE quiz_id = ?", quizid)
	if err != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not delete from db"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Deleted successfully"
	}
	c.JSON(200, sendmsg)
}

func updateQuestion(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	var que quiz
	err := c.BindJSON(&que)
	if err != nil {
		panic(err)
	}

	var sendmsg status
	_, err1 := db.Query("UPDATE quizzes SET question_type=?,question_statement=?,optiona=?,optionb=?,optionc=?,optiond=?,ansa=?,ansb=?,ansc=?,ansd=?,img=?,aud=?,img_url=? WHERE quiz_id=? AND que_id=? AND genre_id=?", que.QuestionType, que.Question, que.OptionA, que.OptionB, que.OptionC, que.OptionD, que.AnswerA, que.AnswerB, que.AnswerC, que.AnswerD, que.Image, que.Audio, que.ImgURL, que.ID, que.QID, que.GID)
	if err1 != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not update in db"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Updated successfully"
	}
	c.JSON(200, sendmsg)
}

func deleteQuestion(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	genreid := c.Params.ByName("genreId")
	quizid := c.Params.ByName("quizId")
	questionid := c.Params.ByName("questionId")

	var sendmsg status
	_, err = db.Query("DELETE FROM quizzes WHERE quiz_id = ? AND que_id = ? AND genre_id = ?", quizid, questionid, genreid)
	if err != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not update in db"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Updated successfully"
	}
	c.JSON(200, sendmsg)
}

func getQuizzes(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	id := c.Params.ByName("genreId")

	rows, err1 := db.Query("SELECT DISTINCT quiz_id, quiz_name FROM quizzes WHERE genre_id = ?", id)
	if err1 != nil {
		panic(err1)
	}
	var quinam []sendQuiz
	for rows.Next() {
		var qui sendQuiz
		err = rows.Scan(&qui.QuizID, &qui.QuizName)
		quinam = append(quinam, qui)
	}
	c.JSON(200, quinam)
}

func getQuestions(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	genreid := c.Params.ByName("genreId")
	quizid := c.Params.ByName("quizId")

	rows, err1 := db.Query("SELECT que_id,question_type,question_statement,optiona,optionb,optionc,optiond,ansa,ansb,ansc,ansd,img,aud,img_url FROM quizzes WHERE genre_id = ? AND quiz_id = ?", genreid, quizid)
	if err1 != nil {
		panic(err1)
	}
	var quest []sendque
	for rows.Next() {
		var ques sendque
		err = rows.Scan(&ques.QID, &ques.QuestionType, &ques.Question, &ques.OptionA, &ques.OptionB, &ques.OptionC, &ques.OptionD, &ques.AnswerA, &ques.AnswerB, &ques.AnswerC, &ques.AnswerD, &ques.Image, &ques.Audio, &ques.ImgURL)
		quest = append(quest, ques)
	}
	fmt.Println(len(quest))
	c.JSON(200, quest)
}

func getQuestion(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	genreid := c.Params.ByName("genreId")
	quizid := c.Params.ByName("quizId")
	queid := c.Params.ByName("queId")

	rows, err1 := db.Query("SELECT que_id,question_type,question_statement,optiona,optionb,optionc,optiond,ansa,ansb,ansc,ansd,img,aud,img_url FROM quizzes WHERE genre_id = ? AND quiz_id = ? AND que_id = ?", genreid, quizid, queid)
	if err1 != nil {
		panic(err1)
	}
	var ques sendque
	for rows.Next() {
		err = rows.Scan(&ques.QID, &ques.QuestionType, &ques.Question, &ques.OptionA, &ques.OptionB, &ques.OptionC, &ques.OptionD, &ques.AnswerA, &ques.AnswerB, &ques.AnswerC, &ques.AnswerD, &ques.Image, &ques.Audio, &ques.ImgURL)
	}
	c.JSON(200, ques)
}

func createQuiz(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	id := c.Params.ByName("genreId")

	var q []quiz
	err = c.BindJSON(&q)
	if err != nil {
		panic(err)
	}

	var sendmsg status
	for i := 0; i < len(q); i++ {
		_, err = db.Query("INSERT INTO quizzes(quiz_id,quiz_name,genre_id,question_type,question_statement,optiona,optionb,optionc,optiond,ansa,ansb,ansc,ansd,img,aud,img_url) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", q[i].ID, q[i].Name, id, q[i].QuestionType, q[i].Question, q[i].OptionA, q[i].OptionB, q[i].OptionC, q[i].OptionD, q[i].AnswerA, q[i].AnswerB, q[i].AnswerC, q[i].AnswerD, q[i].Image, q[i].Audio, q[i].ImgURL)
		if err != nil {
			sendmsg.Success = false
			sendmsg.Msg = "Could not create completely in db"
		} else {
			sendmsg.Success = true
			sendmsg.Msg = "Created successfully"
		}
	}
	c.JSON(200, sendmsg)
}

func checkAnswers(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	type checkans struct {
		Name  string `json:"name"`
		Score int    `json:"score"`
	}
	genreid := c.Params.ByName("genreId")
	quizid := c.Params.ByName("quizId")
	var ans []checkans
	var count int
	err = c.BindJSON(&ans)
	if err != nil {
		panic(err)
	}
	var response respond
	if ans[len(ans)-1].Name == "guest" {
		response.Logged = 0
		response.Msg = "You need to log in for your score to be saved"
		response.User = "user"
		response.Name = "quest"
	} else {
		response.Logged = 1
		score := ans[len(ans)-1].Score
		response.Score = score
		var userid int
		err = db.QueryRow("SELECT user_id FROM users WHERE username=?", ans[len(ans)-1].Name).Scan(&userid)
		err = db.QueryRow("SELECT COUNT(*) FROM scoreboard WHERE user_id = ? AND quiz_id = ? AND genre_id=?", userid, quizid, genreid).Scan(&count)
		if count == 0 {
			_, err = db.Query("INSERT INTO scoreboard(user_id,quiz_id,genre_id,score) VALUES(?,?,?,?)", userid, quizid, genreid, score)
			if err != nil {
				panic(err)
			}
		} else {
			_, err = db.Query("UPDATE scoreboard SET score = ? WHERE user_id = ? AND quiz_id = ? AND genre_id = ?", score, userid, quizid, genreid)
			if err != nil {
				panic(err)
			}
		}
	}
	c.JSON(200, response)
}

func createQuestion(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	genreid := c.Params.ByName("genreId")
	quizid := c.Params.ByName("quizId")

	rows, err1 := db.Query("SELECT quiz_name FROM quizzes WHERE quiz_id = ? AND genre_id=?", quizid, genreid)
	if err1 != nil {
		panic(err1)
	}
	var quizname string
	rows.Next()
	rows.Scan(&quizname)

	var q quiz
	err = c.BindJSON(&q)

	if err != nil {
		panic(err)
	}
	var sendmsg status
	_, err = db.Query("INSERT INTO quizzes(quiz_id,quiz_name,genre_id,question_type,question_statement,optiona,optionb,optionc,optiond,ansa,ansb,ansc,ansd,img,aud,img_url) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", quizid, quizname, genreid, q.QuestionType, q.Question, q.OptionA, q.OptionB, q.OptionC, q.OptionD, q.AnswerA, q.AnswerB, q.AnswerC, q.AnswerD, q.Image, q.Audio, q.ImgURL)
	if err1 != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not insert in db"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Inserted successfully"
	}
	c.JSON(200, sendmsg)
}

func signup(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	var userinfo user
	var response respond
	err = c.BindJSON(&userinfo)
	if err != nil {
		panic(err)
	}
	if userinfo.Username == "" || userinfo.Password == "" || userinfo.Type == "" {
		response.Logged = 0
		response.Msg = "Fill in all the details"
		response.User = "none"
	} else {

		bytePassword, err1 := bcrypt.GenerateFromPassword([]byte(userinfo.Password), 14)
		hashedPassword := string(bytePassword)
		if err1 != nil {
			panic(err1)
		}
		var cnt int
		err = db.QueryRow("SELECT COUNT(*) FROM users WHERE username = ?", userinfo.Username).Scan(&cnt)
		if err != nil {
			response.Logged = 0
			response.Msg = "Could not access database"
			response.User = "none"
		}

		if cnt == 0 {
			_, err = db.Query("INSERT INTO users(user_type, username, password) VALUES(?,?,?)", userinfo.Type, userinfo.Username, hashedPassword)
			if err != nil {
				response.Logged = 0
				response.Msg = "Invalid Credentials"
				response.User = "none"
			} else {
				response.Logged = 1
				response.Msg = "Registered Successfully"
				response.User = "none"
			}
		} else {
			response.Logged = 0
			response.Msg = "User with this username already exists.Please pick another one."
			response.User = "none"
		}
	}
	c.JSON(200, response)
}

func login(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	var userinfo user
	err = c.BindJSON(&userinfo)
	if err != nil {
		panic(err)
	}
	var pass string
	var response respond
	rows, err1 := db.Query("SELECT password FROM users WHERE username=?", userinfo.Username)
	if err1 != nil {
		response.Msg = "Could not access database"
		response.Logged = 0
	} else {
		rows.Next()
		rows.Scan(&pass)
		err = bcrypt.CompareHashAndPassword([]byte(pass), []byte(userinfo.Password))
		if err != nil {
			response.Logged = 0
			response.Msg = "Password does not match or user with the given username does not exist"
			response.User = "none"
		} else {
			response.Logged = 1
			response.Msg = "Logged in Successfully"
			var usr string
			err = db.QueryRow("SELECT user_type FROM users WHERE username = ?", userinfo.Username).Scan(&usr)
			response.User = usr
			response.Name = userinfo.Username
			var id int
			err = db.QueryRow("SELECT user_id FROM users WHERE username = ?", userinfo.Username).Scan(&id)
			response.ID = id
		}
	}
	c.JSON(200, response)
}

func leaderboard(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	genreid := c.Params.ByName("genreId")
	rows, err1 := db.Query("SELECT user_id,SUM(score) from scoreboard WHERE genre_id = ? GROUP BY user_id", genreid)
	if err1 != nil {
		panic(err1)
	}
	type scores struct {
		Name  string `json:"name"`
		Score int    `json:"score"`
	}
	var sendscore []scores
	for rows.Next() {
		var sendsc scores
		var id int
		rows.Scan(&id, &sendsc.Score)
		err = db.QueryRow("SELECT username FROM users WHERE user_id=?", id).Scan(&sendsc.Name)
		sendscore = append(sendscore, sendsc)
	}
	c.JSON(200, sendscore)
}

func leaderboardTotal(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	rows, err1 := db.Query("SELECT user_id,SUM(score) from scoreboard GROUP BY user_id")
	if err1 != nil {
		panic(err1)
	}
	type scores struct {
		Name  string `json:"name"`
		Score int    `json:"score"`
	}
	var sendscore []scores
	for rows.Next() {
		var sendsc scores
		var id int
		rows.Scan(&id, &sendsc.Score)
		err = db.QueryRow("SELECT username FROM users WHERE user_id=?", id).Scan(&sendsc.Name)
		sendscore = append(sendscore, sendsc)
	}
	c.JSON(200, sendscore)
}

func deleteUser(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	userid := c.Params.ByName("userId")
	_, err = db.Query("DELETE FROM users WHERE user_id = ?", userid)
	var sendmsg status
	if err != nil {
		sendmsg.Success = false
		sendmsg.Msg = "Could not delete"
	} else {
		sendmsg.Success = true
		sendmsg.Msg = "Deleted succesfully"
	}
	c.JSON(200, sendmsg)
}

func getUsers(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	rows, err1 := db.Query("SELECT user_id,username FROM users WHERE user_type = ?", "user")
	if err1 != nil {
		panic(err1)
	}
	type usersend struct {
		ID       int    `json:"id"`
		Username string `json:"name"`
	}
	var use []usersend
	for rows.Next() {
		var us usersend
		err = rows.Scan(&us.ID, &us.Username)
		use = append(use, us)
	}
	c.JSON(200, use)
}

func userQuizzes(c *gin.Context) {
	c.Header("access-control-allow-origin", "*")
	userid := c.Params.ByName("userId")
	rows, err1 := db.Query("SELECT genre_id,quiz_id,score FROM scoreboard WHERE user_id=?", userid)
	if err1 != nil {
		panic(err1)
	}
	type qui struct {
		Username string `json:"name"`
		Quizname string `json:"quiz"`
		Score    int    `json:"score"`
	}
	var q []qui

	for rows.Next() {
		var qu qui
		var qid int
		var gid int
		rows.Scan(&gid, &qid, &qu.Score)
		err = db.QueryRow("SELECT DISTINCT username FROM users WHERE user_id=?", userid).Scan(&qu.Username)
		err = db.QueryRow("SELECT DISTINCT quiz_name FROM quizzes WHERE quiz_id = ? AND genre_id =?", qid, gid).Scan(&qu.Quizname)
		q = append(q, qu)
	}
	c.JSON(200, q)
}

func main() {
	createTables()
	db, err = sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/quizapp")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	r := gin.Default()

	r.POST("/signup", signup)
	r.POST("/login", login)
	r.GET("/users", getUsers)
	r.GET("/usequizzes/:userId", userQuizzes)
	r.DELETE("/users/delete/:userId", deleteUser)
	//to get all the genres
	r.GET("/getgenres", getGenres)
	//to get all the quiz names in the particular genre
	r.GET("/genres/:genreId", getQuizzes)
	//to get all the questions in a selected quiz
	r.GET("/genres/:genreId/:quizId", getQuestions)
	//to get a single selected question
	r.GET("/getque/:genreId/:quizId/:queId", getQuestion)
	//to create a genre
	r.POST("/creategenres", createGenre)
	//to create a quiz,redirects into create n questions
	r.POST("/genres/create/:genreId", createQuiz)
	//to create a question in  a quiz
	r.POST("/genres/create/:genreId/:quizId", createQuestion)
	//to update the name of a genre
	r.PUT("/genres/update/:genreId", updateGenre)
	//to update quiz name
	r.PUT("/genres/update/:genreId/:quizId", updateQuiz)
	//to update question
	r.PUT("/genres/update/:genreId/:quizId/:questionId", updateQuestion)
	//to delete genre
	r.DELETE("/delete/:genreId", deleteGenre)
	//to delete quiz
	r.DELETE("/delete/:genreId/:quizId", deleteQuiz)
	//to delete question
	r.DELETE("/delete/:genreId/:quizId/:questionId", deleteQuestion)
	// r.HandleFunc("/scoreboard,GetScoreboard").Methods("GET")
	r.GET("/scoreboard/:genreId", leaderboard)
	r.GET("/scoreboard", leaderboardTotal)
	r.POST("/finalans/:genreId/:quizId", checkAnswers)
	// log.Fatal(http.ListenAndServe(":8080", r))
	r.Use(cors.Default())
	r.Run(":8080")
}
