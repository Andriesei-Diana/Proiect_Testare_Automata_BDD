from selenium.webdriver import ActionChains

from browser import Browser


class BasePage(Browser):
    # Functie care cauta si returneaza un Web Element dupa un locator dat
    def find(self, locator):
        return self.driver.find_element(*locator)

    # Functie care cauta si returneaza o lista cu Web Elements dupa un locator dat (sub forma de tuplu)
    # Daca nu gaseste nimic, va returna o lista goala
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    # Functie care face click pe un Web Element
    def click(self, locator):
        # self.driver.find_element(*locator).click()
        self.find(locator).click()

    def double_click(self, locator):
        element = self.find(locator)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(element).perform()

    # Functie care scrie pe un Web Element
    # Primeste 2 parametri:
    # locator - locatorul elementului pe care se va scrie (sub forma de tuplu)
    # text - textul care urmeaza a fi scris
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    # Functie care returneaza textul de pe un Web Element
    # Primeste 1 parametru:
    # locator - locatorul elementului de pe care va returna textul
    def get_text(self, locator):
        return self.find(locator).text

    # va returna True daca URL-ul paginii curente este egal cu
    # URL-ul paginii din care apelam metoda
    def is_url_correct(self, url):
        return self.driver.current_url == url

    # Functie care selecteaza (bifeaza) un checkbox
    def check_button_terms(self, locator):
        button_terms = self.find(locator)

        # daca checkbox-ul NU este selectat (bifat), va da click pe el
        if not button_terms.is_enabled():
            self.click(button_terms)

    # Functie care deselecteaza (debifeaza) un checkbox
    def uncheck_checkbox(self, locator):
        checkbox = self.find(locator)

        # daca checkbox-ul este selectat (bifat), va da click pe el
        if checkbox.is_selected():
            self.click(checkbox)
