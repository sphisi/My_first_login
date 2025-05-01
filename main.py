
#login list
logins = []

#if for 1
def loginn():
    contiune_username = 1
    login_username = input("username: ")
    #opens file to check if username and password are in
    with open("logins.csv") as file:
        print(login_username)
        for line in file:
            if login_username in line:
                username, password = line.strip().split(",")
                password = password
                print(password)
                #checks if password is in the value corrosponding the the username
                login_password = input("Password: ").strip.strip()
                print(login_password)
                for line in file:
                    if login_password in line:
                        #asks if to change password or sxt
                        login_options = input("change password: 1\nLogout: 2\nChoice: ")
                        #if change password opens files as read
                        if login_options == "1":
                                #creates new line to append file execpt for changeding line
                                for line in file:
                                    templist = []
                                new_password = input("New password: ")
                                
                                #opens files as write and writes templist to file
                        with open("logins", "w") as file:
                            file.write(templist)
                    else:
                        exit
                else:
                    print("invalid password")
        else:
            print("username not found")


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
    