# ATM Code
# variable
Atm_card = "card"
pin = 1234
Money = 1000
Temp = 0

# code starts
for outer in [1,2,3,4]: # 1 2
# outer for loop you are the person
    print("You are in front of atm machine")
    print("insert your card")
    print ("enter your pin")

    # If
    if (Atm_card == "card") & (pin == 1234): # True
        # Nested If
        if outer <= 3: # 2 == 1 False
            # ATM Machine
            while Temp <= Money:# 0 <= 1000 ture
                print( "count", Temp, "Total Amount", Money)
                Temp = Temp + 100 # 0 100 200 300 400
        else:
            print("only three atempt is possible")
            break
        print("take your money", Money, "rupee")
        Temp = 0
        print("===================")
    elif (Atm_card == "card") | (pin == 1234):
        print("any one value is worng")
    else:
        print("both values are wrong")
        print("Thank you for use") 