import requests
from send_email import send_email

api_key = 'c5db475bce124feba60d0ca22b62e089'
url = ('https://newsapi.org/v2/everything?q=tesla&from=2023-09-06&sortBy'
       '=publishedAt&apiKey=c5db475bce124feba60d0ca22b62e089')

# Make requests
request = requests.get(url)
# Get dictionary with data
content = request.json()

# Access the article titles and description
email_body = ''
for article in content['articles']:
    email_body = email_body + article['title'] + '\n' + article['description'] + 2*'\n'

email_body = email_body.encode('utf-8')

# Sending Email to client
send_email(email_body)

