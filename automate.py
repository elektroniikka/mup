from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL_STKHLM = "https://www.migrationsverket.se/ansokanbokning/valjtyp?sprak=sv&bokningstyp=2&enhet=Z209&sokande=1"
URL_UPPSLA = "https://www.migrationsverket.se/ansokanbokning/valjtyp?sprak=sv&bokningstyp=2&enhet=MUP1&sokande=1"


capabilities = DesiredCapabilities.CHROME.copy()
# If options doesn't work for https ssl connection resolution, uncomment the following line
# capabilities['acceptInsecureCerts'] = True

options = Options()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=Service(
    executable_path=ChromeDriverManager().install()),desired_capabilities=capabilities, options=options)

driver.get(URL_STKHLM)
driver.implicitly_wait(2)

errorPanel = driver.find_elements(By.CLASS_NAME, "feedbackPanelERROR")
try:
    print(errorPanel.count())
    print(errorPanel.text)
except Exception as e:
    print("Date Found")

dateLine = driver.find_element(By.CLASS_NAME, "fc-day-header")
print(dateLine.text)

driver.get(URL_UPPSLA)
driver.implicitly_wait(2)

errorPanel = driver.find_elements(By.CLASS_NAME, "feedbackPanelERROR")
try:
    print(errorPanel.count())
    print(errorPanel.text)
except Exception as e:
    print("Date Found")
dateLine = driver.find_element(By.CLASS_NAME, "fc-day-header")
print(dateLine.text)


# def reset_reader(driver, color):
#     driver.find_element(by=By.LINK_TEXT, value='Apply').click()
#     print(COLORS[color] + "Resetting device" + COLORSE)
#     time.sleep(5)
#     driver.switch_to.alert.accept()
#     # Give time to operate ...
#     time.sleep(INTERVAL)

# for i in range(10):
#     c = i % len(COLORS)
#     reset_reader(driver, c)

driver.quit()
