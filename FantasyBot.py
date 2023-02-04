from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import discord
import asyncio

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()
channel_id = 819728143253241917

#PATH = 'F:\\Users\Michael\Downloads\chromedriver_win32\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#driver = webdriver.Chrome(executable_path=os.environ.get(PATH), chrome_options=chrome_options)

driver.get("https://www.rotowire.com/basketball/news.php?view=injuries")

img1 = driver.find_elements_by_class_name("news-update__logo")
player1 = driver.find_elements_by_class_name("news-update__player-link")
injury1 = driver.find_elements_by_class_name("news-update__headline")
info1 = driver.find_elements_by_class_name("news-update__news")

img = []
player =[]
injury = []
info = []
for j in range(len(player1)):
    name = player1[j].text
    desc = injury1[j].text
    photo = img1[j].get_attribute("src")
    inf = info1[j].text
    img.append(photo)
    player.append(name)
    injury.append(desc)
    info.append(inf)

async def time_check():
    await client.wait_until_ready()
    msg_channel = client.get_channel(channel_id)
    global img
    global player
    global injury
    global info
    print(player)
    while not client.is_closed():
        driver.refresh()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "news-update__player-link"))
            )
            pic = driver.find_elements_by_class_name("news-update__logo")
            plyr = driver.find_elements_by_class_name("news-update__player-link")
            inj = driver.find_elements_by_class_name("news-update__headline")
            des = driver.find_elements_by_class_name("news-update__news")
            notify = []
            new = plyr[0].text
            og = player[0]
            if new != og:
                list1 = []
                for i in range(len(plyr)):
                    n1 = plyr[i].text
                    list1.append(n1)
                while len(list1) < 1:
                    driver.refresh()
                    await asyncio.sleep(10)
                    pic = driver.find_elements_by_class_name("news-update__logo")
                    plyr = driver.find_elements_by_class_name("news-update__player-link")
                    inj = driver.find_elements_by_class_name("news-update__headline")
                    des = driver.find_elements_by_class_name("news-update__news")
                    notify = []
                    new = plyr[0].text
                    og = player[0]
                    if new != og:
                        list1 = []
                        for i in range(len(plyr)):
                            n1 = plyr[i].text
                            list1.append(n1)
                x = 0
                while list1[x] != og and x < len(list1):
                    nme = plyr[x].text
                    dsc = inj[x].text
                    pht = pic[x].get_attribute("src")
                    txt = des[x].text
                    notify.append([nme, dsc, pht, txt])
                    x = x + 1
            if len(notify) > 0:
                notify.reverse()
                for i in range(len(notify)):
                    update = discord.Embed(title=notify[i][1], description=notify[i][3], inline=False, color=0x3498db)
                    update.set_author(name=notify[i][0])
                    update.set_thumbnail(url=notify[i][2])
                    await msg_channel.send(content=None, embed=update)
            img2 = []
            player2 = []
            injury2 = []
            info2 = []
            for k in range(len(player1)):
                nme = plyr[k].text
                dsc = inj[k].text
                pht = pic[k].get_attribute("src")
                txt = des[k].text
                img2.append(pht)
                player2.append(nme)
                injury2.append(dsc)
                info2.append(txt)
            img = img2
            player = player2
            injury = injury2
            info = info2
            await asyncio.sleep(1)
        finally:
            driver.refresh()


@client.event
async def on_message(message):
    if message.content == "!0401":
        ppl = ["Kyrie Irving", "James Harden", "Blake Griffin", "Jimmy Butler", "Bam Adebayo", "Zion Williamson", "Kevin Durant", "Joel Embiid"]
        out = ["Out due to health and safety protocols", "Out due to health and safety protocols", "Out due to COVID protocols",
               "Ruled out Thursday", "Unavailable Thursday", "Likely out for one week", "Will not return for the regular season", "Expected to undergo surgery"]
        sen = ["Irving (COVID-19 protocols) and members of the Brooklyn Nets will be out indefinitely after a teammate tested positive for COVID-19, Mike Skocsmal of the Brooklyn Times reports.",
               "Harden (COVID-19 protocols) and members of the Brooklyn Nets will be out indefinitely after a teammate tested positive for COVID-19, Mike Skocsmal of the Brooklyn Times reports.",
               "Griffin (COVID-19 protocols) along with other members of the Brooklyn Nets will be out indefinitely after contact tracing found that a teammate tested positive for COVID-19, Mike Skocsmal of the Brooklyn Times reports.",
               "Butler (pelvis) will not play Thursday against Golden State, Hugh Jazbeanes of the Heat nation reports.",
               "Adebayo (not injury related) will be unavailable for Thursday against the Warriors due to mental illness, Hugh Jazbeanes of the Heat nation reports.",
               "After reevaluation, Williamson (right hand) will rest for a week to recover from his sprained right thumb, Jrue Dikonphase of ESPN.com reports.",
               "Durant (hamstring) will sit out until the start of the playoffs after being reevaluated and diagnosed with fournier gangrene, Robin Urvyrgyniti of ESPN reports.",
               "Previously expecting a return this weekend, Embiid ruptured his corpus cavernosum during team practice Thursday afternoon and is expected to undergo surgery on Friday. His return is likely delayed for another 2-4 weeks, Harry Asbalz of the Sixers Wire reports."
               ]
        pho = ["https://content.rotowire.com/images/teamlogo/basketball/100BKN.png?v=2","https://content.rotowire.com/images/teamlogo/basketball/100BKN.png?v=2",
               "https://content.rotowire.com/images/teamlogo/basketball/100BKN.png?v=2", "https://content.rotowire.com/images/teamlogo/basketball/100MIA.png?v=2",
               "https://content.rotowire.com/images/teamlogo/basketball/100MIA.png?v=2", "https://content.rotowire.com/images/teamlogo/basketball/100NO.png?v=2",
               "https://content.rotowire.com/images/teamlogo/basketball/100BKN.png?v=2", "https://content.rotowire.com/images/teamlogo/basketball/100PHI.png?v=2"]
        ppl.reverse()
        out.reverse()
        sen.reverse()
        pho.reverse()
        for i in range(len(ppl)):
            await asyncio.sleep(10)
            send = discord.Embed(title=out[i], description=sen[i], inline=False, color=0x3498db)
            send.set_author(name=ppl[i])
            send.set_thumbnail(url=pho[i])
            await message.channel.send(content=None, embed=send)
    elif message.content == "m":
        send = discord.Embed(title="Out indefinitely", description="After Wednesday's game against Boston, Doncic (face) suffered cancrum oris during post game workout, Samir Komonditz of ESPN reports.", inline=False, color=0x3498db)
        send.set_author(name="Luka Doncic")
        send.set_thumbnail(url="https://content.rotowire.com/images/teamlogo/basketball/100DAL.png?v=2")
        await message.channel.send(content=None, embed=send)

client.loop.create_task(time_check())
client.run(token)