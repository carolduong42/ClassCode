#def triangle_area (base, height):
    #area = (1/2)(base * height)
    #return(area)
#print( triangle_area(3,4) ) # would return 6 and print to console
#print( triangle_area(8,11) ) # would return 44 and print to console

def trapezoid_area (base, base2, height):
    area =( (base + base2)* height)/2 
    return area
print(trapezoid_area(2,17,11))

grocery_list = {"chicken": 1.59, "beef" : 1.99, "cheese" : 1.00, "milk": 2.50 }
#beef = 1.99
#cheese = 1.00
def total_price (beef, cheese) :
    #total_price = (beef + cheese)
    total_price = grocery_list[beef] + grocery_list[cheese]
    return total_price
string = 'the total price of beef and cheese is 2.99'
print(total_price("beef", "cheese") and string)

def price_difference (beef, cheese) : 
    #price_difference = (beef - cheese)
    total_price = grocery_list[beef] - grocery_list[cheese]
    return price_difference
string = 'the difference between beef and cheese is 0.99'
print(price_difference("beef", "cheese") and string)

shoe_inv =  {"Jordan 13": 1, "Yeezy" : 8, "Foamposite" : 10, "Air Max": 5, "SB Dunk": 20}
yeezy = 8
def restock (yeezy):
#def restock (shoe_name, multiplier):
    restock = (yeezy * 3) 
    #newInv = shoe_inv[shoe_name] * multiplier 
    return restock
print(restock(yeezy))

SB_Dunk = 20
def clearance_sale (SB_Dunk):
    clearance_sale = (SB_Dunk / 4)
    return clearance_sale
print(clearance_sale(SB_Dunk))

