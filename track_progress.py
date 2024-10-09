import json
import datetime

def track_progress(user_id, progress_data):
    with open('data/user_profiles.json', 'r') as file:
        user_profiles = json.load(file)

    for user in user_profiles:
        if user['id'] == user_id:
            user['progress'].append(progress_data)
            break

    with open('data/user_profiles.json', 'w') as file:
        json.dump(user_profiles, file)

# Example usage
progress_data = {
    'date': str(datetime.date.today()),
    'workout_completed': True,
    'notes': 'Felt great after the workout!'
}
track_progress(user_id=1, progress_data=progress_data)
