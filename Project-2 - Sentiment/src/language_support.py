"""
Language support module for Dynamic AIRA.
Handles language detection and translation.
"""

from deep_translator import GoogleTranslator


def detect_language(text):
    """
    Detect whether the text is English or Hindi.
    """

    for character in text:
        if "\u0900" <= character <= "\u097F":
            return "hi"

    return "en"


def translate_to_english(text):
    """
    Translate Hindi to English.
    English text is returned unchanged.
    """

    language = detect_language(text)

    if language == "en":
        return text

    return GoogleTranslator(source="auto", target="en").translate(text)


def translate_from_english(text, target_language):
    """
    Translate English response back to user's language.
    """

    if target_language == "en":
        return text

    return GoogleTranslator(
        source="en",
        target=target_language
    ).translate(text)