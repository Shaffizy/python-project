#i =1
#while i<= 5:
#    print(i)
#    i += 1
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_count += 1
    guess = float(input("Guess Number: "))
    if guess == secret_number:
        print(" Congratulation you won!!!")
        break
else:
    print("You lost")


