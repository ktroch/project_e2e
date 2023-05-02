from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    # Localizadores
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def __init__(self, driver):
        self.driver = driver

    def enter_personal_information(self, first_name, last_name, zip_code):
        # Ingresa la información personal en el formulario
        first_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        first_name_input.send_keys(first_name)

        last_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        last_name_input.send_keys(last_name)

        zip_code_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ZIP_CODE_INPUT))
        zip_code_input.send_keys(zip_code)

    def proceed_to_checkout_overview(self):
        # Hace clic en el botón de "Continue"
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_button.click()
