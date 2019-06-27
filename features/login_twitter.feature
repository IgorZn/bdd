Feature: Login into twitter

    Allow valid users
    To login on twitter
    To be able to use the plataform

  @sunny @smoke @sanity
    Scenario: Valid login
        Given Open "http://twitter.com/"
        When send login "5000700@mail.ru", password "AdminGuru" and log in
        Then the user should be redirected to homepage