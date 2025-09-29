Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# ==============================
# 👋 CryptoBuddy: Rule-Based Chatbot
# Beginner-friendly Python Script
# ==============================

# 1. Predefined Crypto Dataset
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}  

# 2. Chatbot Logic Function
def crypto_chatbot(user_query):
    user_query = user_query.lower()  # simplify matching
    
    # Rule 1: Sustainability
...     if "sustainable" in user_query or "eco" in user_query:
...         recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
...         return f"🌱 Invest in {recommend}! It’s eco-friendly with a sustainability score of {crypto_db[recommend]['sustainability_score']}/10."
...     
...     # Rule 2: Trending (profitability)
...     elif "trending" in user_query or "rising" in user_query:
...         trending = [c for c,v in crypto_db.items() if v["price_trend"] == "rising"]
...         return f"📈 Cryptos trending up: {', '.join(trending)}."
...     
...     # Rule 3: Long-term growth
...     elif "long-term" in user_query or "growth" in user_query:
...         recommend = "Cardano"
...         return f"🚀 {recommend} is trending up and has a strong sustainability score! Perfect for long-term potential."
...     
...     # Rule 4: Market Cap
...     elif "market cap" in user_query:
...         high_caps = [c for c,v in crypto_db.items() if v["market_cap"] == "high"]
...         return f"💰 High market cap cryptos: {', '.join(high_caps)}."
...     
...     # Default response
...     else:
...         return "🤔 I didn’t get that. Try asking:\n- 'Which crypto is trending up?'\n- 'What’s the most sustainable coin?'\n- 'Which crypto should I buy for long-term growth?'"
... 
... # 3. Run Interactive Chat
... print("👋 Hi! I'm CryptoBuddy — your friendly crypto assistant!")
... print("⚠️ Disclaimer: I’m not a financial advisor. Always do your own research!\n")
... 
... while True:
...     user_input = input("You: ")
...     if user_input.lower() in ["exit", "quit", "bye"]:
...         print("CryptoBuddy: 👋 Goodbye! Stay smart with your crypto choices!")
...         break
...     response = crypto_chatbot(user_input)
...     print("CryptoBuddy:", response)
>>> [DEBUG ON]
>>> [DEBUG OFF]
>>> [DEBUG ON]
>>> [DEBUG OFF]
