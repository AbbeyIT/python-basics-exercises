username = ["Kirito", "Asuna", "Sinon"]
password = ["Beater1007", "Flash0930", "Sniper0821"]

currUsername = input("Enter your username: ")
currPassword = input("Enter your password: ")


for x in range(len(username)):
    if currUsername == username[x] and currPassword == password[x]:
        print("Welcome to Sword Art Online " + username[x])
        break
    
else:
    print("Invalid user")