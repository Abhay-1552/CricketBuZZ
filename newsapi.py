import requests

url = "https://cricket-news-api.p.rapidapi.com/cricnews/cricbuzz"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
    "X-RapidAPI-Key": "36bdb2896amshc664096170e4d90p1b6293jsnb64d9c238498",
    "X-RapidAPI-Host": "cricket-news-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response)
