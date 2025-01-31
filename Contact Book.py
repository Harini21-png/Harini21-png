contacts={}
def add_contact():
    name=input("enter your name:")
    phone=input("enter your phone number:")
    if name in contacts:
        add=f""" a name {name} is already existed"""
        print(add)
    else:
        contacts[name]=phone
        adds=f"""{name} is added successfully"""
        print(adds)
def view_contact():
    name=input("enter a name:")
    if name not in contacts:
        view=f"""{name} is not available"""
        print(view)
    else:
        for name,phone in contacts.items():
            views=f"""name: {name}, phone: {phone}"""
            print(views)
def del_contact():
    name=input("enter a name to delete:")
    name=name.strip()
    if name in contacts:
        del contacts[name]
        dele=f"""name {name} has deleted successfully"""
        print(dele)
    else:
        delete=f"""no contacts within the name {name}"""
        print(delete)
def search_contact():
    name=input("enter a name to search:")
    if name in contacts:
        search=f"""name:{name},phone:{contacts[name]}"""
        print(search)
    else:
        searches=f"""no contact found with the name {name}"""
        print(searches)
def contact_book():
    while True:
        print("---contact book menu---")
        print("1.add contact")
        print("2.view contact")
        print("3.delete contact")
        print("4.search contact")
        print("5.exit")
        choice = int (input("enter a number:"))
        if choice==1:
            add_contact()
        elif choice==2:
            view_contact()
        elif choice==3:
            del_contact()
        elif choice==4:
            search_contact()
        elif choice==5:
            print("exiting contact book,good bye!")
            break
        else:
            print("invalid choice. please try again")
contact_book()    