Feature: Contact Page

  Background: I am on the 'Contact' page
    Given  I am on the 'Contact' page


  Scenario: User submits an empty form contact
    When I click on the "Trimite" button
    Then I should see "Campul Prenume este obligatoriu." error name message


  Scenario: User submits a complete and valid form contact
    When I enter "Popescu" as name
    When I enter "Ion" as last name
    When I enter "popescu.ion@example.com" as email
    When I enter "0743323390" as phone number
    When I enter "Doctorul Mircea Ion va fi la cabinet maine?" as message
    When I mark the terms condition as checked
    When I click on the "Trimite" button
    Then I should see "Va multumim pentru mesaj."


  Scenario: Check if the invalid email error message is displayed
    When I enter an invalid email "popesc965%xample.com" as data
    When I click on the "Trimite" button
    Then I should see "Campul Email trebuie sa contina o adresa de email valida."


  Scenario: User cannot submits the form contact without accepting terms
    When I enter "Popescu" as name
    When I enter "Ion" as last name
    When I enter "popescu.ion@example.com" as email
    When I enter "0743323390" as phone number
    When I enter "Doctorul Mircea Ion va fi la cabinet maine?" as message
    When I double click on the "Trimite" button
    Then I should see "Va rugam sa confirmati ca ati citit termenii si conditiile de utilizare ale site-ului si sunteti de acord" message

  Scenario: Check that the contact form is submitted with valid mandatory data
    When I enter "Popescu" as name
    When I enter "Ion" as last name
    When I enter "popescu.ion@example.com" as email
    When I enter "Doctorul Mircea Ion va fi la cabinet maine?" as message
    When I double click on the "Trimite" button
    Then I should see "Va multumim pentru mesaj."

  Scenario: The user can send the contact form with invalid name, surname, phone number
    When I enter "564892" as name
    When I enter "36598" as last name
    When I enter "popescu.ion@example.com" as email
    When I enter "abcdefghse" as phone number
    When I enter "Doctorul Mircea Ion va fi la cabinet maine?" as message
    When I mark the terms condition as checked
    When I click on the "Trimite" button
    Then I should see "Va multumim pentru mesaj."

  Scenario: Check that the URL is correct
    Then The URL of the page is the same as "https://teodent.ro/contact"

