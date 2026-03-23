import re

stop_words = {
    "the",
    "is",
    "of",
    "for",
    "me",
    "show",
    "last",
    "two",
    "a",
    "an",
    "and",
    "to",
}


def normalize(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text


def tokenize(text):
    patterns = [
        ("ROLL_NO", r"\b\d{2}[a-z]{3}\d{3}\b"),
        ("YEAR", r"\b(19|20)\d{2}\b"),
        ("COURSE_CODE", r"\b[a-z]{2,5}\d{2,4}\b"),
        ("NUMBER", r"\b\d+\b"),
        ("WORD", r"\b[a-z]+\b"),
        ("EMOJI", r"[^\w\s,]"),
    ]

    tokens = []

    for token_type, pattern in patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            value = match.group()
            if token_type == "WORD" and value in stop_words:
                continue
            tokens.append((token_type, value))

    return tokens


query = "Show me the marks of 23DCE081 for the last two internal exams 😊"

query = normalize(query)

tokens = tokenize(query)

for t in tokens:
    print(t)
