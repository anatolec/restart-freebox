from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller


def restart_freebox(password, url='http://mafreebox.freebox.fr/login.php', headless=True, test=False):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1280")

    if headless:
        chrome_options.add_argument('headless')

    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "password_"))).send_keys(password+Keys.RETURN)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Menu démarrer']"))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Redémarrer')]"))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, f'button-{1006 + test}'))).click()
        print('Freebox Restarted')
    finally:
        driver.quit()
