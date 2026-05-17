from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(), options=options)
        driver.implicitly_wait(5)
        return driver
    except Exception as e:
        print(f"\nError al inicializar el driver: {e}")
        raise

def setup_driver_inventory():
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com")

        username_input = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        return driver
    except Exception as e:
        print(f"\nError al loguear al sitio: {e}")
        raise
