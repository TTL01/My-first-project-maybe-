import random 


try:
 d= int(input(" Enter your choice \n 1. random.randint() \n 2. random.random() :  "))
 

 b = random.random()
 i= random.randint(0,1)
 if d == 1:
  user = input (" Enter your Guess (Heads or Tails): ").lower ()
  if i >= 1 :
    result = "heads"
  elif i == 0 :
    result = "tails"
  if user == result :
     print(" Congratulations Honeeey U guess is correct u do it finally , Your words are consistent with what you said.")
  elif user != result :
    print(f" sryy , get tf out negga \n the results is : {result}\n")
   
  else :
   print(" Enter FK letters")
   
 if d == 2 :
    user = input (" Enter your Guess (Heads or Tails): ").lower ()
    
    if b >= 0.50 :
      result = "heads"
    else :
       result = "tails"
    if user == result :
       print(" Congratulations Honeeey U guess is correct u do it finally.")
    elif user != result :
       print(f" sryy , get tf out negga \n the results is : {result}\n")
   
    else :
      print(" Enter FK letters")

except :
  print("Enter fk number")
print("\n I willl kill U")

 
 
   