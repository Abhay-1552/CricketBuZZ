from flask import Flask, request, render_template
from scraping_data import News


app = Flask(__name__, template_folder='template')


@app.route('/')
def root():
    _news = News()

    _news_data = _news.cricket_news()
    _news_video = _news.feature_videos()

    return render_template('index.html', news=_news_data, video=_news_video)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
