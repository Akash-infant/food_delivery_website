
#for displaying in the front page

def header():
    print("****************************")
    print("TOMATO FOOD DELIVERY")
    print("****************************")
    print("FOOD THAT YOU LOVE")
    print("from")
    print("ZETA")


#for entering personal details    
def personal_details():
    Name =  input("YOUR NAME PLEASE !")
    Age =  int(input("ENTER YOUR AGE :"))
    Address=input("ENTER YOUR ADDRESS :")
    Pin = int(input("ENTER YOUR PINCODE :"))
    Dob =  input("ENTER YOUR BIRTH DATE :")
    Mail = input("ENTER YOUR MAIL ID :")
    
#display  details
def display():

#keeping a password
def password():
    print("KEEP A STRONG PASSWORD THAT HAS MINIMUM 8 CHARACTERS AND A NUMBER ")
    pass1=input("ENTER YOUR PASSWORD:")
    pass2=input("ENTER YOUR PASSWORD ONCE AGAIN :")
    if(pass1==pass2):
        pass
    else:
        print("your password is not the same ")
        

#to show balance amount in tomato wallet
def wallet():
    amount = 0
    print("your current balance for ordering is ", amount)
    
   
    
