# Question 2 - Student Test Score Average Calculator
# ====================================================

def get_score(prompt):
    """Function to get a valid score between 0 and 100"""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Accept three scores from user
score1 = get_score("Enter score 1: ")
score2 = get_score("Enter score 2: ")
score3 = get_score("Enter score 3: ")

# Calculate average
average = (score1 + score2 + score3) / 3

# Display all results
print("\n--- Results ---")
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}")
print(f"Average Score: {average:.2f}")
