from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProgramariPage(BasePage):
    PROGRAMARI_PAGE_URL = 'https://teodent.ro/programari'

    INPUT_NUMELE_DUMNEAVOASTRA = (By.ID, 'name')
    INPUT_ADRESA_EMAIL_VALIDA = (By.ID, 'email')
    INPUT_TELEFON = (By.ID, 'phone')
    INPUT_DETALII_PROGRAMARE = (By.ID, 'details')

    BUTTON_TRIMITE = (By.CSS_SELECTOR, 'button[type="submit"]')

    TERMENI_SI_CONDITII_BUTTON = (By.XPATH, "//button[@type='button' and @role='switch']")
    SUCCES_MESSAGE = (By.XPATH, '//h1')
    ERROR_MESSAGE_NAME_MANDATORY = (By.XPATH, '//p[contains(text(),"Campul nume este obligatoriu.")]')
    ERROR_VALID_EMAIL_REQUIRED_MESSAGE = (
        By.XPATH, '//p[contains(text(),"Campul email trebuie sa contina o adresa de email valida.")]')
    ERROR_MESSAGE_PROGRAMMING_DETAILS_MANDATORY = (
        By.XPATH, '//p[contains(text(),"Campul detalii programare este obligatoriu.")]')

    # Function that opens the page "Programeaza-te"
    def open(self):
        self.driver.get(self.PROGRAMARI_PAGE_URL)

    # Function that completes the name in the input "numele dumneavoastra"
    def set_numele_dumneavoastra(self, nume_text):
        self.type(self.INPUT_NUMELE_DUMNEAVOASTRA, nume_text)

    # Function that completes the email address in the input field
    def set_adresa_email_valida(self, email_text):
        self.type(self.INPUT_ADRESA_EMAIL_VALIDA, email_text)

    # Function that completes the phone number in the input field
    def set_telefon(self, nume_text):
        self.type(self.INPUT_TELEFON, nume_text)

    # Function that completes the programming details in the input
    def set_detalii_programare(self, nume_text):
        self.type(self.INPUT_DETALII_PROGRAMARE, nume_text)

    # Function that ticks the terms and conditions button
    def check_terms_and_condition_checkbox(self):
        self.check_button_terms(self.TERMENI_SI_CONDITII_BUTTON)

    # Function that presses once the send button of the page
    def click_trimite_button(self):
        self.click(self.BUTTON_TRIMITE)

    # Function that displays the message of successful sending of the appointment
    def is_succes_message_displayed(self):
        return self.find(self.SUCCES_MESSAGE).is_displayed()

    # Function that displays the error message: "Campul nume este obligatoriu."
    def is_error_message_name_mandatory_displayed(self):
        return self.find(self.ERROR_MESSAGE_NAME_MANDATORY).is_displayed()

    # Function that displays the error message: "Campul detalii programare este obligatoriu."
    def is_error_programming_details_mandatory_message_displayed(self):
        return self.find(self.ERROR_MESSAGE_PROGRAMMING_DETAILS_MANDATORY).is_displayed()

    # Function that displays the error message: "Campul email trebuie sa contina o adresa de email valida."
    def is_error_valid_email_message_required(self):
        return self.find(self.ERROR_VALID_EMAIL_REQUIRED_MESSAGE).is_displayed()
