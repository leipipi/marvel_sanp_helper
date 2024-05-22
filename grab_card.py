from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import requests

def grab_card():
    # 获取网页内容
    url = "https://marvelsnapzone.com/locations/"
    response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")

    with open("data/card.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")

    # 找到所有cards
    cards = soup.find_all("a", class_="simple-card hasvariants")

    # 指定要抓取哪些卡牌
    grab_list = ['agent 13','america chavez','mantis','nightcrawler','quinjet','angela','the collector','cable','sentinel','moon girl','white queen','devil dinosaur']

    # 卡牌名
    card_names= []
    # 卡牌费用
    card_costs = []
    # 卡牌战力
    card_powers = []

    # 遍历每个card
    for card in cards:
        card_name = card["data-name"]
        if card_name in grab_list:
            print("get ",card_name)
            # 获取图片链接和名称
            img_url = card.find("img")["data-src"]
            img_name = card["data-name"] + ".png"

            # 下载图片并保存为png格式
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            img.save(os.path.join("image/card", img_name))

            card_names.append(card_name)
            card_costs.append(card["data-cost"])
            card_powers.append(card["data-power"])

    print("卡牌图片保存完成！")
    total_card_name,total_card_cost,total_card_power = [],[],[]
    with open('data/card_data.txt', "a+") as f:
        for lines in f.readlines():
            total_card_name.append(lines[0])
            total_card_cost.append(lines[1])
            total_card_power.append(lines[2])
        for card_name,card_cost,card_power in zip(card_names, card_costs, card_powers):
            if len(total_card_name)==0 or card_name not in total_card_name :
                card= card_name + " " + card_cost + " " + card_power+"\n"
                f.write(card)


    return card_names, card_costs, card_powers

grab_card()