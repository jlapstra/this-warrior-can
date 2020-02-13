Feature: Login

    Scenario: Simple Login Page
        Given I access the url "/"
        Then I am redirected to the login page


    Scenario: A user can log into app
        Given I empty the "User" table

        And I create the following users:
            | id | email          | username | password |
            | 1  | test@gmail.com | test     | PSWD12*  |

        When I log in with username "test" and password "PSWD12*"

        Then I am logged in
