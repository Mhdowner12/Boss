from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import GetAllChatsRequest
from telethon.tl.types import Channel
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init(autoreset=True)

# Function to print your name in large, colored text
def print_colored_name(name):
    large_text = (
        f"{Fore.RED}{Back.BLUE}{Style.BRIGHT}"
        "  _                  _   _____           _           \n"
        " | |                | | |  __ \\         | |          \n"
        " | | ___   ___  _ __| |_| |  | | ___  ___| |_ ___  ___ \n"
        " | |/ _ \\ / _ \\| '__| __| |  | / _ \\/ __| __/ _ \\/ __|\n"
        " | | (_) | (_) | |  | |_| |__| |  __/\\__ \\ ||  __/\\__ \ \n"
        " |_|\\___/ \\___/|_|   \\__|_____/ \\___||___/\\__\\___||___/ \n"
        f"{Style.RESET_ALL}"
    )
    print(large_text)

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'
phone_number = input("ENTER YOUR NUMBER (e.g., +1234567890): ").strip()

# List of channel URLs
channel_urls = [
    "https://t.me/millionairemarket",
    "https://t.me/bhartiya_group_3",
    "https://t.me/sfshubs",
    "https://t.me/oponlinepalengke",
    "https://t.me/socialsmarketplace",
    "https://t.me/sfsgroupjoin",
    "https://t.me/pennymart",
    "https://t.me/simmingtalk",
    "https://t.me/telestoreogchat",
    "https://t.me/datatouchmarketplace",
    "https://t.me/hiltonplugus",
    "https://t.me/nekomart",
    "https://t.me/shayaangc",
    "https://t.me/percmarts",
    "https://t.me/mootsmarket",
    "https://t.me/sevendeadlysinsmarket",
    "https://t.me/freakymega",
    "https://t.me/instagramaccountmarketplace",
    "https://t.me/darktrademarket",
    "https://t.me/lucysmarket",
    "https://t.me/classifiedmarketplace",
    "https://t.me/ubereatsmarket",
    "https://t.me/telemartph",
    "https://t.me/darkfprum",
    "https://t.me/milesmart",
    "https://t.me/twiceujjangmarket",
    "https://t.me/general_business",
    "https://t.me/gainmedia",
    "https://t.me/pietersmarket",
    "https://t.me/billboardmarket",
    "https://t.me/globalfinancenetworkers",
    "https://t.me/summermarket",
    "https://t.me/prospermarket",
    "https://t.me/virgomarketplace",
    "https://t.me/sfsmarket4",
    "https://t.me/sellingpromos",
    "https://t.me/igadminmarket",
    "https://t.me/galaxyzxcv",
    "https://t.me/angelmarkett",
    "https://t.me/batakabmarketsue",
    "https://t.me/heavensmarketplace",
    "https://t.me/allcardingplays",
    "https://t.me/alienxmarket",
    "https://t.me/sfsmarket6",
    "https://t.me/steppagainsrfr",
    "https://t.me/moonairemarket",
    "https://t.me/admitmarket",
    "https://t.me/igsfsmarket",
    "https://t.me/bwallagang",
    "https://t.me/notuck",
    "https://t.me/fraudniggas",
    "https://t.me/impacting",
    "https://t.me/ethiopiashill",
    "https://t.me/marketgoat",
    "https://t.me/gbpremsmarket",
    "https://t.me/medi
