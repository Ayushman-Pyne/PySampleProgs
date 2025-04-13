from random import randint as r
def toss():
    gc = True
    while gc:
        while True:
            uc = input("Enter Your Choice(H/T): ")
            if uc in "Hh":
                print("Computer takes Tails.")
                break
            elif uc in "Tt":
                print("Computer Takes Heads.")
                break
            else:
                print("WRONG INPUT! TRY AGAIN...")
                continue
        while True:
            un = int(input("Enter a number for Toss(1-6): "))
            cn = r(1,6)
            print(f"Computer Gives {cn}")
            if un >= 1 and un <= 6:
                ch = cn + un
                if(ch % 2 == 0):
                    if(uc in "Hh"):
                        print("Computer Wins!")
                    else:
                        print("User Wins!")
                else:
                    if(uc in "Tt"):
                        print("Computer Wins!")
                    else:
                        print("User Wins!")
                break
            else:
                print("Wrong Input! Try again...")
                continue
        print("Good Game!")
        gc = input("Wanna Play Again(Y/N)? ") in "Yy"
        print(gc)
