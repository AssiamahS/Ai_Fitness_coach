import json
import random

def load_workout_plans():
    with open('data/workout_plans.json', 'r') as file:
        return json.load(file)

def generate_workout(user_profile):
    workout_plans = load_workout_plans()
    user_goals = user_profile['goals']
    personalized_plan = random.choice(workout_plans[user_goals])
    return personalized_plan

# Example usage
with open('data/user_profiles.json', 'r') as file:
    user_profile = json.load(file)[0]  # Assuming the first user profile for demo purposes

workout = generate_workout(user_profile)
print("Your personalized workout plan:", workout)
