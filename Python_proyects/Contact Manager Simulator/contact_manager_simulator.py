contacts = {

}
while True:
    print(1, "add contact")
    print(2, "search contact")
    print(3, "show contacts")
    print(4, "clean contacts")
    print(5, "exit")
    option = int(input("choose an option: "))
    if option == 1:
        name = input("put the name of the contact: ")
        phone = int(input("put the phone of the contact(ej:3102414141): "))
        contacts[name] = phone
    elif option == 2:
        print("what are you searching?")
        print(1, "name of the contact")
        print(2, "phone of the contact")
        option2 = int(input("choose an option: "))
        if option2 == 1:
            name_search = int(input("put the phone of the contact who are you searching: "))
            for name, phone in contacts.items():
                if name_search in contacts.values():
                    print(f"the name of the contact is: {name}")
                else:
                    print("the contact doesn't exist")
        elif option2 == 2:
            phone_search = input("put the name of the contact who are you searching: ")
            for name, phone in contacts.items():
                if phone_search in contacts.keys():
                    print(f"the phone of the contact is: {phone}")
                else:
                    print("the contact doesn't exist")
        else:
            print("isn't a valide option")
    elif option == 3:
        print(contacts)
    elif option == 4:
        contacts.clear()
        print("the contacts was cleaned")
    elif option == 5:
        print("Goodbye")
        break
    else:
        print("isn't a valide option")