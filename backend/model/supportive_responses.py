"""
supportive_responses.py
-----------------------
Generates supportive, non-judgmental responses based on a detected emotion label.
Emotions supported: sad, anxious, stressed, neutral, happy

Usage:
    python supportive_responses.py
"""

import random

# ---------------------------------------------------------------------------
# Response templates
# Each emotion has 3–5 short, validating variations.
# ---------------------------------------------------------------------------
_RESPONSES: dict[str, list[str]] = {
    "sad": [
        "It's okay to feel sad sometimes — your feelings are completely valid. Be gentle with yourself today.",
        "Feeling sad is a natural part of being human. Take things one small moment at a time.",
        "It's alright to not be okay. Allow yourself to feel this, and know that it won't last forever.",
        "Sadness can be heavy, but you don't have to carry it alone. Reach out to someone you trust when you're ready.",
        "It's okay to feel sad — give yourself permission to rest and recover at your own pace.",
    ],
    "anxious": [
        "It's okay to feel anxious. Try taking a slow, deep breath — you're safe in this moment.",
        "Feeling anxious is your mind trying to protect you. Acknowledge it, then gently bring your focus to what's in front of you right now.",
        "Anxiety can feel overwhelming, but it does pass. Take it one small step at a time.",
        "It's completely understandable to feel anxious. You're doing better than you think.",
        "Feeling anxious is valid. Ground yourself by noticing five things around you — small details can help bring calm.",
    ],
    "stressed": [
        "It's okay to feel stressed — take small steps today, and remember that every little effort counts.",
        "Stress is a sign you care, but you don't have to tackle everything at once. Prioritize one thing at a time.",
        "Feeling stressed is completely normal. Give yourself a short break — even a few minutes can help reset your mind.",
        "It's okay to feel this pressure. You've handled hard days before, and you can handle this one too.",
        "Stress is tough, but you're tougher. Be kind to yourself and take it moment by moment.",
    ],
    "neutral": [
        "It's perfectly fine to feel neutral — not every moment needs to be intense. Enjoy the calm.",
        "A neutral day is still a good day. Sometimes steadiness is exactly what we need.",
        "Feeling balanced and steady is something to appreciate. Take a moment to simply be.",
        "It's okay to just be. Not every day has to be extraordinary — quiet moments have value too.",
    ],
    "happy": [
        "It's wonderful that you're feeling happy! Hold onto this feeling and let it carry you forward.",
        "Happiness suits you! Take a moment to really appreciate what's bringing you joy right now.",
        "Feeling happy is something to celebrate, even in small ways. Keep nurturing what lifts you up.",
        "That's great to hear! Joy is worth savoring — share it with someone you care about if you can.",
        "Feeling happy is a gift. Notice what's contributing to it so you can come back to it when you need a boost.",
    ],
}

_SUPPORTED_EMOTIONS = set(_RESPONSES.keys())


def get_supportive_response(emotion: str) -> str:
    """
    Return a random supportive, non-judgmental response for the given emotion.

    Parameters
    ----------
    emotion : str
        One of 'sad', 'anxious', 'stressed', 'neutral', 'happy'.
        Case-insensitive. Falls back to a neutral response for unknown labels.

    Returns
    -------
    str
        A supportive response string.
    """
    normalized = emotion.strip().lower()

    if normalized not in _SUPPORTED_EMOTIONS:
        # Graceful fallback for unexpected emotion labels
        return (
            f"Whatever you're feeling right now, it's valid. "
            f"Take a moment to check in with yourself and be kind to yourself today."
        )

    return random.choice(_RESPONSES[normalized])


# ---------------------------------------------------------------------------
# Quick terminal test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    sample_emotions = ["sad", "anxious", "stressed", "neutral", "happy", "unknown"]

    print("=" * 55)
    print("  Supportive Response Component — Sample Outputs")
    print("=" * 55)

    for emo in sample_emotions:
        response = get_supportive_response(emo)
        print(f"\nEmotion : {emo!r}")
        print(f"Response: {response}")

    print("\n" + "=" * 55)
