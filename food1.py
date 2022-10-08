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
        print(self.Name)
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
        print("your current balance for ordering is ",self.amount)
        print("ADD BALANCE TO ENJOY YOUR TASTY FOOD ")
        self.add_mon=input("do you want to add money to wallet (Y/N):")
        if(self.add_mon == "Y"):
            self.new_amount=int(input("HOW MUCH WOULD YOU LIKE TO ADD :"))
            self.amount +=self.new_amount
            print("YOUR CURRENT WALLET BALANCE IS ",self.amount,"rupees")
        elif(self.add_mon == "N"):
            print("YOUR WALLET BALANCE IS ",self.amount)

    
a = front_page()
a.header()
a.personal_details()
a.display()
a.password()
a.wallet()   
  
