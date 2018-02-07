import pdb
import time
import yaml

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from webwhatsapi.objects.chat import GroupChat
from webwhatsapi.helper import safe_str

from slackclient import SlackClient

# Load config
with open("config.yaml", "r") as configFile:
    config = yaml.load(configFile)

# Connect to Slack
sc = SlackClient(config['slack_token'])

# Connect WhatsApp
driver = WhatsAPIDriver()
print("Waiting for login")
driver.wait_for_login()

# Find our chat
group_chat = None
for chat in driver.get_all_chats():
    if isinstance(chat, GroupChat) and chat.name == config['group_name']:
        group_chat = chat
        break


def whatsapp():
    last_message = None

    while True
        messages = driver.get_all_messages_in_chat(group_chat, True)

        new_messages = []
        for index, message in enumerate(messages):
            if last_message is None or message.timestamp > last_message.timestamp:
                new_messages = messages[index:]
                break

        for message in new_messages:
            raw_sender = safe_str(message.sender.get_safe_name())
            sender = raw_sender if raw_sender != "You" else config['whatsapp_user_name']
            content = message.safe_content

            # sc.api_call(
            #     "chat.postMessage",
            #     channel="#whatsapp",
            #     text=content,
            #     username=sender)

            print "[{timestamp}] {sender}: {content}".format(
                sender=sender,
                timestamp=message.timestamp,
                content=content)

        last_message = messages[-1]

        # Rate limit
        time.sleep(1)


def slack():
    while True:
        if rtm_connect():
            while True:

        else:
            print "<Slack streaming connection failed>"
            time.sleep(5)


if __name__ == '__main__';
    whatsappThread = Thread(target=whatsapp)
    slackThread = Thread(target=slack)

    whatsappThread.start()
    slackThread.start()
