import super as sp
import information as info

print('super market project'.upper().center(150))
print('made by ahmed gamal'.upper().center(150))
print('*********** Good Luck **********'.center(150).upper())
text="""
    Main Menu
        1. Create Product
        2. Display Allproduct
        3- Search
        4- Delete Product
        5- Exit"""
print(text)

obj=sp.supermarket()
while True:
    try:
        x = int(input("please enter 1-5 to complete in program :- "))
        if x == 1:
            val = info.Information(input('Enter name :- '), int(input('Enter price :- ')), input('Enter type :- '))
            if len(val.name) != 0 and val.price > 0 and len(val.type) != 0:
                obj.create({'name': val.name, 'price': val.price, 'type': val.type})
            else:
                print('sorry not doing process create product')
        elif x == 2:
            obj.display()
        elif x == 3:
            print(obj.search(input("enter name of product to search :- ")))
        elif x == 4:
            obj.delete(input("enter name of product to delete :- "))
        elif x == 5:
            break
    except ValueError:
        print('write number only between (0,5)')