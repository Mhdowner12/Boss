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
    "https://t.me/mediasalez",
    "https://t.me/olympusmarket",
    "https://t.me/narutomarketph",
    "https://t.me/surgemarket",
    "https://t.me/stopnshoppe",
    "https://t.me/multitips3",
    "https://t.me/catmarketzxc",
    "https://t.me/solastamarketplace",
    "https://t.me/useru",
    "https://t.me/maldivesshill",
    "https://t.me/socialmediamoneys",
    "https://t.me/alphamkt",
    "https://t.me/ogmarts",
    "https://t.me/theelfantasma",
    "https://t.me/sfsmarketing",
    "https://t.me/palengkemarket",
    "https://t.me/myheroacademiamarket",
    "https://t.me/bebemarket",
    "https://t.me/drugkoden",
    "https://t.me/criticalmarket",
    "https://t.me/eruditemart",
    "https://t.me/boming1",
    "https://t.me/bigmarketchat",
    "https://t.me/tmbusinesssocialmediasellgroup",
    "https://t.me/topmarts",
    "https://t.me/bins5",
    "https://t.me/djiboutishill",
    "https://t.me/aurelemarket",
    "https://t.me/radiantsmarket2",
    "https://t.me/igmarketgroup",
    "https://t.me/instamarket08",
    "https://t.me/mythologymarket",
    "https://t.me/apocmarket",
    "https://t.me/paradisomarket",
    "https://t.me/newsvc",
    "https://t.me/spacexgroup17",
    "https://t.me/zizhq",
    "https://t.me/sfsmarketchat",
    "https://t.me/richhelppooronly",
    "https://t.me/blacklagoonmarket",
    "https://t.me/ydopenmarket",
    "https://t.me/gomark3t",
    "https://t.me/aomarket",
    "https://t.me/beaversmarketplace",
    "https://t.me/dreadwts",
    "https://t.me/indiansellerscrew3",
    "https://t.me/marketbosss",
    "https://t.me/spyrorip",
    "https://t.me/sntads",
    "https://t.me/theboysmarketplace",
    "https://t.me/atomicmarketplace",
    "https://t.me/cynmarket",
    "https://t.me/indiashill",
    "https://t.me/swiper_goddd",
    "https://t.me/japannshill",
    "https://t.me/deluxy45",
    "https://t.me/paxchat",
    "https://t.me/validcreditcredit550",
    "https://t.me/papamarkett",
    "https://t.me/legitweb0",
    "https://t.me/thailandshill",
    "https://t.me/versacemarket",
    "https://t.me/socialmarketplace2021",
    "https://t.me/denmarkshill",
    "https://t.me/plugsmart",
    "https://t.me/alienhacking",
    "https://t.me/marketsfs",
    "https://t.me/boostmarket",
    "https://t.me/fraudway",
    "https://t.me/majestuosmarket",
    "https://t.me/serpentmarkett",
    "https://t.me/lebanonshill",
    "https://t.me/shop_usernames",
    "https://t.me/rebelmarket",
    "https://t.me/natesopenmarket",
    "https://t.me/goblinmarkett",
    "https://t.me/netherlandsshill",
    "https://t.me/noybemarket",
    "https://t.me/cockmp",
    "https://t.me/indiansellerscrew2",
    "https://t.me/darkweblord7",
    "https://t.me/telehub2",
    "https://t.me/choppersgg",
    "https://t.me/bangladeshshill",
    "https://t.me/phbuyandsell",
    "https://t.me/royalmarkets",
    "https://t.me/tiggersopenmarket"
]

# Extract channel usernames from URLs
channel_usernames = [url.split('/')[-1] for url in channel_urls]

def main():
    #
