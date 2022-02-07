#restaurant.py
#Antonio Vinagre, s1303334
#CS-175L
#Spring 2022

vegetarian = False
vegan = False
gluten_free = False

inp_vgtrn = input('Is anyone in your party a vegetarian? ')

if inp_vgtrn == "yes":
    vegetarian = True

inp_vgn = input('Is anyone in your party a vegan? ')

if inp_vgn == "yes":
    vegan = True

inp_gltnfr = input('Is anyone in your party gluten free? ')

if inp_gltnfr == "yes":
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
