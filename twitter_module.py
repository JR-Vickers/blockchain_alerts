import tweepy

def authenticate_to_twitter(api_key, api_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        return api
    except:
        return None

def format_tweet(entity, wallet_address, transaction_amount_usd, transaction_amount_native):
    wallet_prefix = wallet_address[:3]
    link_to_loch = f"https://app.loch.one/{wallet_address}"
    tweet = f"{entity} {wallet_prefix}... transferred ${transaction_amount_usd} ({transaction_amount_native} native). Details: {link_to_loch}"
    return tweet
