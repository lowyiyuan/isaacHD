from tinydb import TinyDB, Query
import stdiomask
import keyboard
import getpass


# Initialize db.json file to store users
db = TinyDB('db.json')
welcomeScreen = """
*****************************************
Welcome to The National Security Arms CO.
*****************************************
Please select an option to proceed
[1] Login
[2] Register
[3] Submit Application
"""
class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.LoggedIn = True

    
def mainScreen (user):
    print(welcomeScreen)
    a = input()
    if(a == "1"):
        login('','')
    elif(a == "2"):
        register()
    else:
        print("Please choose a valid option!")
        mainScreen('')

def register():
    name = input("Enter Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    User = Query()
    
    if(db.search(User.username == username)):
        print("User already exist!")
        print(input("Press the 'Enter' key to go back"))
        while True:
            try:
                if keyboard.is_pressed('enter'):
                    mainScreen('')
                    break
            except:
                break
    else:
        db.insert({'name': name, 'username': username, 'password': password})
        print("Register successful! Welcome, " + name)
        

    

def login(username, password):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    User = Query()
    if(db.search(User.username == username) and (User.password == password)):
        print("Login Successful!")
        loggedInScreen(username)
    else:
        print("Incorrect Username or Password")
        login('', '')



def loggedInScreen(username):
    print('Welcome, ' + username)


mainScreen('')



