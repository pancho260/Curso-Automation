from src.test.utils import *

def test_de_validar_titulo_del_formulario():
    driver = setup_driver()
    driver.get("https://www.saucedemo.com")

    assert driver.title == "Swag Labs", "The title is not correct"

    driver.quit()

def test_de_carga_del_formulario():
    driver = setup_driver()
    driver.get("https://www.saucedemo.com")

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    assert username_input.is_displayed(), "The login form did not load"

    driver.quit()

def test_de_login():
    driver = setup_driver()
    driver.get("https://www.saucedemo.com")

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_input.send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    assert (driver.current_url ==
            "https://www.saucedemo.com/inventory.html"), "Did not arrive at the inventory page"
    assert driver.find_element(By.XPATH,
                               "//span[@class='title']").text == "Products", "The title is not correct"

    driver.quit()


