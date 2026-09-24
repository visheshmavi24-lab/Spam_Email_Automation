import re

SPAM_KEYWORDS = [
    "winner",
    "won",
    "lottery",
    "prize",
    "free money",
    "claim now",
    "click here",
    "urgent",
    "congratulations",
    "cash prize",
    "limited offer",
    "verify your account"
]


def detect_spam(email_text):
    text = email_text.lower()

    matched_keywords = []

    for keyword in SPAM_KEYWORDS:
        if keyword in text:
            matched_keywords.append(keyword)

    links = re.findall(r"https?://\S+", text)

    spam_score = len(matched_keywords) * 20

    if links:
        spam_score += 10

    spam_score = min(spam_score, 100)

    if spam_score >= 40:
        status = "SPAM"
        action = "Moved to Spam"
    else:
        status = "NOT SPAM"
        action = "Kept in Inbox"

    return {
        "status": status,
        "spam_score": spam_score,
        "matched_keywords": matched_keywords,
        "links_found": len(links),
        "action": action
    }