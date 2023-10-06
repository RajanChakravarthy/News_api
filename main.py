import requests

api_key = 'c5db475bce124feba60d0ca22b62e089'
url = ('https://newsapi.org/v2/everything?q=tesla&from=2023-09-06&sortBy'
       '=publishedAt&apiKey=c5db475bce124feba60d0ca22b62e089')

# Make requests
request = requests.get(url)
# Get dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])

