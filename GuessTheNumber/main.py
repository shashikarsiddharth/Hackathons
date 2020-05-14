import random


def generate_random():
    random_number = random.randrange(1, 10)
    return random_number


def return_adjective(inp):
    if inp <= 5:
        return "Great! "
    elif inp > 5 and inp <= 10:
        return "Good Job! "
    else:
        return "OMG, finally! "


def check_response():
    chance_taken = 1
    generated_number = generate_random()

    while(True):
        predicted_number = int(input("Enter a number: "))
        if predicted_number == generated_number:
            adjective = return_adjective(chance_taken)
            print(adjective, "You guessed it correctly.")
            print("Chance Taken: {}".format(chance_taken))
            break

        elif predicted_number < generated_number:
            print("Too less, little higher.")
            chance_taken += 1

        else:
            print("Quite high, little lower")
            chance_taken += 1


if __name__ == "__main__":
    print("Welcome to guess the number!")
    check_response()
