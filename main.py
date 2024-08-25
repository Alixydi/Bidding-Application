import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the game logo
def print_logo():
    logo = """
     ____  _     ____  _     ____  _____ _ ____  
    /  __|/ \ |  __|/ \ |  __|/  _/  __|  __ |/ \ 
    |  \ | | |  |  \ | | |  |  \ | | | |  \ | |
    |  /_| |_|  |  /_| |_|  |  /_| | | |  /_| |_|
    \____|_____|\____|____|\____|__\____|\____|_| 
    """
    print(logo)

# Function to get the highest bidder
def get_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    return winner, highest_bid

def main():
    bids = {}
    bidding_finished = False

    print_logo()

    while not bidding_finished:
        name = input("Enter your name: ")
        bid = int(input("Enter your bid: $"))
        bids[name] = bid

        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == 'no':
            bidding_finished = True
        elif should_continue == 'yes':
            clear_screen()

    winner, highest_bid = get_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${highest_bid}")

if __name__ == "__main__":
    main()
