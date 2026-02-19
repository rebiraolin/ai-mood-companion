"""
Emotion Classification Module
Classifies text into one of five emotions: sad, anxious, stressed, neutral, happy.
Uses TF-IDF vectorization + Logistic Regression via a scikit-learn Pipeline.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# ---------------------------------------------------------------------------
# Training data – small but realistic examples for each emotion
# ---------------------------------------------------------------------------
TRAINING_DATA = [
    # sad
    ("I feel so empty and alone today", "sad"),
    ("Nothing seems to matter anymore", "sad"),
    ("I can't stop crying over what happened", "sad"),
    ("I miss the people who are no longer in my life", "sad"),
    ("Everything feels hopeless and dark", "sad"),
    ("I feel like nobody cares about me", "sad"),
    ("I lost someone very close to me and it hurts deeply", "sad"),
    ("I keep thinking about the past and it makes me feel terrible", "sad"),
    ("There is a heavy weight on my chest that won't go away", "sad"),
    ("I feel broken inside and don't know how to fix it", "sad"),

    # anxious
    ("I keep worrying about things that haven't happened yet", "anxious"),
    ("My heart is racing and I can't calm down", "anxious"),
    ("I have a big presentation tomorrow and I feel terrified", "anxious"),
    ("What if something bad happens to my family", "anxious"),
    ("I feel like something terrible is about to happen", "anxious"),
    ("I can't sleep because my mind keeps racing with worries", "anxious"),
    ("I get panic attacks in crowded places", "anxious"),
    ("I feel restless and on edge all the time", "anxious"),
    ("I am afraid of making mistakes at work", "anxious"),
    ("The uncertainty of the future scares me so much", "anxious"),

    # stressed
    ("I have too much work and too little time", "stressed"),
    ("The pressure at my job is overwhelming", "stressed"),
    ("I am juggling so many responsibilities right now", "stressed"),
    ("I feel burned out and completely exhausted", "stressed"),
    ("There are so many deadlines and I can't keep up", "stressed"),
    ("My workload is crushing me and I can't breathe", "stressed"),
    ("I feel like I am being pulled in a hundred directions", "stressed"),
    ("I haven't had a break in weeks and I am running on empty", "stressed"),
    ("Everything is piling up and I don't know where to start", "stressed"),
    ("The demands on my time are more than I can handle", "stressed"),

    # neutral
    ("I went to the store to pick up some groceries", "neutral"),
    ("The weather is cloudy today with a chance of rain", "neutral"),
    ("I had a normal day at work, nothing special", "neutral"),
    ("I am reading a book about history", "neutral"),
    ("I cooked dinner and watched some television", "neutral"),
    ("I took the bus to the office this morning", "neutral"),
    ("I have a meeting scheduled for three o'clock", "neutral"),
    ("I need to do laundry later today", "neutral"),
    ("I finished my homework and submitted it on time", "neutral"),
    ("The new software update was installed on my computer", "neutral"),

    # happy
    ("I got promoted at work and I am thrilled", "happy"),
    ("Today was such a wonderful day with my friends", "happy"),
    ("I feel grateful for everything I have in my life", "happy"),
    ("I just received amazing news and I can't stop smiling", "happy"),
    ("Spending time with my family always makes me feel great", "happy"),
    ("I accomplished my goal and I am so proud of myself", "happy"),
    ("I feel full of energy and excitement about the future", "happy"),
    ("Everything is going so well right now, I feel blessed", "happy"),
    ("I laughed so much today, it was the best day ever", "happy"),
    ("I am in love and it feels absolutely wonderful", "happy"),
]

# ---------------------------------------------------------------------------
# Build and train the pipeline
# ---------------------------------------------------------------------------
texts, labels = zip(*TRAINING_DATA)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        stop_words="english",
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        solver="lbfgs",
        C=1.0,
    )),
])

pipeline.fit(list(texts), list(labels))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def predict_emotion(text: str) -> str:
    """Classify a single text string into an emotion category.

    Args:
        text: The input text to classify.

    Returns:
        One of 'sad', 'anxious', 'stressed', 'neutral', or 'happy'.
    """
    return pipeline.predict([text])[0]


# ---------------------------------------------------------------------------
# Interactive testing
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("  Emotion Classifier  –  type 'quit' to exit")
    print("  Emotions: sad | anxious | stressed | neutral | happy")
    print("=" * 60)

    while True:
        user_input = input("\nEnter text: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not user_input:
            continue
        emotion = predict_emotion(user_input)
        print(f"  → Predicted emotion: {emotion}")
