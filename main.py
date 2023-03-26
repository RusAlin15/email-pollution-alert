import requests
from send_email import send_email
api_key = "ff3071960ed34268bc92cc8ffba45737"
topic = "economy"

url = f"https://newsapi.org/v2/everything?language=en&q={topic}&sortBy=publishedAt&apiKey={api_key}"

response = requests.get(url)
content = response.json()

body =f"Subject: Today's {topic} news" + "\n"
for article in content['articles'][:20]:
    body = body + article['title'] + "\n" + article['description'] +"\n" + article['url'] + 2*"\n"

send_email(body.encode('utf-8'))