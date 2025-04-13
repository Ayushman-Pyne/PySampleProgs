# Python Banking Program

def show_balance(balance):
    print("===========================")
    print(f"Your balance is ${balance:.2f}")
    print("===========================")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("===========================")
        print("Not a Valid Amount.")
        print("===========================")
        return 0
    else:
        return amount

def withdraw(balance):
    amount =  float(input("Enter an amount to be withdrawn: "))

    if(amount > balance):
        print("===========================")
        print("Insufficient Funds")
        print("===========================")
        return 0
    elif(amount<0):
        print("===========================")
        print("Not a valid Amount")
        print("===========================")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("======Banking Program======")
        print("1.             Show Balance")
        print("2.                  Deposit")
        print("3.                 Withdraw")
        print("4.                     Exit")
        print("===========================")

        choice = int(input("Enter a Choice(1-4): "))
        print("===========================")

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("Wrong Input Try again")
                print("===========================")

    print("Thank You!")

if __name__ == "__main__":
    main()