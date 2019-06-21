print('What is the longest word in the English language?')
print('You have 3 attempts!')
secret_word = "pneumonoultramicroscopicsilicovolcanoconiosis"
guess = ""
i = 0
while guess != secret_word and i <= 2:  # != means not equal
    i = i + 1
    print("Attempt " + str(i))
    guess = input("Enter guess: ")
    if guess == secret_word:
        print("You win!")
    elif guess != secret_word and i <= 2:
        print("Try again")
    else:
        print("Haha! You lose")
