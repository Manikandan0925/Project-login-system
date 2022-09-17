granted = False
import re
regex =re.compile(r'([A-Za-z]+[0-9]*[.-_])+[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("db.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")
        
def register(name,password):
    file = open("db.txt","a")
    file.write(name+","+password+"\n")
    grant()
def access(option):
    global name
    if(option=="login"):
        name = input("Enter your user name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your User name and password to register")
        name = input("Enter your name: ")
        
        if not re.match(regex, name):
            print("please enter correct email ID")
            access(option!="login")
        else:
            password = input("Enter your password: ")
            if len(password)>=6 and len(password)<=16:
                register(name,password)
            else:
                print("your password must greathen 6 character or less then 16 charecter")
                access(option!="login")
def begin():
    global option
    print("welcome to Register| login programming")
    option = input("Login |Register: \n")
    if(option!="login" and option!="Register"):
        begin()
        
begin()
access(option)

if(granted):
    print("Welcome! "+name)
    


    