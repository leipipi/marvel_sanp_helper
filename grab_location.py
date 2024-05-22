from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import requests

# 获取网页内容
url = "https://marvelsnapzone.com/locations/"
response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

with open("data/location_html.html", "r", encoding="utf-8") as f:
    html_content = f.read()
soup = BeautifulSoup(html_content, "html.parser")

# 找到所有cards
cards = soup.find_all("a", class_="simple-card location")

print(cards)

# 遍历每个card
for card in cards:
    # 获取图片链接和名称
    img_url = card.find("img")["data-src"]
    img_name = card["data-name"] + ".png"

    # 下载图片并保存为png格式
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    img.save(os.path.join("image/location", img_name))

print("图片保存完成！")