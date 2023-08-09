import time
import requests
import smtplib

# Replace with your own access token
access_token = "YOUR_ACCESS_TOKEN"

# Ask the user for an Instagram username to check
username = input("Enter an Instagram username to check: ")
email_address = input("Enter your email to get an email when someone unfollows you: ")

def send_email(unfollowed_users):
    """Send an email to the user when someone unfollows them."""
    # use gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")
    server.sendmail(
        "YOUR_EMAIL_ADDRESS",
        email_address,
        f"The following users have unfollowed {username}: {', '.join(unfollowed_users)}"
    )
    
# Initialize the list of followers
followers = []




while True:
    # Get the current list of followers
    url = f"https://api.instagram.com/v1/users/{username}/followed-by?access_token={access_token}"
    response = requests.get(url)
    data = response.json()
    current_followers = [follower["username"] for follower in data["data"]]

    # Find the users who have unfollowed
    unfollowed_users = set(followers) - set(current_followers)

    # Update the list of followers
    followers = current_followers

    # Print the list of unfollowed users
    if len(unfollowed_users) > 0:
        print(f"The following users have unfollowed {username}: {', '.join(unfollowed_users)}")
        send_email(unfollowed_users)
    else:
        print(f"No users have unfollowed {username}.")

    # Wait for 10 seconds before checking again
    time.sleep(10)