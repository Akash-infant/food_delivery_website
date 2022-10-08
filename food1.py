class front_page:
    def header(self):
        print("****************************")
        print("TOMATO FOOD DELIVERY")
        print("****************************")
        print("FOOD THAT YOU LOVE")
        print("from")
        print("ZETA")


#for entering personal details    
    def personal_details(self):
        self.Name =  input("YOUR NAME PLEASE !")
        self.Age =  int(input("ENTER YOUR AGE :"))
        self.Address=input("ENTER YOUR ADDRESS :")
        self.Pin = int(input("ENTER YOUR PINCODE :"))
        self.Dob =  input("ENTER YOUR BIRTH DATE :")
        self.Mail = input("ENTER YOUR MAIL ID :")
    
#display  details
    def display(self):
        print(self.name)
        print(self.Age)
        print(self.Address)
        print(self.Pin)
        print(self.Dob)
        print(self.Mail)
    

#keeping a password
    def password(self):
        print("KEEP A STRONG PASSWORD THAT HAS MINIMUM 8 CHARACTERS AND A NUMBER ")
        self.pass1=input("ENTER YOUR PASSWORD:")
        self.pass2=input("ENTER YOUR PASSWORD ONCE AGAIN :")
        if(self.pass1==self.pass2):
        pass
        else:
            print("your password is not the same ")
        

#to show balance amount in tomato wallet
    def wallet(self):
        self.amount = 0
        print("your current balance for ordering is ", amount)
        print("ADD BALANCE TO ENJOY YOUR TASTY FOOD ")
        self.amount=input("do you want to add money to wallet (Y/N):")
        if(self.amount == "Y"):
            self.amount_1=int(input("HOW MUCH WOULD YOU LIKE TO ADD :"))
            self.amoumt+=self.amount_1
        elif(self.amount =="N"):
            print("YOUR WALLET BALANCE IS ",self.amount)

    
a = front_page()
a.header()
a.personal_details()
a.display()
a.password()
a.wallet()   
  
