def phonebook(phone_book):
    def add_num():
        user_1 = input("To add a number press y or n to go back to main menu:")
        while user_1 != 'y' and user_1!= 'n':
            print("enter only y or n!")
            user_1 = input("To add a number press y or n to go back to main menu:")
        while user_1!='n':
            name  = input("Please enter the name of the person:")
            number= input("Please enter the number            :")
            phone_book[name] = number
            user_1 = input("To add a number press y or n to go back to main menu:")
        if user_1=='n':
            phonebook(phone_book)
        phonebook(phone_book)
    def del_num():
        del_name = input("Please enter the name to delete:")
        del phone_book[del_name]
        print("Number successfully deleted!")
        user_2 = input("\nTo view the phonebook press v\nTo del a num press d\nChoose your option:")
        while user_2 != 'v' and user_2 != 'd':
            print("Please enter 'v' or 'd' only!")
            user_2 = input("To view the phonebook press v\nTo del a num press d\nChoose your option:")
        if user_2 == 'v':
            view_phonebook()
        elif user_2 == 'd':
            del_num()

    def view_phonebook():
        for key,val in phone_book.items():
            print("{:^10}:{:10}".format(key,val))
        user_2 = input("\nTo view the phonebook press v\nTo del a num press d\nChoose your option:")
        while user_2 != 'v' and user_2 != 'd':
            print("Please enter 'v' or 'd' only!")
            user_2 = input("To view the phonebook press v\nTo del a num press d\nChoose your option:")
        if user_2 == 'v':
            view_phonebook()
        elif user_2 == 'd':
            del_num()

    if phone_book == {}:
        print("Your phone_book is empty")
        add_num()
    else:
        user_2 = input("\nTo view the phonebook press v\nTo del a num press d\nChoose your option:")
        while user_2!='v' and user_2!='d':
            print("Please enter 'v' or 'd' only!")
            user_2 = input("To view the phonebook press v\nTo del a num press d\nChoose your option:")
        if user_2=='v':
            view_phonebook()
        elif user_2=='d':
            del_num()


phone_book = {}
user = input("To go into phonebook press y or q to exit : ")
while user!='y' and user!='q':
    print("enter only y or q!")
    user = input("To go into phonebook press y or q to exit : ")
if user=='y':
    phone_book = phonebook(phone_book)
else:
    print("Bye")