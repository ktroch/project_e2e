import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import Config

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Inicia el navegador
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(Config.BASE_URL)

    def test_login_valid_user(self):
        # Crea una instancia de la página de inicio de sesión y realiza el inicio de sesión
        login_page = LoginPage(self.driver)
        login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

        # Verifica que el usuario ha iniciado sesión correctamente
        self.assertIn(Config.HOME_PAGE_TITLE, self.driver.title)

    def test_login_invalid_user(self):
        # Crea una instancia de la página de inicio de sesión y realiza el inicio de sesión con credenciales inválidas
        login_page = LoginPage(self.driver)
        login_page.login(Config.INVALID_USER, Config.INVALID_PASSWORD)

        # Verifica que el mensaje de error de inicio de sesión es correcto
        error_message = login_page.get_error_message()
        self.assertEqual(error_message, Config.INVALID_CREDENTIALS_ERROR_MESSAGE)

    def tearDown(self):
        # Cierra el navegador al finalizar la prueba
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
