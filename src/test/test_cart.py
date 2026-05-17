from src.utils.utils import *

def test_de_agregar_producto():
    driver = setup_driver_inventory()

    inventory_item = driver.find_element(By.CLASS_NAME, "inventory_item")
    inventory_item.find_element(By.ID,
                                "add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.ID, "remove-sauce-labs-backpack").is_displayed(), "No se pudo agregar el producto"

    driver.quit()

def test_de_contador_de_productos():
    driver = setup_driver_inventory()

    inventory_item = driver.find_element(By.CLASS_NAME, "inventory_item")
    inventory_item.find_element(By.ID,
                                "add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.CLASS_NAME,
                                       "shopping_cart_badge").text == "1", "El contador del carrito no incremento"

    driver.quit()

def test_de_navegar_al_carrito_de_compras():
    driver = setup_driver_inventory()

    inventory_item = driver.find_element(By.CLASS_NAME, "inventory_item")
    inventory_item.find_element(By.ID,
                                "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert driver.find_element(By.CLASS_NAME,
                               "title").text == "Your Cart", "The title is not correct"


def test_de_verificar_el_producto_en_el_carrito_de_compras():
    driver = setup_driver_inventory()

    inventory_item = driver.find_element(By.CLASS_NAME, "inventory_item")
    inventory_item.find_element(By.ID,
                                "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
    assert cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack", "The item does not exist in the cart"