from bs4 import BeautifulSoup

html = """
<div class="ds-flex ds-flex-col ds-mt-2 ds-mb-2">
    <div class="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1">
        <div class="ds-flex ds-items-center ds-min-w-0 ds-mr-1" title="England Lions">
            <img width="20" height="20" alt="England Lions Flag" class="ds-mr-2" src="https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_160,q_50/lsci/db/PICTURES/CMS/313200/313257.logo.png" style="width: 20px; height: 20px;">
            <p class="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3">England Lions</p>
        </div>
        <div class="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap">
            <span class="ds-text-compact-xs ds-mr-0.5"></span>
            <strong class="ds-text-typo-mid3">553/8d</strong>
        </div>
    </div>
    <div class="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1">
        <div class="ds-flex ds-items-center ds-min-w-0 ds-mr-1" title="India A">
            <img width="20" height="20" alt="India A Flag" class="ds-mr-2" src="https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_160,q_50/lsci/db/PICTURES/CMS/313300/313306.logo.png" style="width: 20px; height: 20px;">
            <p class="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate">India A</p>
            <i class="icon-dot_circular ds-text-icon-error hover:ds-text-icon-error-hover" style="font-size: 12px;"></i>
        </div>
        <div class="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap">
            <span class="ds-text-compact-xs ds-mr-0.5">(20 ov) </span>
            <strong class="">72/6</strong>
        </div>
    </div>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')

# Extracting team names and scores
team_elements = soup.find_all('div', class_='ci-team-score')

for team_element in team_elements:
    team_name_element = team_element.find('p', class_='ds-font-bold')
    score_element = team_element.find('strong', class_='ds-text-typo-mid3')

    if team_name_element and score_element:
        team_name = team_name_element.text.strip()
        score = score_element.text.strip()

        print(f'Team: {team_name}, Score: {score}')
