Spam Email Automation

A Python-based REST API that automatically analyzes email content and classifies it as Spam or Not Spam.

Objective

The objective of this project is to automate basic spam email detection without using any external email API.

Features

- Detects suspicious email content
- Checks common spam keywords
- Detects links in emails
- Generates a spam score
- Classifies emails as SPAM or NOT SPAM
- Provides an automatic action
- REST API based implementation

Technologies Used

- Python
- Flask
- REST API
- Regular Expressions

How It Works

Email
↓
REST API
↓
Spam Detection
↓
Spam Score
↓
SPAM / NOT SPAM
↓
Automatic Action

API Endpoint

POST "/check-email"

Example Input

{
    "email": "Congratulations! You won a lottery prize. Claim now!"
}

Example Output

{
    "status": "SPAM",
    "spam_score": 100,
    "matched_keywords": [
        "winner",
        "won",
        "lottery",
        "prize",
        "claim now"
    ],
    "links_found": 0,
    "action": "Moved to Spam"
}

Normal Email Example

Input

Hello sir, I am submitting my assignment. Please review it when you have time. Thank you.

Result

Status: NOT SPAM
Action: Kept in Inbox

Project Structure

Spam_Email_Automation/
│
├── app.py
├── spam_detector.py
├── requirements.txt
└── README.md

How to Run

1. Install Dependencies

pip install -r requirements.txt

2. Run the Application

python app.py

3. Open in Browser

http://127.0.0.1:5000

API Usage

Send a POST request to:

http://127.0.0.1:5000/check-email

Example request:

{
    "email": "Congratulations! You won a lottery prize. Claim now!"
}

The API returns the spam status, spam score, detected keywords, number of links, and recommended action.

Future Improvements

- Machine Learning based spam classification
- Email database integration
- Gmail/Outlook integration
- Web-based user interface
- Improved spam detection accuracy
- Automatic email movement to Spam or Inbox