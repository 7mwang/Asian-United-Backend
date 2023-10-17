import random

def main():
    target_position = random.randint(1, 100)
    print(f"Aim Trainer - Hit the target at position {target_position}")
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if guess == target_position:
                print("Congratulations! You hit the target.")
                break
            else:
                print("Missed. Try again.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
if __name__ == "__main__":
    main()