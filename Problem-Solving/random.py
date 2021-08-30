
import random 

char_list = ['a','e','i','o','u'] 
random.shuffle(char_list) 
print(''.join(char_list)) 

secret_number = random.randint(1,500)  
print("Pick a number between 1 to 500" )
res = input("Guess the number: ") 
while True:  
    if res==secret_number:  
        print ("You win", secret_number )
        break 
    else:  
        print ("You lose", secret_number )
        break