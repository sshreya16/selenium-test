from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to your ChromeDriver
service = Service("C:\Users\Shreya\Desktop\chromedriver-win64")

driver = webdriver.Chrome()
driver.get("https://shaadi.com")
title = driver.title
driver.implicitly_wait(0.5)
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
text_box.send_keys("Selenium")
submit_button.click()
text = message.text
driver.quit()