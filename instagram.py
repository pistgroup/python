import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import loginInfo
import urllib

options = webdriver.ChromeOptions()
options.add_argument("--headless")
#options=options,ヘッダーレスの場合
driver = webdriver.Chrome(executable_path=r"C:\Users\USER\Anaconda3\Lib\site-packages\selenium\chromedriver")

url = "https://www.instagram.com/"
driver.get(url)
time.sleep(3)  # Waiting 3 seconds after we open the page.

# ログイン処理
login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login.click()
time.sleep(2)

username = driver.find_element_by_name("username")
username.send_keys(loginInfo.username)

password = driver.find_element_by_name("password")
password.send_keys(loginInfo.password)
login_button = driver.find_element_by_class_name("L3NKy")
login_button.submit()
time.sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "HoLwm")))
pop_up = driver.find_element_by_class_name("HoLwm")
pop_up.click()

#検索する
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(1)

tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja"
tagName = input("タグを入力してください：") #タグの名前
encodedTag = urllib.parse.quote(tagName)  # 普通にURLに日本語は入れられないので、エンコードする
encodedURL = tagSearchURL.format(encodedTag)
print("encodedURL:{}".format(encodedURL))
driver.get(encodedURL)
time.sleep(3)

#写真を取得してクリックする
mediaSelector = "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a"
likeXpath = '/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span'
#カウンター
likedCounter = 1
followCounter= 0

nextpath = "a.coreSpriteRightPaginationArrow"
canselPath = "/html/body/div[2]/button[1]"

driver.find_element_by_xpath(mediaSelector).click()
for likedCounter in range(5):
        time.sleep(15)
        driver.find_element_by_xpath(likeXpath).click()
        try:
            time.sleep(5)
            driver.find_element_by_css_selector(nextpath).click()
            likedCounter += 1
        except:
            break
print(" {} いいね".format(likedCounter))