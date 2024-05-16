# Justin Cheah Wei Hao TP064130
# Mum Choon Jie TP064004
from datetime import datetime


def Main_Page():
    while True:
        print("=" * 50)
        print("|Asian Event Management Services (AEMS)|")
        print("")
        print("Type '1' to show all available events.")
        print("Type '2' to show events per category.")
        print("Type '0' to go Register/Login page for Admin and Customer.")
        print("=" * 50)
        print("")
        view_data()
        Next = int(input("| 1.Login | 2.Register | 0.Exit :"))
        if Next == 1:
            Login_System()
        elif Next == 2:
            Register()
        elif Next == 0:
            print("-" * 40)
            print("Thank You !!! Please Visit Again")
            print("-" * 40)
            break
        else:
            print("Invalid Option!!!")


def view_data():
    while True:
        db = open("Event.txt", "r")
        choice = int(input("Event : 1.All 2.Category 0.Next :"))
        print("-" * 40)
        if choice == 1:
            for i in db:
                a, b, c, d, e, f, g, h = i.split(" , ")
                h = h.strip()
                print("Category: " + a + "| Type: " + b + "| EventName: " + c + "| Location: " + d
                      + "| Date: " + e + "| Duration: " + f + "| Time: " + g + "| Price:RM " + h)
        elif choice == 2:
            record = input("Category = Entertainment , Educational , Charity , Other :")
            record = record.title()
            for i in db:
                a, b, c, d, e, f, g, h = i.split(" , ")
                h = h.strip()
                if i.startswith(record):
                    print(" Type: " + b + "| EventName: " + c + "| Location: " + d +
                          "| Date: " + e + "| Duration: " + f + "| Time: " + g + "| Price:RM " + h)
        elif choice == 0:
            break
        else:
            print("invalid Option!!!")
        db.close()


def Admin_Page():
    while True:
        AdminPage = int(input("| 1.ADD | 2.Modify | 3.Display | 0.Logout:"))
        print("=" * 40)
        if AdminPage == 1:
            add_Event()
        elif AdminPage == 2:
            modify_Event()
        elif AdminPage == 3:
            while True:
                displayOption = int(input("| 1.Event | 2.Registration | 3.Payment Detail | 0.Exit :"))
                if displayOption == 1:
                    view_data()
                elif displayOption == 2:
                    RegistrationDetail()
                elif displayOption == 3:
                    PaymentDetail()
                else:
                    break
        elif AdminPage == 0:
            print("-" * 40)
            print("Logout Success !!!")
            print("-" * 40)
            break
        else:
            print("-" * 40)
            print("Invalid Option!!!")
            print("-" * 40)


def User_Page(UserName):
    while True:
        UserPage = int(input("|1.Display | 2.Add to Cart | 0.Logout :"))
        if UserPage == 1:
            view_data()
        elif UserPage == 2:
            AddItem = addtoCart(UserName)
            Payment(UserName, AddItem)
        elif UserPage == 0:
            print("-" * 40)
            print("Logout Success!!!")
            print("-" * 40)
            break
        else:
            print("Invalid Option!!!")


def Admin_Register():
    while True:
        Admin_verification()
        db = open("admin_Account.txt", "r")
        userCheckList = []
        passwordCheckList = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            userCheckList.append(a)
            passwordCheckList.append(b)
        db.close()
        while True:
            UserName = input("Enter the UserName: ")
            if UserName in userCheckList:
                print("-" * 40)
                print("the UserName have exists!")
                print("-" * 40)
            else:
                Password = input("Enter the password: ")
                Password1 = input("Comfirm the password: ")
                if Password in passwordCheckList:
                    print("-" * 40)
                    print("Password already exists! ")
                    print("-" * 40)
                elif Password != Password1:
                    print("-" * 40)
                    print("Password din't match,restart")
                    print("-" * 40)
                else:
                    db = open("admin_Account.txt", "a")
                    db.write(UserName + "," + Password + "\n")
                    print("-" * 40)
                    print("Register Success")
                    print("-" * 40)
                    db.close()
                    break
        break


def User_Register():
    db = open("User_Account.txt", "r")
    icon = ['@', '#', '$', '%', '&', '*']
    userCheckList = []
    passwordCheckList = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        userCheckList.append(a)
        passwordCheckList.append(b)
    while True:
        UserName = input("Enter the UserName: ")
        if UserName in userCheckList:
            print("the UserName have exists!")
        else:
            print("\n Password Requirement \n * the length of password is 6 to max 12\n "
                  "* At Least one number\n * At Least one uppercase letter \n * At Least one lowercase letter\n "
                  "* At least one of the symbols $,@,#,%,&,* \n  ")
            Password = input("Enter the password: ")
            Password1 = input("Confirm the password: ")
            if Password in passwordCheckList:
                print("the Password has exists! ")
            elif Password != Password1:
                print("Password don`t match,restart")
            elif len(Password) < 6 or len(Password) > 12:
                print("Password not match Length requirement 6 to 12 ")
            elif not any(char.isdigit() for char in Password):
                print("Password should have at least one numeral")
            elif not any(char.isupper() for char in Password):
                print('Password should have at least one uppercase letter')
            elif not any(char.islower() for char in Password):
                print('Password should have at least one lowercase letter')
            elif not any(char in icon for char in Password):
                print('Password should have at least one of the symbols $,@,#,%,&,*')
            else:
                db = open("User_Account.txt", "a")
                db.write(UserName + "," + Password + "\n")
                print("-" * 40)
                print("Register Success")
                print("-" * 40)
                db.close()
                return UserName


def Register():
    while True:
        Selection = int(input("Register 1.Admin 2.User 0.Exit :"))
        print("=" * 40)
        if Selection == 1:
            Admin_Register()
            Admin_Page()
            break
        elif Selection == 2:
            UserName = User_Register()
            User_Page(UserName)
            break
        elif Selection == 0:
            break
        else:
            print("Invalid Option!!!")


def Login(db):
    Account_list = []
    while True:
        UserName = input("Enter your UserName: ")
        Password = input("Enter your password: ")
        for i in db:
            Account_list.append(i)
        if UserName + "," + Password + "\n" in Account_list:
            print("-" * 45)
            print("Login Successful")
            print("Welcome," + UserName)
            print("-" * 45)
            return UserName
        else:
            print("-" * 40)
            print("Invalid Username or password")
            print("-" * 40)


def Login_System():
    while True:
        LoginOption = int(input("Login 1.Admin 2.User 0.Exit :"))
        if LoginOption == 1:
            Admin_verification()
            db = open("admin_Account.txt", "r")
            Login(db)
            Admin_Page()
            db.close()
        elif LoginOption == 2:
            db = open("User_Account.txt", "r")
            UserName = Login(db)
            User_Page(UserName)
            db.close()
        elif LoginOption == 0:
            break
        else:
            print("Invalid Option !!!")


def Admin_verification():
    while True:
        AdminCode = ["#001", "#002", "#003", "#004", "#005"]
        ConfirmCode = input("Enter the given Admin Code :")
        if ConfirmCode not in AdminCode:
            print("Invalid Admin Code, Please Try Again.")
            print("=" * 40)
            Login_System()
        else:
            break


def add_Event():
    db = open("Event.txt", "a")
    while True:
        print("Add Event Menu")
        print("")
        print("=" * 40)
        print("Type of Categories : Entertainment , Educational , Charity , Other.")
        print("(Type out one of the available category)")
        print("=" * 40)
        print("")
        Category = input("Category: ")
        Category = Category.title()
        Type = input("The types of event: ")
        Type = Type.title()
        EventName = input("Event Name : ")
        EventName = EventName.title()
        Location = input("Location: ")
        Location = Location.title()
        Date = input("Date: ")
        Duration = input("Duration: ")
        Time = input("Time(12/24 HourSystem ): ")
        Price = input("Price(RM): ")
        Price = Price.title()
        db.write(Category + " , " + Type + " , " + EventName + " , " + Location + " , " + Date + " , " + Duration
                 + " , " + Time + " , " + Price + "\n")
        response = input("Do you wish to continue with the Data Entry ? [Y/N]")
        if response.upper() == "Y":
            print("Continue Insert")
        elif response.upper() == "N":
            print("Insert Success")
            break
        else:
            print(" Invalid Option!!!")
    db.close()


def modify_Event():
    db = open("Event.txt", "r")
    EventRecord = db.readlines()
    NewRecord = EventRecord
    db.close()
    while True:
        print("Event Modify Function")
        EventName_modify = input("Enter Event Name(Please the Correct Event Name): ")
        EventName_modify = EventName_modify.title()
        for i in EventRecord:
            if EventName_modify in i:
                print(i)
                while True:
                    Confirm = input("Is this event ? <Y/N> :")
                    if Confirm.upper() == "Y":
                        db = open("Event.txt", "w")
                        modify = EventRecord.index(i)
                        print("Category | Entertainment , Educational , Charity , Other ")
                        Category = input("Category: ")
                        Category = Category.title()
                        Type = input("Event Type: ")
                        Type = Type.title()
                        EventName = input("Event Name : ")
                        EventName = EventName.title()
                        Location = input("Location: ")
                        Location = Location.title()
                        Date = input("Date: ")
                        Duration = input("Duration: ")
                        Time = input("Time: ")
                        Price = input("Price: ")
                        Price = Price.title()
                        NewRecord[modify] = (
                                Category + " , " + Type + " , " + EventName + " , " + Location + " , " + Date
                                + " , " + Duration + " , " + Time + " , " + Price + "\n")
                        for line in NewRecord:
                            db.write(line)
                        print("Modify Success!")
                        print(NewRecord[modify])
                        db.close()
                        break
                    elif Confirm.upper() == "N":
                        print("Modify has been Cancel!!")
                        break
                    else:
                        print("Invalid Option!!!")


def addtoCart(UserName):
    db = open("Event.txt", "r")
    EventRecord = db.readlines()
    db.close()
    Price = []
    while True:
        print("Add to Cart")
        AddItem = input("the Event Name :")
        AddItem = AddItem.title()
        for i in EventRecord:
            a, b, c, d, e, f, g, h = i.split(" , ")
            h = h.strip()
            i = i.strip()
            if h == "Free":
                Price.append(h)
            else:
                h = float(h)
                Price.append(h)
            if AddItem in i:
                print(i)
                Confrim = input("This the event want add to Cart<Y/N>:")
                if Confrim.upper() == "Y":
                    db = open("RegistrationDetail.txt", "a")
                    Quantity = int(input("Quantity of the ticket:"))
                    if h == "Free":
                        totalprice = h
                    else:
                        totalprice = h * Quantity
                    Record = (str(UserName) + " , " + a + " , " + c + " , " + d + " , " + e + " , " + g + " , "
                              + str(Quantity) + " , " + str(totalprice) + "\n")
                    db.write(Record)
                    print("Add Success, make payment !!!")
                    db.close()
                    return AddItem
                elif Confrim.upper() == "N":
                    break
                else:
                    print("Invalid Option!!!")


def Payment(UserName, AddItem):
    print("Payment Page --->", UserName)
    db = open("RegistrationDetail.txt", "r")
    EventRecord = db.readlines()
    db.close()
    while True:
        Itempayment = AddItem
        for i in EventRecord:
            a, b, c, d, e, f, g, h = i.split(" , ")
            h = h.strip()
            i = i.strip()
            if Itempayment in i:
                print(i)
                Confirm = input("Do you want do make payment<Y/N>:")
                if Confirm.upper() == "Y":
                    db = open("paymentDetail.txt", "a")
                    Name = input("Account Name:")
                    Name = Name.title()
                    AccountNum = input("Bank Account No. : ")
                    Pin = input("Pin Number: ")
                    status = datetime.now()
                    db.write(a + " , " + Name + " , " + AccountNum + " , " + Pin + " , " + c + " , "
                             + g + " , " + h + " , " + str(status) + "\n")
                    db.close()
                    print("Congrats. Payment has been done!!!")
                    break
                elif Confirm.upper() == "N":
                    break
                else:
                    print("Invalid Option!!!")
        break


def RegistrationDetail():
    while True:
        db = open("RegistrationDetail.txt", "r")
        print("Registration Detail")
        selection = int(input("1.All 2.Search 0.Exit:"))
        if selection == 1:
            for i in db:
                a, b, c, d, e, f, g, h = i.split(" , ")
                h = h.strip()
                print("Username: " + a + " | Category: " + b + " | Event Name: " + c + " | Location : " + d +
                      " | Date: " + e + " | Time: " + f + " | Quantity: " + g + " | Total Price: " + h)
        elif selection == 2:
            Search = input("Search UserName: ")
            Search = Search.title()
            for i in db:
                a, b, c, d, e, f, g, h = i.split(" , ")
                h = h.strip()
                if i.startswith(Search):
                    print("Username: " + a + " | Category: " + b + " | Event Name: " + c + " | Location : " + d +
                          " | Date: " + e + " | Time: " + f + " | Quantity: " + g + " | Total Price: " + h)
        elif selection == 0:
            break
        else:
            print("Invalid Option!!! Please try again.")
        db.close()


def PaymentDetail():
    while True:
        db = open("paymentDetail.txt", "r")
        print("Payment Detail")
        selection = int(input("1.All 2.Search 0.Exit: "))
        if selection == 1:
            for i in db:
                a, b, c, d, e, f, g, h = i.split(" , ")
                h = h.strip()
                print("Username: " + a + " | Account Name: " + b + " | Bank Account No.: " + c
                      + " | Pin NO. : " + d + "\n" + " | Event Name: " + e + " | Quantity: " + f +
                      " | Total Price: " + g + " | Date & Time: " + h)
        elif selection == 2:
            Search = input("Search UserName: ")
            Search = Search.title()
            for i in db:
                a, b, c, d, e, f, g, h = i.split(" , ")
                h = h.strip()
                if i.startswith(Search):
                    print("Username: " + a + " | Name of the Payor: " + b + " | Bank Account No.: " + c
                          + " | Pin NO. : " + d + "\n" + " | Event Name: " + e + " | Quantity: " + f +
                          " | Total Price: " + g + " | Date & Time: " + h)
        elif selection == 0:
            break
        else:
            print("Invalid Option!!!, pls try again")
        db.close()


Main_Page()