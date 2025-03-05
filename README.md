# Tesla Stock Price & News Alert

This Python script monitors the daily stock price of **Tesla Inc. (TSLA)** and sends an email alert if the stock price changes by a specified percentage compared to the previous trading day. Additionally, the script fetches the latest news articles related to Tesla and includes them in the email notification.

---

## Features

- **Stock Price Monitoring:**  
  Fetches the latest daily closing prices of **Tesla Inc. (TSLA)** using the [Alpha Vantage API](https://www.alphavantage.co/).
  
- **Stock Price Change Calculation:**  
  Calculates the percentage change in Tesla’s stock price compared to the previous trading day. If the change is above the threshold (default is 1%), an alert email is triggered.
  
- **Latest Tesla News:**  
  Fetches the top 3 latest news articles related to Tesla using the [NewsAPI](https://newsapi.org/). The email includes article titles, descriptions, sources, and links.

- **Email Notifications:**  
  Sends an email with the stock price update and the latest news. The email content is dynamic, depending on the stock price change and news availability.

---

## Prerequisites

- Python 3.x  
- Required Python libraries: `requests`, `smtplib`, `email.mime`  
- API Keys:  
  - [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key)
  - [NewsAPI Key](https://newsapi.org/register)
- **Gmail App Password**  
  - If using Gmail to send emails, generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en) to use with this script.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/tesla-stock-alert.git
   cd tesla-stock-alert
   ```

2. **Install Required Libraries:**

   Install dependencies using `pip`:

   ```bash
   pip install requests
   ```

3. **Set Up Environment Variables:**

   Ensure you have the following environment variables set up:
   - `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key.
   - `NEWS_API_KEY`: Your NewsAPI key.
   - `EMAIL_APP_PASSWORD`: Your Gmail App Password.

   You can set them in your environment or create a `.env` file to store them securely.

---

## How to Use

1. **Edit Email Configuration:**  
   Update the `sender_email` and `receiver_email` variables in the script to the appropriate email addresses.

2. **Run the Script:**

   Simply run the script:

   ```bash
   python tesla_stock_alert.py
   ```

   If the percentage change in Tesla's stock price is greater than or equal to 1%, an email will be sent with the stock update and the top 3 Tesla news articles.

---

## Example Output

If the stock price changes by 2%, the email subject and body will look like:

**Email Subject:**  
`Tesla Stock Update: 🔺2% change!!!`

**Email Body:**  
```
Stock Update: TSLA

Change: +2% 

Source: Bloomberg
Title: Tesla Stock Jumps After Record Earnings
Description: Tesla's earnings report shows strong growth, leading to a surge in stock prices.
Read more: https://www.bloomberg.com/news/article/tesla-record-earnings

Source: CNBC
Title: Tesla Hits New Milestone in Production
Description: Tesla announces it has surpassed its production goals for the quarter.
Read more: https://www.cnbc.com/tesla-hits-new-production-milestone

Source: Reuters
Title: Tesla Stock Expected to Rise in Coming Days
Description: Experts predict a positive trend for Tesla's stock after recent developments.
Read more: https://www.reuters.com/tesla-stock-rise
```

---

## Error Handling

- If there is not enough stock data (less than 2 trading days), the script will raise an error.
- If the stock price change is less than the specified threshold (default is 1%), no email will be sent.

---

## Customization

- **Threshold Change Percentage:**  
  You can adjust the threshold for sending email notifications by modifying the line:

  ```python
  if abs(percent_change) >= 1:
  ```

  Change `1` to any other value (e.g., `5` for 5%).

- **Email Content:**  
  The email template is simple. You can enhance it by using HTML for better formatting.

---

## License

This project is licensed under the MIT License.

---

## Contributions

Feel free to fork this project and contribute improvements, fixes, or new features. Pull requests are welcome!

---

## Contact

If you have any questions, feel free to reach out to me at:  
**Email:** [danielsobowale67@gmail.com](mailto:danbowale@gmail.com)  
