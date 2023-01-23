#deck of cards
import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose,opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over.You lose"
    elif computer_score>21:
        return "Opponent went over.You win"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    usercards=[]
    computer_cards=[]
    is_game_over=False
    for i in range(2):
        usercards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(usercards)
        computer_score=calculate_score(computer_cards)

        print(f"You have choosen cards {usercards} and yourscore is {user_score}")
        print(f"Computer first card {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True

        else:
                        
            user_input=input("type y to add new card and n to pass")
            if user_input=="y":
                usercards.append(deal_card())
            else:
                is_game_over=True
            
    while computer_score!=0 and computer_score<17:
                computer_cards.append(deal_card())
                computer_score=calculate_score(computer_cards)


    print(f"your score is {user_score} and computer score is {computer_score}")
    print(compare(user_score,computer_score))
play_game()
while(input("want to restart y or n")=="y"):
     play_game()
   
    


