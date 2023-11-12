from browser import Browser
from pages.base_page import BasePage
from pages.contact_page import ContactPage
from pages.programari_page import ProgramariPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.contact_page = ContactPage()
    context.programari_page = ProgramariPage()



def after_all(context):
    context.browser.close()