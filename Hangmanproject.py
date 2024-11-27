import random
import re

def Hangman():
    print("Welcome to Hangman!,though this ain't your typical hangman but pls do keep an open mind.")
    print("You are to guess the correct word based on hints being dropped, you have three attempts at each word")
    print("for each attempt a different hint would be given but it is still referring to the same word you are at.")
    print("This was done so you can know more than one interesting fact on certain things, making it both fun and knowledgeable.")
    print("Also, Do note that after three attempts at a word you must re-run the code so you can start the game again with a different word.")
    print("Hope you enjoy it!!!, Let's Get Started!")

    # Define the words and their hints
    hints_dict = {
        "Turkey": ["A six-letter word for a domestic bird.",
                   "The country is located between Europe and Asia.",
                   "The name of a bird that's also the name of a country."],
                   
        "Nile": ["A four-letter word for a river.",
                 "The longest river in Africa.",
                 "This river is regarded as the wealth of Egypt."],
        "Canada": ["A six-letter word for a country.",
                   "Known for its maple syrup and winters.Hence nicknamed the Maple Country",
                   "Located in North America plus one-tenth of the world's forest are there."],
        "Cheetah": ["A seven-letter word for a wild animal.",
                    "The fastest land animal.",
                    "It’s spotted and found in the savannah."],
        "Eagle":["A five-letter word for a very mighty bird.",
                 "Somehow regarded as the king of all birds because it is used as a symbol of strength in many countries.",
                 "Known for it's excellent and sharp vision"],
         "Ostrich":["A seven-letter word for a big bird",
                    "The heaviest bird in the word",
                    "it has a long neck and long strong legs"],
         "Archaeopteryx":["A thirthteen-letter word for an ancient bird",
                          "Known as the world's first bird",
                          "A Genus of Feathered Dinosaurs"]

    }

    # Randomly select a word and its hints
    randomword = random.choice(list(hints_dict.keys()))
    hints = hints_dict[randomword]

    # Hide the word
    hideword = re.sub(r'\w', '_', randomword)
    print(f"The word: {hideword}")

    # Allow up to 3 attempts
    for attempt in range(3):
        print(hints[attempt])  # Display the current hint
        guess = input("Enter your guess: ")

        if guess.lower() == randomword.lower():
            print("Congratulations! You guessed the correct word!")
            return
        else:
            print("Incorrect. Try again.")

    # If the user fails all attempts
    print(f"Game Over! The correct word was: {randomword}")

# Call the game
Hangman()



 