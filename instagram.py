import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import loginInfo
import requests

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\USER\Anaconda3\Lib\site-packages\selenium\chromedriver")
request = requests.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

#カウンター
likedCounter = 1
followCounter= 0

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
pop_up = driver.find_element_by_class_name("HoLwm")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "HoLwm")))



#検索する
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(1)

#検索する
push = driver.find_element_by_class_name('XTCLo')
seachkey = input('いいねを押したいタグを入力してください：')
print(seachkey)
push.send_keys(seachkey)
push.submit()
time.sleep(5)

#写真を取得してクリックする
request.find_element_by_css_selector(mediaSelector).click()
for likedCounter in range(500):
        time.sleep(15)
        request.find_element_by_xpath(likeXpath).click()
        time.sleep(1)
        request.find_element_by_xpath(followpath).click()
        try:
            time.sleep(5)
            likedCounter += 1
            print(" {} いいね".format(likedCounter))
            request.find_element_by_xpath(nextPagerSelector).send_keys(Keys.RIGHT)
            followCounter+= 1
            print(" {} フォロー".format(followCounter))
        # すでにフォロー中の場合の処理
        except:
            request.find_element_by_xpath(canselpath)
            request.find_element_by_xpath(canselpath).click()
            request.implicitly_wait(5)