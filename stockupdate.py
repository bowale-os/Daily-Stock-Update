import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY =  os.getenv("NEWS_API_KEY")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'outputsize':'compact',
    'datatype':'json',
    'apikey':STOCK_API_KEY
}

news_parameters = {
    'q':COMPANY_NAME,
    'apiKey':NEWS_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = stock_response.json()


# Extract the time series data
time_series = data.get("Time Series (Daily)", {})

# Sort the dates in descending order to get the most recent ones
sorted_dates = sorted(time_series.keys(), reverse=True)

# Ensure there are at least two trading days available
if len(sorted_dates) < 2:
    raise ValueError("Not enough trading data available.")

# Get the latest and previous trading day closes
latest_close = float(time_series[sorted_dates[0]]['4. close'])
previous_close = float(time_series[sorted_dates[1]]['4. close'])

# Calculate the percentage change
change = latest_close - previous_close
percent_change = round((change / previous_close) * 100, 2)  # Rounded to two decimal places

#Set emoji
emoji = '🔺' if percent_change > 0 else '🔻'


#Set your preferred change percent
if abs(percent_change) >= 3:
    sender_email = "danielsobowale67@gmail.com"
    sender_password = EMAIL_APP_PASSWORD
    receiver_email = sender_email

    news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    tesla_news = news.json()
    articles = tesla_news['articles']

    top_three = articles[:3]
    full_body = f"Stock Update: {STOCK_NAME}\n\n"
    if not articles:
        full_body += '\nNo recent news available.\n'
    for article in top_three:
        source_name = article['source']['name']
        title = article['title']
        description = article['description']
        url = article['url']
        author = article['author']
        full_body += (
            f"Source: {source_name}\n"
            f"Title: {title}\n"
            f"Description: {description}\n"
            f"Read more: {url}\n\n"
        )

    # Email content
    subject = f"Tesla Stock Update: {emoji}{percent_change}% change!!!"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(full_body, 'plain', 'utf-8'))

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print('% Change is less than 5')



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

