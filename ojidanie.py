"""
2.4 Настройка ожиданий
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
 Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome('C:\\Users\\Mixa\\.vscode\\chromedriver.exe')
    browser.get(link)

    konpka = browser.find_element_by_css_selector('#book')

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,'price'), '100')
    )
    konpka.click()

    x_1 = browser.find_element_by_css_selector('#input_value')
    x = x_1.text

    y = calc(x)

    pole = browser.find_element_by_css_selector('#answer')
    pole.send_keys(y)

    submit = browser.find_element_by_css_selector('#solve')
    submit.click()

finally:

    time.sleep(10)
    browser.quit()





