# telegram-mass-dm
a tool that sends bulk message to telegram users

developer: https://t.me/pysmart


![FFB92B22-B027-4874-8E30-BBE32A3749E5](https://github.com/user-attachments/assets/e1738869-c48b-4e03-a760-9211d8316493)


# STEPS TO FOLLOW
- Set Up Telegram API Credentials
- You'll need an API ID and API Hash from my.telegram.org.
 
<b>ALSO AVAILABLE FOR TELEGRAM MASS DMs</b>

developer: https://t.me/pysmart

- Go to my.telegram.org.
- Log in with your phone number.
- Click on API development tools.
- Copy your API ID and API Hash.

<b>ALSO AVAILABLE FOR TELEGRAM MASS DMs</b>

developer: https://t.me/pysmart

# How It Works:
- Session Saving: The TelegramClient('session_name', api_id, api_hash) automatically saves the session into a file named session_name.session.
- When you run the script again, it won't ask you to log in if the session is still valid.
- Login: The script starts by logging in using your phone number. If the session is already saved, it skips this step.
- Sending Messages: It reads a file (users.txt) containing usernames or phone numbers and sends a message to each one.

<b>ALSO AVAILABLE FOR TELEGRAM MASS DMs</b>

developer: https://t.me/pysmart

# Notes
Ensure that the users.txt file is in the same directory as the script or provide an absolute path.
For sending messages to phone numbers, ensure they are in your Telegram contacts. 
