import requests
from bs4 import BeautifulSoup

url = input("スクレイピングしたいWebページのURLを入力してください: ")

# HTTP GETリクエストを送信してWebページを取得する
response = requests.get(url)

# 取得したWebページのHTMLコンテンツを解析する
soup = BeautifulSoup(response.text, 'html.parser')

# ヘッダーやフッター、ナビゲーションバーを除外するためのHTMLタグを指定する
exclude_tags = ['header', 'footer', 'nav', 'form', 'select', 'ul' , 'li' ]



# 本文を取得する
body_list = []
for tag in soup.find_all(['p', 'div', 'article']):
    # 除外するタグを持つ親要素がある場合は除外する
    if any(exclude_tag in [parent.name for parent in tag.parents] for exclude_tag in exclude_tags):
        continue
    # テキストを取得する
    text = tag.get_text()
    if text.strip():
        body_list.append(text.strip())

# 重複を取り除く
body_set = set(body_list)

# 取得したデータをファイルに保存する
with open('output.txt', 'w', encoding='utf-8') as f:
    for body in body_set:
        f.write(body + '\n')