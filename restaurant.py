#restaurant.py
#Antonio Vinagre, s1303334
#CS-175L
#Spring 2022

while True:
    vegetarian = False
    vegan = False
    gluten_free = False

    inp_vgtrn = input('Is anyone in your party a vegetarian? ')

    if inp_vgtrn.lower() == "yes":
        vegetarian = True

    inp_vgn = input('Is anyone in your party a vegan? ')

    if inp_vgn.lower() == "yes":
        vegan = True

    inp_gltnfr = input('Is anyone in your party gluten free? ')

    if inp_gltnfr.lower() == "yes":
        gluten_free = True

    print('Here are your restaurant choices:')

    if not vegan == True and not vegetarian == True and not gluten_free == True:
        print('Joe\'s Gourmet Burgers')

    if vegan == False and gluten_free == False:
        print('Mama\'s Fine Italian')

    if vegan == False:
        print('Main Street Pizza Company')

    print('Corner Café')
    print('The Chef\'s Kitchen')

    redo = input("Do you want to do another search? ")
    if redo.lower() == "no":
        break
