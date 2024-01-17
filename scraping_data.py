from bs4 import BeautifulSoup
import requests


class News:
    def __init__(self):
        self.url = "https://www.cricbuzz.com/"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36'
        }
        self.news_storage = []
        self.news_video = []

    def cricket_news(self):
        try:
            response = requests.get(self.url, headers=self.header)

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find_all('div', {'class': 'big-crd-main cb-bg-white cb-pos-rel'})

            for content in main_content:
                context = content.find('div', {'class': 'crd-cntxt'})
                _context = context.get_text() if context else "N/A"

                img = content.find('img').get('src')

                title = content.find('h2', {'class': 'big-crd-hdln'})
                _title = title.find('a').get_text() if title else "N/A"

                intro = content.find('div', {'class': 'cb-nws-intr'})
                _intro = intro.get_text() if intro else "N/A"

                data = {
                    "Context": _context,
                    "Image": img,
                    "Title": _title.lstrip('\t'),
                    "Intro": _intro
                }

                self.news_storage.append(data)

            return self.news_storage

        except Exception as e:
            print("Error fetching content:", e)
            return "Error fetching data."

    def feature_videos(self):
        try:
            response = requests.get(self.url, headers=self.header)

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find_all('div', {'class': 'cb-col cb-col-100 cb-mid-wrp'})

            for content in main_content:
                _video = content.find('a', {'class', 'suggested-video-gtm'})
                _video_url = _video.get('href') if _video else 'N/A'

                _title = _video.find('h4').get_text()
                _image = _video.find('img').get('src')

                _time = content.find('div', {'class': 'cb-nws-time'}).get_text()

                data = {
                    'Url': _video_url,
                    'Title': _title,
                    'Image': _image,
                    'Time': _time
                }

                self.news_video.append(data)
            return self.news_video

        except Exception as e:
            print("Error fetching content:", e)
            return "Error fetching data."


if __name__ == '__main__':
    app = News()
    print(app.feature_videos())
