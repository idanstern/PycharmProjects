from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver1 = webdriver.Chrome()
driver1.get("C:/Users/Idan Stern/OneDrive/שולחן העבודה/tip_calc/index.html")
billamt = driver1.find_element("id", "billamt")
billamt.send_keys("100")
driver1.find_element("xpath", "//*[@id=\"serviceQual\"]/option[3]").click()
driver1.find_element("id", "peopleamt").send_keys("5")
driver1.find_element("id", "musicQuality").send_keys("4")
driver1.find_element("id", "calculate").click()
expected = "8"
actual = driver1.find_element("id", "tip").text
print(f"actual is: {actual}")
if expected == actual:
    print("tip is ok")
else:
    print("tip is not ok")

sleep(10)
