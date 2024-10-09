from scripts.generate_workout import generate_workout
from scripts.track_progress import track_progress
from scripts.motivational_tips import get_motivational_tip

def main():
    user_id = 1
    # Load user profile (for demo purposes)
    with open('data/user_profiles.json', 'r') as file:
        user_profiles = json.load(file)
    user_profile = user_profiles[0]  # Assuming the first user profile

    # Generate workout
    workout = generate_workout(user_profile)
    print("Your personalized workout plan:", workout)

    # Track progress (for demo purposes)
    progress_data = {
        'date': str(datetime.date.today()),
        'workout_completed': True,
        'notes': 'Felt great after the workout!'
    }
    track_progress(user_id, progress_data)

    # Get motivational tip
    tip = get_motivational_tip()
    print("Motivational Tip:", tip)

if __name__ == "__main__":
    main()
