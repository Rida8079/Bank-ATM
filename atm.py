class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def check_balance(self):
        print("your balance is 50000")
    def withdrawl(self, amount):
        new_amount=50000-amount
        print("you have withdrawn amount"+str(amount)+".your remaining balance is"+str(new_amount))
def main():
    card_number=input("insert your card number:->")
    pin_number=input("enter your pin number:->")
    new_user=Atm(card_number, pin_number)
    print("choose your activity")
    print("1.Balance Enquiry   2.Withdrawl")
    activity=int(input("enter activity number:->"))
    if(activity==1):

        new_user.check_balance()
    elif(activity==2):
        amount=int(input("enter the amount:->"))
        new_user.withdrawl(amount)
    else:
        print("enter your valid number")
if __name__=="__main__":

    main()