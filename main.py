import requests
from send_email import send_email

topic = 'Tesla'
api_key = 'c5db475bce124feba60d0ca22b62e089'
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'from=2023-09-08&'
       'sortBy=publishedAt&'
       'apiKey=c5db475bce124feba60d0ca22b62e089&'
       'language=en')

# Make requests
request = requests.get(url)
# Get dictionary with data
content = request.json()

# Access the article titles and description
email_body = ''
for article in content['articles'][:20]:
    if article['title'] is not None:
        email_body = ("Subject: Today's News"
                      + '\n' + email_body + article['title'] + '\n' + article['description']
                      + '\n' + article['url'] + 2*'\n')

email_body = email_body.encode('utf-8')

# Sending Email to client
send_email(message=email_body)

