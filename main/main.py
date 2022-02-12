import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition


s = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = 'https://2domains.ru/login'

def authentication():
    driver.get(url)
    driver.find_element(By.ID,"loginform-username").send_keys("admin@leads.su")
    time.sleep(2)
    driver.find_element(By.ID,"loginform-password").send_keys("AW31dsa1223sd3")
    time.sleep(2)
    driver.find_element(By.NAME,"login-button").click()

    wait = WebDriverWait(driver, 15)
    wait.until(Condition.presence_of_element_located((By.CSS_SELECTOR, '.b-service.b-service.b-service--align.b-service--default')))

    try:
        while True:
            wait.until(Condition.element_to_be_clickable((By.CLASS_NAME, 'b-service__wide-button'))).click()
    except:
        print('кнопка закончилась !!')

    html = driver.page_source
    driver.close()
    return html


def find_elements(el):
    soup = BeautifulSoup(el, "html.parser")
    domains = []
    for element in soup.find_all('div', {'class' : 'b-service__area clickable'}):
        res = element.text
        arr = []
        for i in res.lower().split():
            if i in ('самое', 'время', 'продлить!', 'до', 'продлить'):
                continue
            arr.append(i)
        domains.append('; '.join(arr))
    return domains

result = find_elements(authentication())

with open("success.txt","w", encoding="utf-8") as f:
    for item in result:
        f.write("%s\n" % item)
