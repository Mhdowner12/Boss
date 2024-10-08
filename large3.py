from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError
from getpass import getpass
import time

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'
phone_number = input("ENTER YOUR NUMBER (e.g., +9838383929): ")

# List of channel usernames with '@' prefix
channel_usernames = [
    '@instagramsonly', '@iwannasuicedeopenmarket', '@explosiveness', '@jacesmarket',
    '@makeemoney', '@sfsbuysell', '@legitbuyersndsellers', '@zax_central', '@calypsomarket',
    '@sudanshill', '@aimsmarketplace', '@halfofbrickayeee', '@bertsmarket', '@igbuysellm',
    '@cashappserviceschat', '@oginstagramm', '@surgesocialmarket', '@nyccarder', '@epmarket',
    '@redymarket', '@hypewts', '@officialgoodshitchat', '@discovermarket', '@spprobymrdoui',
    '@saltedstore', '@openmarketcompany', '@shootout_community_chats', '@instagramtrade',
    '@guapforum', '@umbrellamarket', '@thenightmarket', '@pendingsfs', '@chapzzmarketplace',
    '@wysmarketingchat2', '@instawoodi', '@fraud_city', '@legitestmarket', '@talamarkettt',
    '@instagrammarket', '@nuttymarket', '@medusamedussmedusa', '@scams_no_grams', '@flyxmarketx',
    '@moonrocksmarket', '@dreimarket', '@publicfoodhouse', '@demon_support', '@traplinefullzgulag',
    '@spainshill', '@premiumszxcc', '@cyborg_spam', '@blackavenuee', '@cohmedymarket', '@jmopenmarketplace',
    '@tiggerchat', '@teleworldmarket', '@rvelvetmarket', '@premiermarket', '@boliviashill', '@ynwmarket',
    '@tksfs', '@broccoli5k', '@culturemarket', '@themobilemarket', '@powermarketing', '@igmarketchat',
    '@buysellinstaacc', '@xiomarkett', '@pyxismarket', '@theblackmarket', '@lucimarket',
    '@netifypremiumsupplymarket', '@icestory', '@sfsmarket3', '@mathew2344', '@theredmarket',
    '@legitpageadvertising', '@afghanistanshill', '@sarisarimarket', '@fivioopenmarket', '@twittermp',
    '@cardingshgroup', '@mjtrustedmarket', '@popthatpussyptp', '@asclepiusmarket', '@hubofmarkets',
    '@conceiited', '@onepiecemarket', '@multi_tips2', '@szpmarket', '@marketlmfao', '@skyymarket',
    '@chocolatecitys', '@highpayingmarket', '@tays56', '@buyersandsellersgroupp', '@dineathome',
    '@mmacirclejerk', '@lesothoshill', '@platinummarket', '@maroonmarket', '@leafcanada',
    '@bargaining', '@apsellers_01', '@peurtelegram', '@belarusshill', '@moonteamart',
    '@charslamarket', '@thegrandexchange', '@banklords', '@spread4gains', '@mewmewmarket',
    '@marketext', '@crazckers', '@imupfromscamming', '@instagramigig', '@franceeshill',
    '@intocryptoverse', '@cashoutmarket', '@thepugmarket', '@legalehandel', '@indiansellerscrew',
    '@lucifersmarket', '@igaccounts', '@execmarket', '@spamilogy', '@australiashill', '@fsegang',
    '@socialsprint', '@tgmegamart', '@legitcreme', '@moneyworlda', '@bpmarkettt', '@bulksmsspam',
    '@igaccounts4sale', '@igbst'
]

def main():
    client = TelegramClient('session_name', api_id, api_hash)
    
    try:
        client.connect()
        
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            code = input('Enter the code: ')
            try:
                client.sign_in(phone_number, code)
            except SessionPasswordNeededError:
                password = getpass('Enter your 2FA password: ')
                client.sign_in(phone_number, code, password)
        
        for i, channel in enumerate(channel_usernames):
            try:
                client(JoinChannelRequest(channel))
                print(f'Successfully joined {channel}')
            except Exception as e:
                print(f'Failed to join {channel}: {e}')
            
            # Sleep for 7 minutes after joining every 4 channels
            if (i + 1) % 4 == 0:
                print("Sleeping for 7 minutes...")
                time.sleep(7 * 60)

    except PhoneCodeInvalidError:
        print('The code you entered is invalid. Please try again.')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        client.disconnect()

if __name__ == '__main__':
    main()
