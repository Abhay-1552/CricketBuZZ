from flask import Flask, request, render_template
from scraping_data import News
from scraping_score import Score


app = Flask(__name__, template_folder='template')


@app.route('/')
def root():
    _news = News()
    _score = Score()

    _news_data = _news.cricket_news()
    _news_video = _news.feature_videos()
    _match_details = _score.cricket_detail()

    return render_template('index.html', news=_news_data, video=_news_video, details=_match_details)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
