#TIP CALCULATOR 1
#level_of_service = ("good", "fair", "bad")

#bill_amount = int(input("Enter total bill amount: "))
#level_of_service = input("Enter level of service (good,fair or bad): ")
#tip_amount = 0.0
#if (level_of_service == "good"):
    #tip_amount = bill_amount * .20
#elif (level_of_service == "fair"):
    #tip_amount = bill_amount * .15
#elif(level_of_service == "bad"):
    #tip_amount = bill_amount * .10
#else:
    #print("Please enter again.")
#total_amount = tip_amount + bill_amount

#print("Tip Amount:$" "%.2f" %  tip_amount)
#print("Total Amount:$ " "%.2f" % total_amount)

#TIP CALCULATOR 2

#level_of_service = ("good", "fair", "bad")

#bill_amount = int(input("Enter total bill amount: "))
#level_of_service = input("Enter level of service (good,fair or bad): ")
#amount_of_people = int(input("Split between how many people? "))
#tip_amount = 0.0
#if (level_of_service == "good"):
 #   tip_amount = bill_amount * .20
#elif (level_of_service == "fair"):
 #   tip_amount = bill_amount * .15
#elif(level_of_service == "bad"):
 #   tip_amount = bill_amount * .10
#else:
 #   print("Please enter again.")
#total_amount = tip_amount + bill_amount
#amount_per_person = total_amount/amount_of_people

#print("Tip Amount:$" "%.2f" %  tip_amount)
#print("Total Amount:$ " "%.2f" % total_amount)
#print("Amount per Person:$ " "%.2f" % amount_per_person)

# HOW MANY COINS?


#print("You have 0 coins.")
#coins = 0
#while True:
 #   answer = input('Do you want another coin? ')
  #  if answer.lower() == 'yes':
   #     coins += 1
    #    print("You have ", coins, " coins.")
    #elif answer.lower() == 'no':
     #   print("Bye.")
      #  break
    #

#PRINT A BOX
#width = int(input("Width? " ))
#height = int(input("Height? "))

#i = 0
#while(i < height):
 #   j = 0
  #  while(j < width):
   #     if(i == 0 or i == height - 1 or j==0 or j == width - 1):
    #        print('*', end = ' ')
     #   else:
      #      print(' ', end = ' ')
       # j += 1
   # i += 1
    #print()    

#PRINT A TRIANGLE

#number_of_rows = int(input("Enter number of rows for triangle: "))
#rows = 0
#while rows < number_of_rows:
 #   space = number_of_rows-rows-1
  #  while space > 0:
   #     print(end=" ")
    #    space = space -1
    #star = rows +1
    #while star > 0:
     #   print("*", end=" ")
      #  star = star -1
    #rows = rows + 1
    #print()

#MULTIPLICATION TABLE

#num_multi = 10
#num = 1
#while num <= num_multi:
 #   i = 1
  #  while i <= num_multi:
   #     answer = num * i
    #    print(num, " * ", i," = ", answer)
     #   i +=1 
    #print("")
    #num += 1    
