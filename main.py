
#login list
logins = []


#if for 1
def loginn():
    #opens file to check if username and password are in
    username_check()
    #checks if password is in the value corrosponding the the username
    password_check()
    #asks if to change password or sxt

def username_check():
    contiune_username = 1
    while contiune_username == 1:
        global login_username
        login_username = input("username: ")
        with open("logins.csv") as file:
            # print(login_username)
            for line in file:
                if login_username in line:
                    global password
                    username, password = line.strip().split(",")
                    contiune_username = 2
                else:
                    print("username not found")

def password_check():
    contiune_password = 1
    while contiune_password == 1:
        login_password = input("Password: ")
        # print(login_password)
        with open("logins.csv") as file:
            print(login_password)
            for line in file:
                if login_password in line:
                    post_login_options()
                    contiune_password = 2
                else:
                    print("invalid password")

def post_login_options():
    login_options = input("change password: 1\nLogout: 2\nChoice: ")
    #if change password opens files as read
    if login_options == "1":
        #creates new line to append file execpt for changeding line
        with open("logins.csv") as file:
            templist = []
            new_password = input("New password: ")
            for line in file:
                templist.append(line)
                #opens files as write and writes templist to file
                with open("logins", "w") as file:
                    file.write(templist)
                    exit()
    else:
        exit



#if for register 2
def registerr():
    contine_register = 1
    register_username = input("new username: ")
    while contine_register == 1:
        register_password = input("New password: ")
        if len(register_password) < 4:
            print("to small")
        else:
            logins.append(f"{register_username},{register_password}")
            contine_register = 2
        #add usernames to file
            with open("logins.csv", "a") as file:
                file.write(f"\n{register_username},{register_password}")


#var for contiune loop
continuecode = 1
def contorexit():
    continuecode = 2
    return continuecode

#menu
while continuecode == 1:
    menu_options = input("login: 1\nregister: 2\nexit: 3\nChoice: ")
    if menu_options == "1":
        loginn()
    elif menu_options == "2":
        registerr()
    elif menu_options == "3":
        exit()
    else:
        print("pick a valid option")
    contorexit()
    