Feature: Create User

    Scenario: Create User and Login
        Given I fill out all the required fields

        And I am redirected to login

        Then The user is found in the database


    Scenario: Test Duplicate User doesn't work
        Given I empty the "User" table

        And I create the following users:
            | id | email          | username | password |
            | 1  | test@gmail.com | test     | PSWD12*  |

        When I create a user with the same username

        Then An exception is not raised


    Scenario: Test invalid email
        Given I submit an invalid email

        Then No user is created


    Scenario: Test field required
        Given I omit first name

        Then No user is created
