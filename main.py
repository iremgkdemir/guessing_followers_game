import random
from art import logo, vs
from game_data import data
from replit import clear

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def game():
    # Random selection for the first and second accounts
    compare = get_random_account()
    against = get_random_account()

    # Follower counts for the selected accounts
    c_count = compare['follower_count']
    a_count = against['follower_count']

    print(logo)

    # Ensure compare and against are not the same
    while compare == against:
        against = get_random_account()

    # Display the details of the accounts being compared
    print(f"Compare A: {compare['name']}, a {compare['description']}, "
          f"from {compare['country']}.")
    # print(c_count) # Commented out follower count to reduce output

    print(vs)

    print(f"Against B: {against['name']}, a {against['description']}, "
          f"from {against['country']}.")
    # print(a_count) # Commented out follower count to reduce output

    compare_followers(c_count, a_count)

# Global variable for user score
user_score = 0

def compare_followers(A, B):
  global user_score
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()  
  # Check if user's guess is correct
  if (guess == 'A' and A > B) or (guess == 'B' and B > A):  
    user_score += 1  # Increment user's score if the guess is correct
    clear()  # Clear the console
    print(f"You're right! Current score: {user_score}.") 
  
  else:
    clear()  
    print(f"Sorry, that's wrong. Final score: {user_score}")  
    return  # Exit the function

  game()  # Start a new game round after evaluating user's guess

game()


