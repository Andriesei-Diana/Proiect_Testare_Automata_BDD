from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPage(BasePage):

    CONTACT_PAGE_URL = 'https://teodent.ro/contact'

    INPUT_NUME = (By.ID, 'last_name')
    INPUT_PRENUME = (By.ID, 'first_name')
    INPUT_ADRESA_DE_EMAIL = (By.ID, 'email')
    INPUT_TELEFON = (By.ID, 'phone')
    INPUT_MESAJ = (By.ID, 'message')

    BUTTON_TRIMITE = (By.CSS_SELECTOR, 'button[type="submit"]')

    BUTTON_TERMENI_SI_CONDITII = (By.XPATH, "//button[@type='button' and @role='switch']")
    ERROR_MESSAGE_NUME = (By.XPATH, '//p[contains(text(), "Campul Prenume este obligatoriu.")]')
    EMAIL_OBLIGATORIU_ERROR = (By.XPATH, '//form/div[2]/div[3]/p')
    ERROR_MESSAGE_TERMS_AND_CONDITIONS_CHECK = (By.XPATH,
                                                '//p[contains(text(),"Va rugam sa confirmati ca ati citit termenii si conditiile de utilizare ale site-ului si sunteti de acord")]')
    SUCCES_MESSAGE = (By.XPATH, '//h1')

    # Function that opens the page "Contact"
    def open(self):
        self.driver.get(self.CONTACT_PAGE_URL)

    # Function that completes the name in the input "Nume"
    def set_nume(self, nume_text):
        self.type(self.INPUT_NUME, nume_text)

    # Function that completes the first name in the input "Prenume"
    def set_prenume(self, prenume_text):
        self.type(self.INPUT_PRENUME, prenume_text)

    # Function that completes the email address in the input field
    def set_adresa_email(self, email_text):
        self.type(self.INPUT_ADRESA_DE_EMAIL, email_text)

    # Function that completes the phone number in the input field
    def set_telefon(self, telefon_text):
        self.type(self.INPUT_TELEFON, telefon_text)

    # Function that completes a message in the "mesaj" field
    def set_mesaj(self, mesaj_text):
        self.type(self.INPUT_MESAJ, mesaj_text)

    # Function that ticks the terms and conditions button
    def check_terms_and_conditions_checkbox(self):
        self.check_button_terms(self.BUTTON_TERMENI_SI_CONDITII)

    # Function that presses once the send button of the page
    def click_trimite_button(self):
        self.click(self.BUTTON_TRIMITE)

    # Function that presses twice the send button of the page
    def double_click_on_trimite_button(self):
        self.double_click(self.BUTTON_TRIMITE)

    # Function that displays the error message: "Campul Prenume este obligatoriu."
    def is_error_message_nume_displayed(self):
        return self.find(self.ERROR_MESSAGE_NUME).is_displayed()

    # Function that displays the message of successful sending of contact
    def is_succes_message_displayed(self):
        return self.find(self.SUCCES_MESSAGE).is_displayed()

    # Function that displays the error message: "Campul Email trebuie sa contina o adresa de email valida."
    def is_error_required_valid_email_displayed(self):
        return self.find(self.EMAIL_OBLIGATORIU_ERROR).is_displayed()

    # Function that displays the error message: "Va rugam sa confirmati ca ati citit termenii si conditiile de utilizare ale site-ului si sunteti de acord"
    def is_error_message_terms_and_conditions_check_displayed(self):
        return self.find(self.ERROR_MESSAGE_TERMS_AND_CONDITIONS_CHECK).is_displayed()
