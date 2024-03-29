import os
import sys
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def exception(e):
    e_type, e_object, e_traceback = sys.exc_info()

    e_filename = os.path.split(e_traceback.tb_frame.f_code.co_filename)[1]
    e_message = str(e)
    e_line_number = e_traceback.tb_lineno

    error = (
        f'Exception type: {e_type}\n'
        f'Exception filename: {e_filename}\n'
        f'Exception line number: {e_line_number}\n'
        f'Exception message: {e_message}'
    )

    del (e_type, e_object, e_traceback)

    print(error)


class Score:
    def __init__(self):
        self.url: str = "https://www.espncricinfo.com/live-cricket-score"
        self.header: dict = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36'
        }

        self.match: list = []
        self.result: list = []

    def cricket_detail(self):
        try:
            response = requests.get(self.url, headers=self.header)

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find_all('div', {
                'class': ('ds-border-b ds-border-line ds-w-1/2', 'ds-border-b ds-border-line ds-border-r ds-w-1/2')})

            for content in main_content:
                _info = content.find('div', {'class': 'ds-truncate'})

                _time = _info.find('span',
                                   {'class': 'ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5'}).get_text() \
                    if _info else 'N/A'

                _detail = _info.find('div',
                                     {'class': 'ds-text-tight-xs ds-truncate ds-text-typo-mid3'}).get_text() \
                    if _info else 'N/A'

                _split = _detail.split(',')

                _tour = _split[-1]
                _date = f"{_split[-3]},{_split[-2]}"
                _info = f"{_split[0]},{_split[1]}"

                _status = content.find('p', {'class': 'ds-text-tight-s ds-font-regular ds-truncate ds-text-typo'})
                _match_status = _status.find('span').get_text() if _status else 'N/A'

                data: dict = {
                    "Time": _time,
                    "Details": _info,
                    "Tour": _tour,
                    "Date": _date,
                    "Status": _match_status
                }

                self.match.append(data)
            return self.match

        except Exception as e:
            exception(e)

    def cricket_score(self):
        try:
            response = requests.get(self.url, headers=self.header)

            soup = BeautifulSoup(response.content, 'html.parser')

            team_scores = soup.find_all('div', class_='ci-team-score')

            for team_score in team_scores:
                team_name = team_score.find('p', class_='ds-font-bold').text.strip() if team_scores else 'N/A'

                flag_image_src = team_score.find('img').get('src') if team_scores else 'N/A'

                overs = team_score.find('span', class_='ds-text-compact-xs').get_text() \
                    if team_score.find('span', class_='ds-text-compact-xs') else 'N/A'

                strong_tags = team_score.find_all('strong')

                runs = ''
                for strong_tag in strong_tags:
                    run = strong_tag.get_text() if team_score.find('strong') else 'N/A'
                    runs += run

                self.result.append({
                    "Team": team_name,
                    "Flag": flag_image_src,
                    "Overs": overs,
                    "Runs": runs
                })

            team_a: list = self.result[::2]
            team_b: list = self.result[1::2]

            return team_a, team_b

        except Exception as e:
            exception(e)


if __name__ == '__main__':
    app = Score()
    a, b = app.cricket_score()
    print(a)
    print(b)
