Feature: Create User

    Scenario: Create User and Login
        Given I fill out all the required fields

        And I am redirected to login

        Then The user is found in the database

