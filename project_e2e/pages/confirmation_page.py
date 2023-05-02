from selenium.webdriver.common.by import By

class ConfirmationPage:

    # Localizadores
    THANK_YOU_MESSAGE = (By.XPATH, '//h2[text()="THANK YOU FOR YOUR ORDER"]')

    def __init__(self, driver):
        self.driver = driver

    def is_confirmation_page_displayed(self):
        # Verifica si se muestra la página de confirmación
        thank_you_message = self.driver.find_element(*self.THANK_YOU_MESSAGE)
        return thank_you_message.is_displayed()
