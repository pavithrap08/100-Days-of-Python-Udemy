import random

def calculate_score(cards):
    #Takes A List of Cards and Provide its Sum 
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def dealcard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def compare(u_score,c_score):
    if u_score==c_score:
        return "Its a Draw ✨🟰"
    elif c_score==0:
        return "Lose,opponent has BlackJack 😱"
    elif u_score==0:
        return "Win with a Blackjack 🤩"
    elif u_score>21:
        return "You went over, You Lose😭"
    elif c_score>21:
        return "Opponent went Over, You Win🥳"
    elif u_score>c_score:
        return "You Won 😎"
    else:
        return "You Lose 😞"
        

user_cards=[]
computer_cards=[]
computer_score=-1
users_score=-1
for _ in range(2):
    new_card=dealcard()
    user_cards.append(new_card)
    computer_cards.append(dealcard())

is_gameover=False
while not is_gameover:
    users_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your Cards:{user_cards},current score :{users_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if users_score==0 or computer_score==0 or users_score>21:
        is_gameover=True
    else:
        user_deal=input("Type 'Y' to get another card, Type 'N' to Pass: ")
        if (user_deal=='Y' or user_deal=='y'):
            user_cards.append(dealcard())
        else:
            is_gameover=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(dealcard())
        computer_score=calculate_score(computer_cards)

print(f"   Your final hand: {user_cards}, final score: {users_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(users_score, computer_score))
compare(users_score,computer_score)
