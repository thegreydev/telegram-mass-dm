from telethon import TelegramClient
import os

# Telegram API credentials (from my.telegram.org)
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
phone_number = 'YOUR_PHONE_NUMBER'  # Your phone number with country code

# Path to the file that contains the list of users
users_file = 'users.txt'  # File with Telegram usernames or phone numbers

# The message to send
message = "Hello, this is a test message from Python!"

# Create the Telegram client and save session automatically
client = TelegramClient('session_name', api_id, api_hash)

async def send_messages():
    # Connect and log in (if necessary)
    await client.start(phone_number)

    # Ensure the session is saved
    print("Logged in successfully!")

    # Read the list of users from the file
    if os.path.exists(users_file):
        with open(users_file, 'r') as f:
            users = [line.strip() for line in f.readlines()]
    else:
        print(f"Error: {users_file} does not exist.")
        return

    # Loop through each user and send the message
    for user in users:
        try:
            # Send a message to the user
            await client.send_message(user, message)
            print(f"Message sent to {user}")
        except Exception as e:
            print(f"Failed to send message to {user}: {e}")

# Run the async function
with client:
    client.loop.run_until_complete(send_messages())
