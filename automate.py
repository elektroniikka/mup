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
dateLine = driver.find_element(By.CLASS_NAME, "fc-day-header")
if len(errorPanel) > 0:
    print("No dates found for Stockholm")
else:
    print("Date found to be {0}".format(dateLine.text))

driver.get(URL_UPPSLA)
driver.implicitly_wait(2)

errorPanel = driver.find_elements(By.CLASS_NAME, "feedbackPanelERROR")
dateLine = driver.find_element(By.CLASS_NAME, "fc-day-header")
if len(errorPanel) > 0:
    print("No dates found for Uppsala")
else:
    print("Date found to be {0}".format(dateLine.text))

driver.quit()
