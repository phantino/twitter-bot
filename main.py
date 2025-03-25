import tweepy
import time
import random
import requests

# Twitter API credentials
API_KEY = "me1Lh9XGEInlojf6VI3T6NE3G"
API_SECRET = "D1lYFKBgAcwAuNRQjtdToHb7gGbDngYZWUlZHYW1BO3Ik3zJZH"
ACCESS_TOKEN = "1318929592938385410-dkk3UgKgPWH8uPyGzOTYiADAQ1YvD8"
ACCESS_SECRET = "AgQVovE4Xb7fLuhUtFgeWrERyIC1MRYaRQKv1RrXo96mS"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Send a test tweet
try:
    api.update_status("🚀 Twitter bot test from Railway!")
    print("✅ Tweet sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")

# Educational and market insights tweets
educational_tweets = [
    "💡 Trading Tip: Always use stop-loss to protect your capital! #CryptoTrading",
    "📊 Fundamental vs Technical Analysis: Which one do you use? Both matter! #Investing",
    "🚀 The best traders focus on risk management, not just profits. #TradingMindset",
    "🧠 Did you know? 90% of traders lose money because they trade on emotions. Stay disciplined!",
    "Want to earn from crypto? Copy trade on Bybit: [https://bit.ly/4kUQRqh]",
    "📈 Bitcoin halving reduces supply, making BTC scarcer. Next halving: 2024. Are you ready?",
    "🔥 DeFi is changing finance! Yield farming, staking, and lending are the future. #DeFi",
    "🔍 Always check liquidity before buying new tokens! Avoid rug pulls. #CryptoSafety",
    "📉 Overtrading kills portfolios! Stick to your strategy and avoid revenge trading. #TradingTips",
    "🔹 Diversification is key! Never put all your money into one coin. #CryptoInvesting",
    "📌 Learn candlestick patterns! They reveal market sentiment and trend reversals. #CryptoCharts",
    "💰 Passive income ideas: Staking, yield farming, and lending crypto assets. #DeFiEarnings",
    "📊 RSI below 30 = Oversold (buy signal), above 70 = Overbought (sell signal). Use wisely!",
    "🚨 Stop chasing pumps! If it's already up 100%, you're likely late. #CryptoTrading",
    "🧐 Always check a project's whitepaper before investing. Research is key! #DYOR",
    "💹 Market cap matters! A $1 coin and a $10,000 coin can have the same market cap. #Crypto101",
    "📉 Bear markets create opportunities! Smart investors accumulate, not panic. #HODL",
    "⚡ Leverage trading = High rewards but also high risk. Use cautiously! #RiskManagement",
    "🔄 DCA (Dollar Cost Averaging) helps reduce risk and smooth out volatility. #InvestWisely",
]

# Promotional tweets with referral link        
referral_tweets = [
    "🚀 Start trading crypto with low fees! Sign up now: [https://bit.ly/4kUQRqh] #CryptoTrading",
    "💰 Earn passive income with staking & yield farming! Join here: [https://bit.ly/4kUQRqh] #DeFi",
    "🔥 Get exclusive trading rewards when you sign up! Register now: [https://bit.ly/4kUQRqh] #Investing",
    "📈 Want to trade like a pro? Use my referral link for bonuses! [https://bit.ly/4kUQRqh] #CryptoTips",
    "💹 Secure your crypto assets with the best exchange. Sign up today: [https://bit.ly/4kUQRqh] #Security",
]

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
