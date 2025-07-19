import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
YAHOO_API_KEY = os.getenv("YAHOO_FINANCE_API_KEY")



@tool
def tool1_weather(query: str) -> str:
    """
    Weather Tool: Handles current, forecast, yesterday's weather, or city comparison based on user query.
    Automatically extracts intent and cities from input.
    """
    try:
        import re
        from datetime import datetime, timedelta

        
        q = query.lower()

       
        is_forecast = "forecast" in q or "next 7" in q or "7-day" in q
        is_yesterday = "yesterday" in q
        is_compare = "compare" in q or (" and " in q and "weather" in q)

       
        cities = re.findall(r"(in|at|of)?\s*([A-Z][a-z]+(?: [A-Z][a-z]+)?)", query)
        city_names = list({match[1].strip() for match in cities}) or [query.strip()]

       
        if is_compare and len(city_names) >= 2:
            results = []
            for city in city_names[:2]:
                url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
                data = requests.get(url).json()
                temp = data["current"]["temp_c"]
                condition = data["current"]["condition"]["text"]
                results.append(f"{city}: {temp}°C, {condition}")
            return f"🌤️ City Comparison:\n" + "\n".join(results)

        city = city_names[0]

        # Yesterday’s weather
        if is_yesterday:
            yday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
            url = f"http://api.weatherapi.com/v1/history.json?key={WEATHER_API_KEY}&q={city}&dt={yday}"
            res = requests.get(url)
            data = res.json()
            avg_temp = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
            condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
            return f"📆 Yesterday’s Weather in {city} ({yday}): {avg_temp}°C, {condition}"

        # 7-Day Forecast
        elif is_forecast:
            url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=7"
            data = requests.get(url).json()
            result = f"📅 7-Day Forecast for {city.title()}:\n"
            for day in data["forecast"]["forecastday"]:
                result += f"{day['date']}: {day['day']['condition']['text']}, Avg Temp: {day['day']['avgtemp_c']}°C\n"
            return result.strip()

        
        else:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
            data = requests.get(url).json()
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            return f"🌤️ Current Weather in {city.title()}: {temp}°C, {condition}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


@tool
def tool2_stock(query: str) -> str:
    """
    Dynamically fetch stock symbol from Yahoo Finance and return its stock price.
    """
    import requests
    import yfinance as yf

    headers = {"User-Agent": "Mozilla/5.0"}
    search_url = f"https://query1.finance.yahoo.com/v1/finance/search?q={query}"

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        quotes = data.get("quotes")
        if not quotes:
            return f"❌ No matching stock symbol found for '{query}'."

        symbol = quotes[0].get("symbol")
        if not symbol:
            return f"⚠️ No symbol found for '{query}' in search results."

        ticker = yf.Ticker(symbol)
        price = ticker.info.get("regularMarketPrice")

        if price:
            return f"📈 Stock: {symbol}\n💰 Current Price: ₹{price}"
        else:
            return f"⚠️ Could not fetch price for '{symbol}'."

    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"


@tool
def tool3_general_qa(question: str) -> str:
    """Tool3: Answer general knowledge questions like 'What is AI?' or 'Who is the PM of India?'."""
    return f"(LLM will answer this): {question}"
