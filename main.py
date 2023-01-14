import tweepy
import time

def replyMsg(msg, id):
    print(id)
    if '1' in msg:
        api.update_status(("Starting Game @{}").format(mention.author.screen_name), in_reply_to_status_id=id)
    elif '2' in msg:
        api.update_status(("Checking record @{}").format(mention.author.screen_name), in_reply_to_status_id=id)
    elif '3' in msg:
        api.update_status(("Github @{}").format(mention.author.screen_name), in_reply_to_status_id=id)
    elif '4' in msg:
        api.update_status(("Help @{}").format(mention.author.screen_name), in_reply_to_status_id=id)
    else:
        print('fuck')

all_keys = open('twitterkeys', 'r').read().splitlines()                 # Opens the key document so that they can be transferred into variables

api_key = all_keys[0]                                                   # Sets the api key from the twitter account to a variable that we can use
api_key_secret = all_keys[1]                                            # Sets the api secret key from the twitter account to a variable that we can use    
access_token = all_keys[2]                                              # Sets the access token from the twitter account to a variable that we can use
access_token_secret = all_keys[3]                                       # Sets the access token secret from the twitter account to a variable we can use

authenticator = tweepy.OAuth1UserHandler(api_key, api_key_secret)       # Autehenticates keys and allows access into the account
authenticator.set_access_token(access_token, access_token_secret)       # Autehenticates keys and allows access into the account

api = tweepy.API(authenticator, wait_on_rate_limit=True)                # Sets an API variable that can be used for any following script

bot_id = int(api.verify_credentials().id_str)
mention_id = 1
user_cmds = ["1", "2", "3", "4"]

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        mention_id = mention_id
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if True in [word in mention.text.lower() for word in user_cmds]:
                try:
                    print(mention.text.lower())
                    #api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    replyMsg(mention.text, mention.id_str)
                except Exception as exc:
                    print(exc)

    
    time.sleep(10)



        
