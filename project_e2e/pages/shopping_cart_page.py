from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    # Localizadores
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # Introduce el nombre de usuario
        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        username_input.clear()
        username_input.send_keys(username)

        # Introduce la contraseña
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        # Hace clic en el botón de inicio de sesión
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
