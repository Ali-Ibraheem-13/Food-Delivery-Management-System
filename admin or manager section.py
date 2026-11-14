
#Main Data Section
import random
import time
t = time.localtime()
now = f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'
key = 'Ali13@@'
Order_Summary = []
Account = 0
#Afternoon
dish1 = ['Heavy meals', 'mini meals', 'spicy food', 'fast food', 'veg or Non-veg']
Restaurant1 = ['paradise', 'bawarchi', 'pista', 'Hotel grand', 'Masthi Dhaaba']
p1 = [60, 49, 60, 75, 99]

#evening
dish2 = ['Hot Drinks', 'Protein Fluids', 'Popcorn Special', 'Desi Snack', 'Light Juices']
Restaurant2 = ['Friendly Cafe', 'Mirchi Crack', 'Pretty Knock**Dock', 'Cool Breeze', 'Until Full']
p2 = [15, 35, 25, 40, 30]

#night
dish3 = ['Soups & Comfort Bowls', 'Light & Healthy Plates', 'Curd Rice Bowl ', 'Light Tiffins', 'Bread Omlette']
Restaurant3 = ['Taj Falaknuma Palace', 'ITC Kohenur', 'The Golkonda Hotel', 'Radisson Hotel', 'Ginger Hyderabad']
p3 = [129, 150, 89, 50, 90]

#morning
dish4 = ['Freshly Baked Bread Basket', 'Masala Omelette/Plain Omelette', 'Idli & Vada with Sambar', 'Sprout Salad', 'Paratha with Pickle & Curd', 'Dosa (Plain/Masala)']
Restaurant4 = ['FabHotel Limestone', 'Hotel Minerva Grand', 'Hotel Rizwan', 'Mini-Break', 'DieT🥗Content', 'Try and Taste']
p4 = [67, 49, 30, 59, 70, 70]
settings = 'Customers','Delivery Partners','Orders','Payments','Offers & Coupons','Reports'

print('🎀'*10,'🎈'*6,'🎀'*10)
login_person = input('Are You Chief/Customer(1/2):')

#Chief section
if login_person == '1':
   while True:            
      if 12<= t.tm_hour <16:
                        print('*'*5,'Good Afternoon Chief ','*'*5)
                        Dish,Restaurant,Price = dish1,Restaurant1,p1
      elif 16<= t.tm_hour <20:
                        print('*'*5,'Good Evening Chief ','*'*5)
                        Dish,Restaurant,Price = dish2,Restaurant2,p2
      elif 20<= t.tm_hour <=23:
                        print('*'*5,'Good Night Chief ','*'*5)
                        Dish,Restaurant,Price = dish3,Restaurant3,p3
      else:
         print('*'*5,'Good Morning Chief ','*'*5)
         Dish,Restaurant,Price = dish4,Restaurant4,p4
      #password section for chief
      setup = input('Do you like to modify credentials (yes/no):')
      if setup == 'yes':
                 alphabet1 = input("enter a  upper-caseletter :")#A
                 alphabet2= input("enter a lower-case letter :")#li
                 num = input("enter a number :")#13
                 password=alphabet1+alphabet2+num
                 print( "the password is :",password)#Ali13@@
                 if alphabet1== alphabet1.upper() and  alphabet2 == alphabet2.lower()  and num.isdigit():
                        print('Login Successfully')
                        break
                 else:
                   print('password does not meet all requirements')
             #direct login
      elif setup == 'no':
                  sign_in = input('enter password:')
                  if sign_in == key:
                     print('Login Successfully')
                     break
                  else:
                     print('password is not correct please Retry') 
   b = input('Do you want to show foods(yes/no) :')
   # food system analyze and things over to change
   if b == 'no':
         C =  input('Do you want to see the Work Amenities (yes/no):')
         if C == 'yes':
            i = 1
            while i<=len(settings):
               print(i,'.',settings[i-1],sep='')
               i = i+1
         elif C == 'no':
            change = input('Do you want make any changes (yes/no):')
            if change == 'yes':
                change_1= input('Do you want to add or remove any things(1/2):')
                if change_1 == '1':
                   add_food_item = input('enter  food item:')
                   add_restaurent_item = input('enter  restaurent item:')
                   add_price = input('enter  price:')
                   Dish.append(add_food_item)
                   Restaurant.append(add_restaurent_item)
                   Price.append(add_price)
                   print('Item added successfully')
                   print('-'*6,'The updated menu','-'*6)
                   print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
                   i = 1
                   while i <= len(Dish):
                    dish_with_emoji = f"🍴{Dish[i-1]}"
                    res_with_emoji = f"✦{Restaurant[i-1]}" 
                    print(f'{i:<6}{dish_with_emoji:<32}{res_with_emoji:<30}{Price[i-1]:>8}')
                    i += 1
                   
                elif change_1 == '2':
                   remove_food_item = input('enter  food item:')
                   remove_restaurent_item = input('enter  restaurent item:')
                   remove_price = input('enter  price:')
                   
                   if change_1 == '2' and remove_food_item in Dish:
                       Dish.remove(remove_food_item)
                       Restaurant.remove(remove_restaurent_item)
                       Price.remove(remove_price)
                       print('item removed successfully')
                       print('-'*6,'The updated menu','-'*6)
                       print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
                       i = 1
                       while i <= len(Dish):
                          dish_with_emoji = f"🍴{Dish[i-1]}"
                          res_with_emoji = f"✦{Restaurant[i-1]}" 
                          print(f'{i:<6}{dish_with_emoji:<32}{res_with_emoji:<30}{Price[i-1]:>8}')
                          i += 1
                   else:
                      print('item not found')
               
            elif change == 'no':
                order = input('Do you want to see the orders (yes/no):')
                if order == 'yes':
                   print('current orders are:0')
                else:
                  pass
            else:
             print('Invalid Option')
   elif b == 'yes':
               print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
               i = 1
               while i <= len(Dish):
                    dish_with_emoji = f"🍴{Dish[i-1]}"
                    res_with_emoji = f"✦{Restaurant[i-1]}" 
                    print(f'{i:<6}{dish_with_emoji:<32}{res_with_emoji:<30}{Price[i-1]:>8}')
                    i += 1

                
               
                
               
               
       
   elif b == 'yes':
            print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
            i = 1
            while i <= len(Dish):
               dish_with_emoji = f"🍴{Dish[i-1]}"
               res_with_emoji = f"✦{Restaurant[i-1]}"
               print(f'{i:<6}{Dish[i-1]:<32}{Restaurant[i-1]:<30}{Price[i-1]:>8}')
               i += 1
                
              
              
              
   elif b == 'yes':
              print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
              i = 1
              while i <= len(Dish):
               dish_with_emoji = f"🍴{Dish[i-1]}"
               res_with_emoji = f"✦{Restaurant[i-1]}" 
               print(f'{i:<6}{Dish[i-1]:<32}{Restaurant[i-1]:<30}{Price[i-1]:>8}')
               i += 1
               
              
   else:
    print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<32}{"Prices":>11}')
    i = 1
    while i <= len(Dish):
      dish_with_emoji = f"🍴{Dish[i-1]}"
      res_with_emoji = f"✦{Restaurant[i-1]}"
      print(f'{i:<6}{Dish[i-1]:<32}{Restaurant[i-1]:<30}{Price[i-1]:>8}')
      i += 1
      
       
  
                  
#Customer section
if login_person == '2':
   cnt = 0
   customer = ''
   while True:
    print('🌟'*8,'🫶 Amma Foods Welcomes You 🫶','🌟'*8)
    password = input('Are you an existing account holder or New Holder(1/2):')
    if password == '1':
               name=input('enter your Name:')
               gender = input('Enter your Gender (M/F):').upper()
               if gender == 'M':
                  print('HI',name ,'👨‍')
               else:
                  print('HI',name,'👧')
               a = input('Do you want to login with Mail or Mobile Number (1/2):')
               if a == '1':
                    mail = input('please provide your mail:')
                    if mail.endswith('@gmail.com'):
                       otp = random.randint(1000,9999)
                       print('your OTP:',otp)
                       OTP  = int(input('please enter OTP:'))
                       if otp == OTP:
                          print('*'*7,'Your are logged in Successfully','*'*7)
                          break
                          cnt = cnt+1
                       else:
                         print('Invalid OTP Entered')
               elif a == '2':
                     mobile_number = input('enter your mobile number:')
                     if len(mobile_number)== 10 and mobile_number.isdigit():
                        otp = random.randint(1000,9999)
                        print('your OTP:',otp)
                        OTP  = int(input('please enter OTP:'))
                        if otp == OTP:
                          print('*'*7,'Your are logged in Successfully','*'*7)
                          break
                          
                        else:
                         print('Invalid OTP Entered')
                     else:
                      print('Credentials are Invalid')
               

    elif password == '2':
             name=input('enter your Name:')
             gender = input('Enter your Gender (M/F/not to say):')
             if gender == 'M':
                  print('HI',name ,'👨‍')
             else:
               print('HI',name,'👧')
             mail = input('please enter your mail:')
             customer += name[:]
             if mail.endswith('@gmail.com'):
                   otp = random.randint(1000,9999)
                   print('your OTP:',otp)
                   OTP  = int(input('please enter OTP:'))
                   if otp == OTP:
                        print('*'*7,'Your are logged in Successfully','*'*7)
                        break
                   else:
                     print('Invalid OTP Entered')
             else:
               print('Invalid Credentials')
   else:
      print('Try again')
      
#Customer View Section              
if login_person == '2':
   print('😋😋 What you Try Today 😋😋')
   B = input('Do you want to show foods(yes/no) :')
   quantity = []
   if B == 'no':
       c =  input('Do you need any Assisstance or to open Menu (1/2):')
       if c == '1':
            print('please Dial XXXXX-XXXXX for any queries')
            
            
       elif c == '2':
            print('📋Explore Services🔧')
            print('✯Account options','Order Details','Coupons and Cashback','Feedback',sep= '\n✯')
            
           
            
       else:
         print('Invalid Option')
               
   elif B == 'yes' and 12<= t.tm_hour <16:
               print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
               quantity = []
               i = 1
               while i<= len(dish):
                print(f'{i:<6}{dish[i-1]:<32}{restaurant[i-1]:<30}{price[i-1]:>8}')
                i += 1
               
       
   elif B == 'yes' and  16<= t.tm_hour <20:
              print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
              quantity = []
              while i<= len(dish):
                print(f'{i:<6}{dish[i-1]:<32}{restaurant[i-1]:<30}{price[i-1]:>8}')
                i += 1
              
              
   elif B == 'yes' and  20<= t.tm_hour <24:
              print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
              quantity = []
              i = 1
              while i <= len(dish):
               print(f'{i:<6}{dish[i-1]:<32}{restaurant[i-1]:<30}{price[i-1]:>8}')
               i += 1
              
              
   else:
      print(f'{"S.no":<6}{"Food name":<32}{"Restaurant Name":<30}{"Prices":>11}')
      quantity = []
      i = 1
      while i <= len(dish):
         print(f'{i:<6}{dish[i-1]:<32}{restaurant[i-1]:<30}{price[i-1]:>8}')
         i += 1
   #Basket and Delivery managemnet system
   ch = input('would you like to add to basket (ok/no):')            
   if ch == 'ok':
         IT = input('Items to add to basket:')
         for item in IT:
            quantity.append([
               Dish[int(item)-1],
               Restaurant[int(item)-1],
               Price[int(item)-1]
              ])
         Total_items = len(quantity)
         print('Your Cart Items:')
         print(f'{'Name':<30}{'Price':<15}')
         for q in quantity:
                        print(f'{q[0]:<35}{q[2]:<15}')
         print('-'*45)
         print('Total Items :',Total_items )
         total_amount = sum(q[2] for q in quantity)
         print('Total Amount to Pay:',total_amount)
         print('*'*15)
   else:
      print('Kindly Visit Food Space')
      

    

   confirm = input('Would you like to proceed for Delivery (yes/no):')
   if confirm == 'yes':
                   pay = input('would you like to pay in COD/online(1/2):')
                   hour = t.tm_hour
                   minute = t.tm_min + 15
                   if minute >= 60:
                       minute = minute - 60
                       hour = hour + 1
                   if pay == '1':
                     print('keep cash of :',total_amount)
                     print('🛵💨'*6,'your food will be deliverd within 15min','🛵💨'*6)
                     print('-'*10)
                     print('Delivery Time:',hour,':',minute,'Pm')
                     
                            
                   elif pay == '2':
                       print('1.phonepe','2.Paytm','3.Gpay','4.BHIM',sep="\n")
                       ask = int(input('choose an UPI app(1/2/3/4):'))
                       app ={1:'phonepe',2:'paytm',3:'Gpay',4:'BHIM'}
                       if ask in app:
                            print('Redirecting to your App:',app[ask])
                            print('🛵'*6,'your food will be deliverd within 15min','🛵'*6)
                            print('-'*15)
                            print('Your food will be delivered on:',hour,':',minute,'Pm')
                            
                   else:
                    print('Invalid selection')
   else:
      print('Exiting from the food space')
      
                     
