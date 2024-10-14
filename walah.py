import os
import json
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest

CREDENTIALS_BASE_FOLDER = 'sessions'

# Create base folder for sessions if it doesn't exist
if not os.path.exists(CREDENTIALS_BASE_FOLDER):
    os.mkdir(CREDENTIALS_BASE_FOLDER)

# Function to save credentials in a session-specific folder
def save_credentials(session_name, credentials):
    session_folder = os.path.join(CREDENTIALS_BASE_FOLDER, session_name)
    if not os.path.exists(session_folder):
        os.mkdir(session_folder)  # Create folder for the session if it doesn't exist
    path = os.path.join(session_folder, "credentials.json")
    with open(path, 'w') as f:
        json.dump(credentials, f)

# Function to load credentials from a session-specific folder
def load_credentials(session_name):
    session_folder = os.path.join(CREDENTIALS_BASE_FOLDER, session_name)
    path = os.path.join(session_folder, "credentials.json")
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

# Function to retrieve the last saved message from 'Saved Messages'
async def get_last_saved_message(client):
    saved_messages_peer = await client.get_input_entity('me')
    history = await client(GetHistoryRequest(
        peer=saved_messages_peer,
        limit=1,
        offset_id=0,
        offset_date=None,
        add_offset=0,
        max_id=0,
        min_id=0,
        hash=0
    ))

    if not history.messages:
        print("No messages found in 'Saved Messages'.")
        return None

    return history.messages[0]

# Function to forward the message to all joined groups
async def forward_to_groups(client, last_message):
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            group = dialog.entity
            try:
                await client.forward_messages(group, last_message)
                print(f"Message forwarded to {group.title}")
            except Exception as e:
                print(f"Failed to forward message to {group.title}: {str(e)}")
            await asyncio.sleep(3)  # Small delay between each forward to prevent flooding

# Function to login and perform message forwarding
async def login_and_forward(api_id, api_hash, phone_number, repeat_times, delay):
    session_name = phone_number  # Use phone number as the session name
    session_folder = os.path.join(CREDENTIALS_BASE_FOLDER, session_name)
    client = TelegramClient(session_folder, api_id, api_hash)

    await client.start(phone=phone_number)

    try:
        if await client.is_user_authorized() is False:
            await client.send_code_request(phone_number)
            await client.sign_in(phone_number)
    except SessionPasswordNeededError:
        password = input("Two-factor authentication enabled. Enter your password: ")
        await client.sign_in(password=password)

    last_message = await get_last_saved_message(client)
    if last_message is None:
        return

    for round_num in range(1, repeat_times + 1):
        await forward_to_groups(client, last_message)

        if round_num < repeat_times:
            await asyncio.sleep(delay)

    await client.disconnect()

async def main():
    # Ask how many sessions to log in
    num_sessions = int(input("Enter how many sessions you want to log in: "))

    for i in range(1, num_sessions + 1):
        print(f"\nSession {i}:")
        session_name = f'session{i}'

        # Load credentials if they exist
        credentials = load_credentials(session_name)

        if credentials:
            print(f"Using saved credentials for session {i}.")
            api_id = credentials['api_id']
            api_hash = credentials['api_hash']
            phone_number = credentials['phone_number']
        else:
            api_id = int(input(f"Enter API ID for session {i}: "))
            api_hash = input(f"Enter API hash for session {i}: ")
            phone_number = input(f"Enter phone number for session {i} (with country code): ")

            # Save credentials for future use
            credentials = {
                'api_id': api_id,
                'api_hash': api_hash,
                'phone_number': phone_number
            }
            save_credentials(session_name, credentials)

        # Ask how many times and the delay
        repeat_times = int(input(f"How many times to send the message to all groups for session {i}? "))
        delay = int(input(f"Enter the delay (in seconds) between each round for session {i}: "))

        # Start the login and forwarding process
        await login_and_forward(api_id, api_hash, phone_number, repeat_times, delay)

if __name__ == "__main__":
    asyncio.run(main())