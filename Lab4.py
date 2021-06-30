#def triangle_area (base, height):
    #area = (1/2)(base * height)
    #return(area)
#print( triangle_area(3,4) ) # would return 6 and print to console
#print( triangle_area(8,11) ) # would return 44 and print to console

from typing import Counter


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

def restock (shoe_name, multiplier):
    newInv = shoe_inv[shoe_name] * multiplier 
    return newInv
print(restock("Yeezy", 3))

def clearance_sale (shoe_name, dividor):
    newInv = shoe_inv[shoe_name] / dividor
    return newInv
print(clearance_sale("SB Dunk", 5))

city_names = ["Oakland","Seattle", "Atlanta", "New York City", "Memphis", "Miami", "Los Angelos", "New Orleans"]

def printCityNames(cities_list):
    counter = 0 
    while counter < len(cities_list):
        print(cities_list[counter])
        counter += 1
        return "completed"
printCityNames(city_names)
