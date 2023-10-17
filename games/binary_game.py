import random

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def binary_to_decimal(binary):
    return int(binary, 2)

def play_binary_game():
    score = 0
    for _ in range(10):  # You can adjust the number of rounds
        decimal = random.randint(1, 255)  # Generate a random decimal number between 1 and 255
        binary = decimal_to_binary(decimal)

        print(f"Decimal: {decimal}")
        user_input = input("Enter the binary representation: ")

        if user_input == binary:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {binary}")

    print(f"Game over! Your score: {score}/10")

if __name__ == "__main__":
    print("Welcome to the Binary Conversion Game!")
    print("Try to convert the given decimal numbers to binary.")
    print("You will have 10 rounds. Let's start!\n")
    
    play_binary_game()
