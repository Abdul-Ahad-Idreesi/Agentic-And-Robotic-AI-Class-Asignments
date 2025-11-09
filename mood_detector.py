# mood_detector.py

def detect_mood(text):
    """
    Analyzes the input text and determines the mood (Happy, Sad, or Neutral)
    based on keyword matching.
    """
    # Define keywords for different moods
    happy_keywords = ["happy", "joy", "great", "good", "awesome", "fantastic", "love", ":)"]
    sad_keywords = ["sad", "unhappy", "bad", "terrible", "hate", "cry", ":("]
    neutral_keywords = ["ok", "fine", "neutral", "average", "normal"]

    # Initialize mood scores
    happy_score = 0
    sad_score = 0
    neutral_score = 0

    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()

    # Check for happy keywords
    for keyword in happy_keywords:
        if keyword in text_lower:
            happy_score += 1

    # Check for sad keywords
    for keyword in sad_keywords:
        if keyword in text_lower:
            sad_score += 1

    # Check for neutral keywords
    for keyword in neutral_keywords:
        if keyword in text_lower:
            neutral_score += 1

    # Determine the dominant mood
    if happy_score > sad_score and happy_score > neutral_score:
        return "Happy"
    elif sad_score > happy_score and sad_score > neutral_score:
        return "Sad"
    elif neutral_score > happy_score and neutral_score > sad_score:
        return "Neutral"
    elif happy_score == sad_score and happy_score > 0:
        return "Mixed (Happy and Sad)" # Handle cases where both happy and sad keywords are present
    else:
        return "Neutral" # Default to neutral if no strong mood is detected or scores are tied

if __name__ == "__main__":
    print("Welcome to the Mood Detector!")
    user_input = input("Please enter some text to detect your mood: ")

    # Detect the mood
    mood = detect_mood(user_input)

    # Print a friendly message with the detected mood
    print(f"Your mood seems {mood}.")
