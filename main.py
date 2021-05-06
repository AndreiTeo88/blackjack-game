import random
from art import logo
from replit import clear

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,  10]
  player = random.choice(cards)
  return player

def calculate_score(list_of_cards):
  """Calculates the score from a list of cards"""
  if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
      return 0
  if 11 in list_of_cards and sum(list_of_cards) > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
  return sum(list_of_cards)

def compare(player, computer):
  """Compares the value betwen player and computer"""
  if player > 21 and computer > 21:
    return "You went over. You lose"

  if player == computer:
    return "Draw"
  elif computer == 0:
    return "Lose, opponent has Blackjack"
  elif player == 0:
    return "Win with a Blackjack"
  elif player > 21:
    return "You went over. You lose"
  elif computer > 21:
    return "Opponent went over. You win"
  elif player > computer:
    return "You win"
  else:
    return "You lose"
    
def blackjack_game():
  print(logo)

  user_cards = []
  computer_cards = []
  end_game = False

  for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not end_game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer first card: {computer_cards[0]}")

    if computer_score == 0 or user_score == 0 or user_score > 21:
      end_game = True
    else:
      continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
      if continue_game == "y":
        user_cards.append(deal_card())
      else:
        end_game = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack_game()
