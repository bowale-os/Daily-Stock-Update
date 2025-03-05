# 🚀 Tesla Stock Tracker  

This Python script tracks **Tesla Inc. (TSLA)** stock prices and sends an email alert when there is a **5% or more change** in the stock price. If the change threshold is met, it also fetches **the latest news articles** related to Tesla and includes them in the email.  

## 📌 Features  
✅ Fetches daily stock prices using **Alpha Vantage API**.  
✅ Calculates **percentage change** in stock price.  
✅ If the change is **≥5%**, it retrieves **Tesla-related news** from **NewsAPI**.  
✅ Sends an **email alert** with stock updates and news summaries.  
✅ **Automated execution**—can be scheduled to run daily.  

## 🛠️ Setup Instructions  

### 1️⃣ Prerequisites  
Ensure you have **Python 3+** installed. Install required dependencies:  

```bash
pip install requests smtplib email
```

### 2️⃣ API Key Setup  
You'll need **API keys** for:
- [Alpha Vantage](https://www.alphavantage.co/support/#api-key) (Stock data)
- [NewsAPI](https://newsapi.org/register) (News articles)

Once you get the keys, replace:  
```python
'apikey': 'YOUR_ALPHAVANTAGE_API_KEY'
'apiKey': 'YOUR_NEWSAPI_API_KEY'
```

### 3️⃣ Email Configuration  
Replace the sender email and **use an App Password** (if using Gmail):  
```python
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
```
> 💡 **Tip:** Never expose credentials in code—use **environment variables** instead.

### 4️⃣ Run the Script  
Simply execute:  
```bash
python stock_tracker.py
```
You can also schedule it using **cron jobs** (Linux/macOS) or **Task Scheduler** (Windows).  

## 📧 Email Alert Example  
**Subject:** Tesla Stock Update: 🔺5% change!!!  

**Body:**  
```
Stock Update: TSLA

Source: CNBC  
Title: Tesla Shares Surge After Strong Q4 Report  
Description: Tesla stock jumped 6% after reporting strong revenue growth...  
Read more: https://www.cnbc.com/article/tesla-q4-report.html  
```

## 🚀 Future Enhancements  
- ✅ **Twilio SMS Alerts** 📱  
- ✅ **Better Email Formatting (HTML)** ✨  
- ✅ **Secure API Keys via Environment Variables** 🔒  
- ✅ **Automate Daily Execution** ⏳  

## 📝 License  
This project is for **educational purposes** only. Use it responsibly! 🚀  
