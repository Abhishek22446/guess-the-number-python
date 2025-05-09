import random 

print("Hi welcome to the random number guessing game.\n You got 6 chances to guess the number. \n Let's start the game")


number_to_guess = random.randrange(50)


#giving a number of chances to identify the num to guess

chances = 6

#initially the counter value is zero when game start's

guess_counter = 0

#while is used to repeat the guess counter


while guess_counter < chances :
    
    
 #guess_counter is increased when the num is lesser than chances(6)
    
    guess_counter += 1
    
    my_guess = int(input("Please enter your Guessing number : "))
    
    
    if my_guess < 0 or my_guess >= 50:
        print("Entered number is out of range! Please enter a number between 0 and 49.")
        guess_counter -= 1  # Undo the increment to not waste a chance
        continue  # Skip rest of the loop

    
    
    if my_guess == number_to_guess :
        
        print(f'The Number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
        
      #stopping the game when the guess number is equal to num to guess
        
        break
    
    
    
    elif guess_counter >= chances and my_guess != number_to_guess :
        print(f' Oops sorry,the number is {number_to_guess} better luck next time ')
        
    elif my_guess > number_to_guess :
        print("your guess is higher ")
        
    elif my_guess <  number_to_guess :
        print("your guess is lower ")