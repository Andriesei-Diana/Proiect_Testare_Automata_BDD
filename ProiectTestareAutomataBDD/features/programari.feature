Feature: Programeaza-te Page

  Background: I am on the 'Programeaza-te' page
    Given I am on the 'Programeaza-te' page

  Scenario: The user submits an appointment using valid data
    When I enter "Ionescu Paul" as a complete name
    When I enter as a email "ionescu.paul@example.com"
    When I enter "0742255230" as a phone number
    When I enter "Ortodontie/Elena Miron" as a programming details
    When I mark the terms conditions as checked in Programeaza-te page
    When I click on the button "Trimite"
    Then I should see "Va multumim pentru mesaj." message


  Scenario: The user sends a schedule without filling in the data fields
    When I click on the button "Trimite"
    Then It should appear the message "Campul nume este obligatoriu."


  Scenario: The user is using an invalid email address
    When I enter as a email "alabalaportocala"
    When I click on the button "Trimite"
    Then I will see displayed the message: "Campul email trebuie sa contina o adresa de email valida."


   Scenario: Check that the URL is correct
    Then The URL of the page is "https://teodent.ro/programari"

