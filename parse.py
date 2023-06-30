from bs4 import BeautifulSoup as BS
import requests
import os
from url import create_folder_if_not_exists, download_and_extract_zip

is_git = input('Do you want to clone or to download repositories (c/d)?: ') == 'c'
name = input('Enter username: ')
while name != '':
    r = requests.get(f'https://github.com/{name}?tab=repositories')
    s = BS(r.content, 'html.parser')
    links = [i.get("href")[1:] for i in s.find_all('a', attrs={'itemprop': 'name codeRepository'})]
    create_folder_if_not_exists('result')
    create_folder_if_not_exists('result/'+name)
    for a in links:
        if is_git:
            os.system(f'cd {os.getcwd()}/result/{a.split("/")[0]} & git clone https://github.com/{a}.git')
        else:
            download_and_extract_zip(f'https://github.com/{a}/archive/refs/heads/main.zip', f'result/{a.split("/")[0]}', f'result/{a}.zip')
    name = input('Enter username: ')
