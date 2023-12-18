print("1. Add an element\n2. Delete an element\n3. Print the list")     # options to add, delete & print elements in arrays
list = []       # declaration of list 

while(True):
    try:
        optionSelected = int(input("\nSelect any option from above: "))     # variable to store the option choice
    except ValueError:
        print("Please select option from 1, 2 and 3")
    print("-------------------------------")
    try:
        # Making cases for add, delete and printing element
        match(optionSelected):
            case 1:
                # Case for adding the element
                list.append(int(input("Enter the element: ")))
                print(list)
            case 2:
                # Case for deleting the element
                list.pop(int(input("Enter the element's position: ")) - 1)
                print(list)
            case 3:
                # Case for printing the list (not element)
                print(list)
                break
            case _:
                # Case for unexpected user input (input other than 1, 2 and 3)
                print("Please select option from 1, 2 and 3\n1. Add an element\n2. Delete an element\n3. Print the list")
    except:
        print("Only integer values are acceptable!")

