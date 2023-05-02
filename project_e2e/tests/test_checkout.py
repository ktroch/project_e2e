import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from utils.config import Config

class TestCheckout(unittest.TestCase):

    def setUp(self):
        # Inicia el navegador
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(Config.BASE_URL)

    def test_checkout(self):
        # Crea una instancia de la página de inicio de sesión y realiza el inicio de sesión
        login_page = LoginPage(self.driver)
        login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

        # Verifica que el usuario ha iniciado sesión correctamente
        inventory_page = InventoryPage(self.driver)
        self.assertIn(Config.HOME_PAGE_TITLE, self.driver.title)

        # Agrega un producto al carrito
        inventory_page.add_product_to_cart(0)

        # Visualiza el carrito y va a la página de checkout
        cart_page = CartPage(self.driver)
        cart_page.view_cart()
        cart_page.go_to_checkout()

        # Completa el formulario de compra
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_form(Config.FIRST_NAME, Config.LAST_NAME, Config.ZIP_CODE)

        # Finaliza la compra hasta la confirmación
        confirmation_page = ConfirmationPage(self.driver)
        confirmation_page.finish_checkout()

        # Verifica que se haya completado la compra correctamente
        self.assertIn(Config.CONFIRMATION_PAGE_TITLE, self.driver.title)

    def tearDown(self):
        # Cierra el navegador al finalizar la prueba
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
