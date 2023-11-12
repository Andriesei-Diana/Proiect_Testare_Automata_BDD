from behave import *


@given("I am on the 'Contact' page")
def step_impl(context):
    context.contact_page.open()


# Scenario: Send message without data
@when('I click on the "Trimite" button')
def step_impl(context):
    context.contact_page.click_trimite_button()


@when('I double click on the "Trimite" button')
def step_impl(context):
    context.contact_page.double_click_on_trimite_button()


@then('I should see "{message}" error name message')
def step_impl(context, message):
    context.contact_page.is_error_message_nume_displayed(), (
        "The error message does not contain the expected text")


@when('I enter "{nume_text}" as name')
def step_impl(context, nume_text):
    context.contact_page.set_nume(nume_text)


@when('I enter "{prenume_text}" as last name')
def step_impl(context, prenume_text):
    context.contact_page.set_prenume(prenume_text)


@when('I enter "{email_text}" as email')
def step_impl(context, email_text):
    context.contact_page.set_adresa_email(email_text)


@when('I enter "{phone_text}" as phone number')
def step_impl(context, phone_text):
    context.contact_page.set_telefon(phone_text)


@when('I enter "{mesaj_text}" as message')
def step_impl(context, mesaj_text):
    context.contact_page.set_mesaj(mesaj_text)


@when('I mark the terms condition as checked')
def step_impl(context):
    context.contact_page.check_terms_and_conditions_checkbox()


@then('I should see "Va multumim pentru mesaj."')
def step_impl(context):
    context.contact_page.is_succes_message_displayed()


@when('I enter an invalid email "{email_text}" as data')
def step_impl(context, email_text):
    context.contact_page.set_adresa_email(email_text)


@then('I should see "Campul Email trebuie sa contina o adresa de email valida."')
def step_impl(context):
    context.contact_page.is_error_required_valid_email_displayed()


@then(
    'I should see "Va rugam sa confirmati ca ati citit termenii si conditiile de utilizare ale site-ului si sunteti de acord" message')
def step_impl(context):
    context.contact_page.is_error_message_terms_and_conditions_check_displayed()


@then('The URL of the page is the same as "{url}"')
def step_impl(context, url):
    context.contact_page.is_url_correct(url), "The login page url is incorrect."
