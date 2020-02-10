guess_word = "d3cartel"
guess = ""
guess_count = 0
limit = 3
out_of_guesses = False

print("A guessing Game...You've got 3 guesses")
while guess != guess_word and not(out_of_guesses):
    if guess_count < limit:
        guess = input("Enter your Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("\nYou LOOSE, You are out of Guesses")
else:
    print("\nOMG!! You are a Genius.. You WIN")
        
    
    
    
