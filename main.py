# Fetch latest cryptocurrency news from CoinGecko API                
def get_crypto_news():
    url = "https://api.coingecko.com/api/v3/status_updates"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'status_updates' in data and data['status_updates']:
            latest_news = data['status_updates'][0]['description']
            return latest_news[:270]  # Limit to Twitter character count
    return None

# Auto-tweet function
def auto_tweet():
    random_choice = random.random()
    if random_choice < 0.4:  # 40% chance to tweet news
        tweet = get_crypto_news()
        if tweet:
            api.update_status(f"📰 Crypto Update: {tweet}")
            print(f"Tweeted News: {tweet}")
        else:
            tweet = random.choice(educational_tweets)
            api.update_status(tweet)
            print(f"Tweeted: {tweet}")
    elif random_choice < 0.7:  # 30% chance to tweet educational content
        tweet = random.choice(educational_tweets)
        api.update_status(tweet)
        print(f"Tweeted: {tweet}")
    else:  # 30% chance to tweet referral link
        tweet = random.choice(referral_tweets)
        api.update_status(tweet)
        print(f"Tweeted Referral: {tweet}")

    # Auto-reply function (engaging with viral tweets)                    
    def auto_reply():
        search_keywords = ["Bitcoin", "Crypto", "Ethereum", "Altcoins", "Trading"]
        for keyword in search_keywords:
            try:
                tweets = api.search_tweets(q=keyword, count=5, lang="en")
                if tweets: # Check if tweets is not empty
                    for tweet in tweets:
                        try:
                            reply_text = f"Great insights! Also, check this out: [https://bit.ly/4kUQRqh]"
                            api.update_status(f"@{tweet.user.screen_name} {reply_text}", in_reply_to_status_id=tweet.id)
                            print(f"Replied to {tweet.user.screen_name}: {reply_text}")
                            time.sleep(15)  # Avoid spamming
                        except tweepy.TweepyException as e:
                            print(f"Error replying to {tweet.user.screen_name}: {e}")
            except tweepy.TweepyException as e:
                print(f"Error searching for tweets: {e}")

        # Run bot continuously
        while True:
            auto_tweet()
            auto_reply()
        time.sleep(300)  # Wait 2 hour before next round
