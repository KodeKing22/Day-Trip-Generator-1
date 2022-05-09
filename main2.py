# #Day Trip Generator

import random



name = input("Greetings, please tell us your name: ")

print('Hello ' + name + ',' + " Welcome to your Day Trip!")

print("We will select at random a destination, a restaurant, a mode of transportation, and a form of entertainment for your trip. If you would like to re-select any of the choices we've made just let us know. ")

# Destination

destinations = ['Paris', 'London', 'Greece', 'Switzerland', 'Barcelona',]

def d_choice():
    choice = ""
    des_choice = random.choice(destinations)
    while choice != 'Yes':
        print('Your current destination choice is: ' + des_choice)
        choice = input('Do yo like your destination selection? Yes or No: ')
        Yes = 'Great!'
        No = 'New destination selected. '
    
        if choice == 'Yes':
            print(Yes)

        elif choice == 'No':
            des_choice = random.choice(destinations)
            print(No)            
    return des_choice

final_des_choice = d_choice()   
print('Your final destination choice is: ' + final_des_choice)

# Restaurant

restaurants = ['McDonalds', 'In and Out', 'Subway', 'Chipole', 'Taco Bell', 'Waffle House', 'Starbucks', 'Dutch Bros']    

def r_choice():
    choice = ""
    rest_choice = random.choice(restaurants)
    while choice != 'Yes':
        print('Your current restaurant choice is: ' + rest_choice)
        choice = input('Do yo like your restaurant selection? Yes or No: ')
        Yes = 'Great!'
        No = 'New restaurant selected. '  
    
        if choice == 'Yes':
            print(Yes)

        elif choice == 'No':
            rest_choice = random.choice(restaurants)
            print(No)            
    return rest_choice

final_rest_choice = r_choice()   
print('Your final restaurant choice is: ' + final_rest_choice)

# Transportation 

transportation = ['Piggy Back Ride', 'Bike', 'Horse and Carriage', 'Jet Pack', 'Barefoot', 'Lambo', 'Tesla']

def t_choice():
    choice = ""
    trans_choice = random.choice(transportation)
    while choice != 'Yes':
        print('Your current mode of transportation choice is: ' + trans_choice)
        choice = input('Do yo like your mode of transportation selection? Yes or No: ')
        Yes = 'Great!'
        No = 'New mode of transportation selected. '  
    
        if choice == 'Yes':
            print(Yes)

        elif choice == 'No':
            trans_choice = random.choice(transportation)
            print(No)            
    return trans_choice

final_trans_choice = t_choice()   
print('Your final mode of transportation choice is: ' + final_trans_choice)

# Entertainment

entertainment = ['Fireworks', 'A Comedy Show', 'Jail or Prison Break', 'Sailing', 'Sight Seeing', 'Sky Diving', 'Hunting']

def e_choice():
    choice = ""
    enter_choice = random.choice(entertainment)
    while choice != 'Yes':
        print('Your current form of entertainment choice is: ' + enter_choice)
        choice = input('Do yo like your entertainment selection? Yes or No: ')
        Yes = 'Great!'
        No = 'New entertainment selected. '  
    
        if choice == 'Yes':
            print(Yes)

        elif choice == 'No':
            enter_choice = random.choice(entertainment)
            print(No)            
    return enter_choice

final_enter_choice = e_choice()   
print('Your final entertainment choice is: ' + final_enter_choice)

print('Your Day Trip is complete!' )

print('These are your final selections for your day trip: ')
print('Destination: ' + final_des_choice)
print('Restaurant: ' + final_rest_choice)
print('Transportation: ' + final_trans_choice)
print('Entertainment: ' + final_enter_choice)
 