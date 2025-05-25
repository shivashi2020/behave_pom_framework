# features/login.feature
Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When the user logs in with username "myuser" and password "mypassword"
    Then I should be redirected to the dashboard
    And the user logs out


