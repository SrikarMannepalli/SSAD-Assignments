#Things implemented:
* Registration and Login
* Admin can view and delete the users
* Admin can create,update and delete new genres, quizzes and questions
* Questions can be either single correct or multiple correct
* A leaderboard is present for users in each genre, and an overall leaderboard across genres
* Users can see all the quizzes they attempted along with their scores in those quizzes
* Image and Audio questions are also present

#Packages imported in go
"database/sql"
"fmt"

"github.com/gin-contrib/cors"
"github.com/gin-gonic/gin"
"golang.org/x/crypto/bcrypt"
_"github.com/go-sql-driver/mysql"

#To install npm packages
### Run in react-app folder  ###
* npm install

#To run Go server
### Run in go/src folder ###
* go run main.go

#To run react server
### Run in react-app folder ###
* yarn start

#To run 
* Install mySql
* Add your mySql root password to lines 92, 104 and 629 in go/src/main.go
