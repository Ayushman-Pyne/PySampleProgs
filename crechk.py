# Credit card Validator program(Beginner)
# Step 1 - Remove any '-' or ' '
# Step 2 - Add all digits in the odd places from right to left
# Step 3 - Double Every second digit from right to left
#           (If result is a two digit number , add the two digit number together to get a single digit)
# Step 4 - Sum of totals from Step 2 and 3
# Step 5 - If Sum is divisible by 10, the credit card number is valid.

# Step 1

credit_card = "4111111111111111"
credit_card = credit_card.replace("-","")
credit_card = credit_card.replace(" ","")
credit_card = credit_card[::-1]


# Step 2

odd_sum = 0
for x in credit_card[::2]:
    odd_sum += int(x)

# Step 3

even_sum = 0
for x in credit_card[1::2]:
    x = int(x) * 2
    if x > 10:
        even_sum += (1 + x%10)
    else:
        even_sum += x

# Step 4

tot_sum = even_sum + odd_sum

# Step 5

if(tot_sum%10 == 0):
    print("Valid")
else:
    print("Not Valid")
