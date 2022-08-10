import mysql.connector

print("connceting...")

mydb = mysql.connector.connect(
  host="wordle.ce3zuwpfpvje.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Moarte01`",
  database = "Wordle"
)

def ReadUserData(UserID):
    mycursor = mydb.cursor()
    print("reading data")
    #Fix data names
    mycursor.execute("SELECT * FROM WordleScores WHER UserID = {UserID}")
    UserValues = mycursor.fetchall()

    for x in UserValues:
      print(x)
    print(UserID)

    mydb.close()

def CalNewValues(UserID, GameData):
    #strip game to smaller(remove all character positioning)

    print("Calculating")

def WriteUserData(UserID):
    print("Writing Data")
    #find a way to read the data for saved sate in phone as string
    CurrentUser = 3
    UserPlayed = 0
    UserStreak = 0
    UserMaxStreak = 0

    mycursor = mydb.cursor()
    UserVal = UserPlayed,UserStreak,UserMaxStreak,UserID
    #fix column names
    mycursor.execute("INSERT INTO WordleScores (played,curStreak,maxStreak) Values(%s,%s,%s) WHERE UserID = {%s}",UserVal)
    print("Data Written")
    mydb.close()