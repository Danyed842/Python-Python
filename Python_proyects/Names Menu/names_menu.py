names = [ ]
while True:    
    print(f"What do you want to do?:")
    print(f"1. save names in the list")
    print(f"2. remove or show the list")
    print(f"3. exit")
    option = int(input("choose an option: "))
    if option == 1:  
        name = input("put the name to add: ")
        names.append(name)
    elif option == 2:
        print(f"1.remove") 
        print(f"2.show")
        optionb = int(input("choose the option that you need: "))
        if optionb == 1:
            names.clear()
            print("list cleaned.")
        elif optionb == 2:
            print(names)
    elif option == 3:
        print("bye")
        break 
