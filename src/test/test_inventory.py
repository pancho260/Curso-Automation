from src.test.utils import *

def test_de_validar_titulo_del_inventario():
    driver = setup_driver_inventory()

    assert driver.find_element(By.CLASS_NAME,
                               "title").text == "Products", "The title is not correct"

    driver.quit()

def test_de_validar_productos():
    driver = setup_driver_inventory()

    assert len(driver.find_elements(By.CLASS_NAME,
                                    "inventory_item")) > 0, "There are no products on screen"

    driver.quit()

def test_de_validar_interfaz():
    driver = setup_driver_inventory()

    assert driver.find_element(By.ID,
                               "react-burger-menu-btn").is_displayed(), "The menu button is not displayed"
    assert driver.find_element(By.CLASS_NAME,
                               "product_sort_container").is_displayed(), "The filters are not displayed"
    assert driver.find_element(By.CLASS_NAME,
                               "shopping_cart_link").is_displayed(), "The cart button is not displayed"

    driver.quit()


def test_de_validar_el_primer_producto():
    driver = setup_driver_inventory()

    inventory_item = driver.find_element(By.CLASS_NAME, "inventory_item")
    assert inventory_item.find_element(By.CLASS_NAME,
                                       "inventory_item_name").text == "Sauce Labs Backpack", "El nombre del producto no es correcto"
    assert inventory_item.find_element(By.CLASS_NAME,
                                       "inventory_item_price").text == "$29.99", "El precio del producto no es correcto"

    driver.quit()