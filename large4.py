from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError
from getpass import getpass

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'
phone_number = input("ENTER YOUR NUMBER (e.g., +9838383929): ")

# List of channel usernames with '@' prefix
channel_usernames = [
    '@mythsmarket', '@hammermarketplace', '@radiantsmarket', '@a9xstorex',
    '@moneymarkethunters', '@ycmmarket', '@marketave', '@burundishill',
    '@securemarket', '@thefinalmarket', '@ncxmarketcanada', '@socialmaniaog',
    '@phpa_market', '@paypalogschat', '@windsales', '@phmartpremiums',
    '@cameroonshill', '@austriashill', '@newmarket01', '@kamarket',
    '@bestvendorsontelegram', '@kixpliu', '@exoticmarket', '@chrrymrt',
    '@samsmithopenmarket', '@infiniteplugz', '@titanmarket', '@swapkinggc',
    '@plussssultraaaa', '@plazadeac', '@darksideforum', '@wolf_market20',
    '@monstermarket', '@serbiashill', '@sosanti', '@sfsmarketss',
    '@cherishmarket', '@jamiessfsmarket', '@succletmarket', '@gomark3t',
    '@socialmediamoneys', '@marketsplace', '@worldmarketchat', '@igmarke_t',
    '@cookiesmarttt', '@bestttmarket', '@alpaccinochat', '@purplemarketss',
    '@sfsmarket3', '@tiggerchat', '@gcpromotionph', '@kvsmarket',
    '@sauceworldd', '@steppagainsrfr', '@datatouchmarketplace', '@virgomarketplace',
    '@mercadomarket', '@themobilemarket', '@thedmarket', '@scmarketv2',
    '@businessclubv2', '@bigmarketchat', '@fazeemarket', '@moneymartog',
    '@marketplace_ig', '@lasprimasmercado'
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
                password = getpass('Password: ')
                client.sign_in(phone_number, code, password)
                
        for channel in channel_usernames:
            try:
                client(JoinChannelRequest(channel))
                print(f'Successfully joined {channel}')
            except Exception as e:
                print(f'Failed to join {channel}: {e}')

    except PhoneCodeInvalidError:
        print('The code you entered is invalid. Please try again.')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        client.disconnect()

if __name__ == '__main__':
    main()
