import unittest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from utils.config import Config

class TestConfirmation(unittest.TestCase):

    def test_confirmation(self):
        # Inicia el navegador
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(Config.BASE_URL)

        # Crea una instancia de la página de inicio de sesión y realiza el inicio de sesión
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

        # Verifica que el usuario ha iniciado sesión correctamente
        inventory_page = InventoryPage(driver)
        self.assertIn(Config.HOME_PAGE_TITLE, driver.title)

        # Agrega un producto al carrito
        inventory_page.add_product_to_cart(0)

        # Visualiza el carrito y va a la página de checkout
        cart_page = CartPage(driver)
        cart_page.view_cart()
        cart_page.go_to_checkout()

        # Completa el formulario de compra
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form(Config.FIRST_NAME, Config.LAST_NAME, Config.ZIP_CODE)

        # Finaliza la compra hasta la confirmación
        confirmation_page = ConfirmationPage(driver)
        confirmation_page.finish_checkout()

        # Verifica que se haya completado la compra correctamente
        self.assertIn(Config.CONFIRMATION_PAGE_TITLE, driver.title)

        # Cierra el navegador al finalizar la prueba
        driver.quit()

if __name__ == '__main__':
    unittest.main()
