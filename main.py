# Assignment 
'''Make a game :  logo print (ASCII art)
Input Name of user :
Input User bids : The bids comes against the number
Saves in dictionary.
Asks user to bid again : yes/no
The screen gets cleared and asks the new user to bid again (Import clear function.)
After no , exits from while loop.
Prints the name of Highest bidder and the price.'''


import os
from image import logo, yo
# Clears the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)


bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("Enter your name: ")
    bid = float(input("Enter your bid: $"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        clear()

highest_bidder = ""
highest_bid = 0

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

clear()
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid:.2f}")
print(yo)
