from flask import Flask, request
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Get today's date
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Fetch a random quote from the API
    quote_response = requests.get('https://api.quotable.io/random')
    quote_data = quote_response.json()
    quote_text = quote_data.get('content', 'No quote available')
    quote_author = quote_data.get('author', 'Unknown')

    # Display today's date and the random quote
    return f"Welcome to the Python app on Aptible!\nToday's date is: {today_date}\n\n"\
        f"Random Quote:\n'{quote_text}'\n- {quote_author}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)