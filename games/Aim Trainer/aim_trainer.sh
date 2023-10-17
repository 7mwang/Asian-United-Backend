#!/bin/bash

# Linux Shell (Bash) Part
echo "Welcome to the Moving Target Aim Trainer!"
read -p "Press Enter to start..."

# Initialize the target position
target_position=$((1 + RANDOM % 100))

# Function to display the target area
function display_target {
    clear  # Clear the terminal screen
    echo "Moving Target Aim Trainer - Hit the target area between 1 and 100"
    echo ""

    # Display the target area as a horizontal line
    target_line=""
    for ((i = 1; i <= 100; i++)); do
        if [[ $i -eq $target_position ]]; then
            target_line+="X"
        else
            target_line+="-"
        fi
    done

    echo "$target_line"
    echo ""
}

# Function to check if the guess is correct
function check_guess {
    read -p "Enter your guess (1-100): " guess
    if [[ $guess -eq $target_position ]]; then
        echo "Congratulations! You hit the target at position $target_position."
    else
        echo "Missed. The target was at position $target_position."
    fi
}

# Loop to play the game
while true; do
    display_target
    check_guess

    # Move the target to a new random position
    target_position=$((1 + RANDOM % 100))
    
    read -p "Press Enter to shoot again or 'q' to quit: " choice
    if [[ $choice == "q" ]]; then
        break
    fi
done