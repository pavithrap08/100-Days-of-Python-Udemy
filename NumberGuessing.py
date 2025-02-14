logo="""_.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 

"""
import random
EASY_LEVEL=10
HARD_LEVEL=5
def start():
    turns=0
    print(logo)
    a=input("Choose the level for difficulty 'E' for Easy and 'H' for hard")
    if a=='E' or a=='e':
        turns=EASY_LEVEL
    elif a=='H' or a=='h':
        turns=HARD_LEVEL
    print(f"You Got {turns} turns , Game Start")
    val=random.randint(1,100)
    while(turns!=0):
        ip=int(input("Guess a Number between 1 to 100"))
        if ip==val:
            print("You Guessed the Right Value ! Congrats")
            break
        elif ip<val:
            print("Too Low ,Guess Higher ")
        else:
            print("Too High,Guess Higher ")
        turns-=1
    if turns==0:
        print("You Failed The Game ")
        ask=input("Press 'S' to Start Again or 'E' to End ")
        if ask=='S' or ask=='s':
            print("\n"*20)
            start()    
start()
