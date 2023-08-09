# Instagram Unfollower Tracker

This Python script uses the Instagram API to track who unfollows an Instagram user and sends an email notification to the user when someone unfollows them. The script prompts the user to enter an Instagram username to track and an email address to receive notifications. The script then retrieves the list of followers for the user every 10 seconds and compares it to the previous list of followers to find out who has unfollowed them. If someone has unfollowed the user, the script sends an email notification to the user with the list of unfollowed users. This project can be useful for Instagram users who want to keep track of their followers and engagement on the platform.

## Requirements

- Python 3.x
- `requests` library
- `smtplib` library

## Installation

1. Clone the repository or download the `main.py` file.
2. Install the `requests` and `smtplib` libraries using pip: `pip install requests smtplib`.
3. Replace `YOUR_ACCESS_TOKEN`, `YOUR_EMAIL_ADDRESS`, and `YOUR_PASSWORD` with your own access token, email address, and password in the `main.py` file.
4. Run the script using the command `python main.py`.

## Usage

1. Enter an Instagram username to track when prompted.
2. Enter an email address to receive notifications when someone unfollows the user.
3. The script will start tracking the user's followers and send an email notification when someone unfollows them.
