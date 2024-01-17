import os
import sys
import requests
from bs4 import BeautifulSoup


class News:
    def __init__(self):
        self.url: str = "https://www.espncricinfo.com/live-cricket-score"
        self.header: dict = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36'
        }

        self.match: list = []

    def cricket_score(self):
        try:
            response = requests.get(self.url, headers=self.header)

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find_all('div', {
                'class': ('ds-border-b ds-border-line ds-w-1/2', 'ds-border-b ds-border-line ds-border-r ds-w-1/2')})

            for score in main_content:
                _info = score.find('div', {'class': 'ds-truncate'})

                _time = _info.find('span',
                                   {'class': 'ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5'}).get_text()
                _detail = _info.find('div', {'class': 'ds-text-tight-xs ds-truncate ds-text-typo-mid3'}).get_text()

                _team = score.find('div', {'class': 'ds-flex ds-flex-col ds-mt-2 ds-mb-2'})

                _team_content = []
                for _name in _team:
                    _team_flag = _name.find('img').get('src')
                    _team_name = _name.find('p').get_text()
                    _team_content.append({
                        "flag": _team_flag,
                        'name': _team_name
                    })

                # _status = score.find('p', {'class': 'ds-text-tight-s ds-font-regular ds-truncate ds-text-typo'})
                # _match_status = _status.find('span').get_text()

                data: dict = {
                    "Time": _time,
                    "Details": _detail,
                    "Teams": _team_content,
                    # "Status": _status
                }

                self.match.append(data)

            return self.match

        except Exception as e:
            e_type, e_object, e_traceback = sys.exc_info()

            e_filename = os.path.split(e_traceback.tb_frame.f_code.co_filename)[1]
            e_message = str(e)
            e_line_number = e_traceback.tb_lineno

            print(
                f'Exception type: {e_type}\n'
                f'Exception filename: {e_filename}\n'
                f'Exception line number: {e_line_number}\n'
                f'Exception message: {e_message}'
            )

            del (e_type, e_object, e_traceback)


if __name__ == '__main__':
    app = News()
    print(app.cricket_score())