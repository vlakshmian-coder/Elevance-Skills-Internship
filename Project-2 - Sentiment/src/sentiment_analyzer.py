def detect_sentiment(text):
    """Detect whether the text expresses a positive, negative, or neutral sentiment."""

    text = text.lower()

    positive_words = [
        "happy",
        "good",
        "great",
        "excellent",
        "awesome",
        "love",
        "like",
        "thanks",
        "thank you",
        "wonderful",
        "amazing",
        "nice"
    ]

    negative_words = [
        "sad",
        "bad",
        "angry",
        "frustrated",
        "upset",
        "hate",
        "terrible",
        "worst",
        "problem",
        "dislike",
        "don't like",
        "dont like",
        "not good",
        "poor",
        "awful",
        "annoying"
    ]

    # Check negative words first
    for word in negative_words:
        if word in text:
            return "Negative"

    # Then check positive words
    for word in positive_words:
        if word in text:
            return "Positive"

    return "Neutral"