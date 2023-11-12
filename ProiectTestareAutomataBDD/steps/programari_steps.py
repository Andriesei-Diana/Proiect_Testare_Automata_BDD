from behave import *


@given("I am on the 'Programeaza-te' page")
def step_impl(context):
    context.programari_page.open()


@when('I enter "{text_numele_dumneavoastra}" as a complete name')
def step_impl(context, text_numele_dumneavoastra):
    context.programari_page.set_numele_dumneavoastra(text_numele_dumneavoastra)


@when('I enter as a email "{text_email}"')
def step_impl(context, text_email):
    context.programari_page.set_adresa_email_valida(text_email)


@when('I enter "{phone_number}" as a phone number')
def step_impl(context, phone_number):
    context.programari_page.set_telefon(phone_number)


@when('I enter "{programming_detalis}" as a programming details')
def step_impl(context, programming_detalis):
    context.programari_page.set_detalii_programare(programming_detalis)


@when('I mark the terms conditions as checked in Programeaza-te page')
def step_impl(context):
    context.programari_page.check_terms_and_condition_checkbox()


@when('I click on the button "Trimite"')
def step_impl(context):
    context.programari_page.click_trimite_button()


@then('I should see "Va multumim pentru mesaj." message')
def step_impl(context):
    context.programari_page.is_succes_message_displayed()


@then('It should appear the message "Campul nume este obligatoriu."')
def step_impl(context):
    context.programari_page.is_error_message_name_mandatory_displayed()


@then('I will see displayed the message: "Campul email trebuie sa contina o adresa de email valida."')
def step_impl(context):
    context.programari_page.is_error_valid_email_message_required()


@then('I should see displayed the message "Campul detalii programare este obligatoriu."')
def step_impl(context):
    context.programari_page.is_error_programming_details_mandatory_message_displayed()


@then('The URL of the page is "{url}"')
def step_impl(context, url):
    context.programari_page.is_url_correct(url), "The login page url is incorrect."
