 tkinter as tk
import random

# Initialize score and random number
score = 0import
computer_number = random.randint(1, 5)

# Function to check the guess a number between 1 and 5.")
            return
    except ValueError:
        result_label.config(text="Please enter a v
def check_guess():
    global score, computer_number

    try:
        user_guess = int(entry.get())
        if user_guess < 1 or user_guess > 5:
            result_label.config(text="Please enteralid number.")
        return

    if user_guess == computer_number:
        result_label.config(text="Afarin 🎉")
        score += 4
    else:
        result_label.config(text=f"Khak to saret 😅 (The number was {computer_number})")
        score -= 1

    score_label.config(text=f"Score: {score}")
    computer_number = random.randint(1, 5)  # Generate a new number for the next round
    entry.delete(0, tk.END)  # Clear input

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game (1–5)")
root.geometry("300x250")
root.config(bg="#fafafa")

# Widgets
title_label = tk.Label(root, text="Guess the number (1–5)", font=("Arial", 14), bg="#fafafa")
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", font=("Arial", 12), command=check_guess, bg="#4CAF50", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#fafafa")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12, "bold"), bg="#fafafa")
score_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
