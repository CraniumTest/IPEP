def create_personalized_plan(athlete_data):
    # Example logic to create a personalized training plan
    # This can be expanded to incorporate machine learning or rule-based logic
    if athlete_data['agility'] < 50:
        return "Focus on agility training."
    return "Balance training across all areas."

if __name__ == '__main__':
    sample_data = {'agility': 45}
    plan = create_personalized_plan(sample_data)
    print('Training Plan:', plan)
