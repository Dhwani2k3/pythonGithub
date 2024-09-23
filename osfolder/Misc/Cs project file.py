

def mainmenu():
      
      while True:
            print()
            print("1. CUSTOMER DETAILS :: ")
            print("2.  Booking Record :: ")
            print("3.  Calculate Room Rent :: ")
            print("4.  Calculate Resturent Bill :: ")
            print("5.  Calculate Total bill of Customer :: ")
            choice=int(input("ur choice plz:"))
            print()
            if choice==1:
                  Customerdetails()
            elif choice==2:
                  BookingRecords()
            elif choice==3:
                  RoomRent()
            elif choice==4:
                  Resturentbill()
            elif choice==5:
                  Totalbill()
            else:
                  print("INVALID CHOICE")



def Customerdetails():
      
      while True:
            print()
            print("main menu")
            print("11. insert")
            print("12. read")
            print("13. search")
            print("14. update")
            print("15. exit")
            ch=int(input("what do u want to do? :: "))
            if ch==15:
                  break
            print()

            if ch==11:
                  def  Insertingdetails():
                        import pickle
                        record=[]
                        while True:
                              c_id=int(input('customer_id ::'))   #customer_id
                              c_name=input('customer name ::')     #name of customer
                              c_phno=int(input('contact no of customer ::') ) #contact no
                              c_country=input('country of customer   ::')      # country from where customer belong
                              c_age=int(input('age of customer ::'))
                              checkin=input("enter check in date ::")
                              checkout=input("enter check out date ::")
                               # all details of customer
                              customer_details=[c_id,c_name,c_phno,c_country, c_age,checkin,checkout]
                              record.append(customer_details)
                              wish=input('want to add more data yes/no ::')  # want to add more data or no
                              if wish.upper()=='NO':             # if yess then do not write no & if no then write
                                     break
                        file=open('customerdetails.dat','ab+')   # adding record in binary file 
                        pickle.dump(record,file)                          # writing details
                        print('records added')                              # record added
                        file.close()
                  Insertingdetails()                      # calling function ()

            elif ch==12:
                  def Readingfile():
                        import pickle
                        file=open('customerdetails.dat','rb+')
                        try:
                              print(' the contents of the files are : ')
                              while True:
                                    cus_d=pickle.load(file)
                                    for c in cus_d:
                                          print("Customer id : ",c[0])
                                          print("Customer name : ",c[1])
                                          print("Customer phno. : ",c[2])
                                          print("Customer country : ",c[3])
                                          print("Customer age : ",c[4])
                                          print("Customer check in details :: ",c[5])
                                          print("Customer check out details :: ",c[6])
                        except  EOFError:
                              pass
                        file.close()
                  Readingfile()

            
            elif ch==13:
                  def Searchingdetails():
                        import pickle
                        file=open('customerdetails.dat','rb+')
                        cus_d=pickle.load(file)
                        s=0
                        customer_id=int(input(' id of customer :: '))
                        for c in cus_d:
                             if c[0]==customer_id:
                                    print('record found')
                                    print('customer_id : ',c[0])
                                    print('customer_name : ',c[1])
                                    print('customer_phno : ',c[2])
                                    print('customer_country : ',c[3])
                                    print('customer_age : ',c[4])
                                    s=1
                                    break
                        if s==0:
                              print(" id of customer is not found")
                        file.close()
                  Searchingdetails()



            elif ch==14:
                  def Updatingdetails():
                        import pickle
                        file=open('customerdetails.dat','rb+')
                        cus_d=pickle.load(file)
                        u=0
                        customer_id=int(input(" id of customer :: "))
                        for c in cus_d:
                              if c[0]==customer_id:
                                    print('record found')
                                    print('customer_id unique : ',c[0])
                                    print('customer_name : ',c[1])
                                    print('customer_phno : ',c[2])
                                    print('customer_country : ',c[3])
                                    print('customer_age : ',c[4])
                                    c[1]=input("Booking by new name :: ")
                                    c[2]=int(input("Booking by new phone no :: "))
                                    c[3]=input(" country of customer :: ")
                                    c[4]=int(input("age of customer :: "))
                                    u=1
                                    print("record is updated")
                                    break
                        if u==1:
                              file.seek(0)
                              pickle.dump(cus_d,file)
                              print("details updated")
                        file.close()
                  Updatingdetails()
                  
                                    
                                    
                                    
                                    
def BookingRecords():
      import pickle
      print("21. read")
      print("22. exit")
      while True:
            print()
            ch=int(input("what do u want to do? :: "))
            if ch==22:
                  break
            print()
            if ch==21:
                  def Readingfile():
                        import pickle
                        file=open('customerdetails.dat','rb')
                        try:
                              print('the contents of the file')
                              while True:
                                    bkgd=pickle.load(file)
                                    for b in bkgd:
                                          print("Customer id : ",b[0])
                                          print("Customer check in details :: ",b[5])
                                          print("Customer check out details :: ",b[6])
                        except  EOFError:
                              pass
                        file.close()
                  Readingfile()

 
def RoomRent():
      import pickle
      file=open('customerdetails.dat','rb+')
      cus_d=pickle.load(file)
      customer_id=int(input(" id of customer :: "))
      for c in cus_d:
            if c[0]==customer_id:
                  print("we have 3 types of room :: ")
                  print(" Type 1 -----> 7 star  \n Type 2 -----> 5 star \n Type 2 -----> 3 star  ")
                  print("Price of rooms are according to (per night in rs)::  " )
                  print("Type 1 --->3000 \n Type 2 ---> 2000 \n Type 2 ---> 1000 ")
                  n=int(input("no of nights :: "))
                  typ=int(input("enter ur choice :: "))
                  nty=0
                  if typ==1:
                         nty=n*3000
                         print("u=your total room rent is :: ",nty)
                  elif typ==2:
                        nty=n*2000
                        print("u=your total room rent is :: ",nty)
                  elif typ==3:
                        nty=n*1000
                        print("u=your total room rent is :: ",nty)
                  else:
                        print(" please choose any type")
      return nty
      file.close()
            

def Resturentbill():
      import pickle
      file=open('customerdetails.dat','rb+')
      cus_d=pickle.load(file)
      customer_id=int(input(" id of customer :: "))
      for c in cus_d:
            if c[0]==customer_id:
                  print("-->we have 2 types of food \n-->only veg and both veg & non veg")
                  print("-->'veg' for only veg &  'bnv' for both non veg and veg")
                  fdch=input("what type of food u want :: ")
                  if fdch=='veg':
                        print("R1.Cost of breakfast including tea/coffee :: 200  ")
                        print("R2.Cost of lunch including juice/curd etc :: 200  ")
                        print("R3.Cost of evening snacks including tea/coffee :: 100  ")
                        print("R4.Cost of dinner including milk :: 200  ")
                        print("In free \n water (always) ,1 tea/coffe in a day ")
                        print()
                        print("1.   Only option R1 ")
                        print("2.   Only option R4 ")
                        print("3.   Both R1 & R4  only ")
                        print("4.   Both R1 & R2  only ")
                        print("5.   Both R3 & or any other meal only ")
                        print("6.   All four options ")
                  
                        fdct=int(input("enter choice :: "))
                        no=int(input("no. of days"))
                        nft=0
                        if fdct==1 or fdct==2 :
                              nft=no*200
                              print("Ur total bill of one time meal  is :: ",nft)
                        elif fdct==3 or fdct==4:
                              nft=no*400
                              print("Ur total bill of  two time meal is :: ",nft)
                        elif fdct==5:
                              nft=no*300
                              print("Ur total bill of evening and or anyother meal is :: ",nft)
                        elif fdct==6:
                              print("on having all four meal there in 100 rs discount")
                              nft=no*600
                              print("Ur total bill of all 4 meal with Rs100 discount is ::",nft)
            

                  elif fdch=='bnv':
                        print("R1.Cost of breakfast including tea/coffee :: 300  ")
                        print("R2.Cost of lunch including juice/curd etc :: 300  ")
                        print("R3.Cost of evening snacks including tea/coffee :: 100  ")
                        print("R4.Cost of dinner including milk :: 300  ")
                        print("In free \n water (always) ,1 tea/coffe in a day ")
                        print("1.   Only option R1 ")
                        print("2.   Only option R4 ")
                        print("3.   Both R1 & R4  only ")
                        print("4.   Both R1 & R2  only ")
                        print("5.   Both R3 & or any other meal only ")
                        print("6.   All four options ")

                        fdct=int(input("enter choice :: "))
                        no=int(input("no. of days"))
                        nft=0
                        if fdct==1 or fdct==2 :
                              nft=no*300
                              print("Ur total bill of one time meal  is :: ",nft)
                        elif fdct==3 or fdct==4:
                              nft=no*600
                              print("Ur total bill of  two time meal is :: ",nft)
                        elif fdct==5:
                              nft=no*400
                              print("Ur total bill of evening and or anyother meal is :: ",nft)
                        elif fdct==6:
                              print("on having all four meal there in 200 rs discount")
                              nft=no*800
                              print("Ur total bill of all 4 meal with Rs200 discount is ::",nft)
                  else:
                          print("choose any food type")
                          pass
      return nft
      file.close()


def Totalbill():
      r1=Resturentbill()
      r2=RoomRent()
       
      totalbill=r1+r2
      print(r1,"+",r2)
      print("Total bill of customer is :: " ,totalbill)
      print("including room rent , resturent bill")
      
            
mainmenu()

                        
                  
                        
                                          
                        
                  
                              
                              
      

            


      

            
            
                  
                  
            
      
            

