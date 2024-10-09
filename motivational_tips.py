import random

def get_motivational_tip():
    tips = [
        "Keep pushing your limits!",
        "Every step counts!",
        "You’re stronger than you think!",
        "Consistency is key to success!",
        "Believe in yourself and all that you are."
    ]
    return random.choice(tips)

# Example usage
tip = get_motivational_tip()
print("Motivational Tip:", tip)
