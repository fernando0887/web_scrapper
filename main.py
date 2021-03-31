import pandas as pd
import requests
from bs4 import BeautifulSoup


print('Insira a url desejada:')
req = requests.get(input())
if req.status_code == 200:
    print('Conexão bem sucedida')
    content = req.content


soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')
table = soup.find(name='table', attrs={'id': 'total_stats'})
table = soup.find_all(name='table')
print(soup.prettify())



table_str= str(table)
df = pd.read_html(table_str)[0]
print(df)
