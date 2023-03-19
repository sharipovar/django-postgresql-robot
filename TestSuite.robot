*** Settings ***
Documentation  API Testing in Robot Framework
Library  SeleniumLibrary
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library  Process
Suite Setup  Start the webserver
Suite Teardown  Stop the webserver

*** Keywords ***
Start the webserver
    ${django process}=  Start Process  python  manage.py  runserver
    Set suite variable  ${django process}

Stop the webserver
    Terminate Process  ${django process}

*** Test Cases ***
Quick Get Request Test
    ${response}=    GET  https://www.google.com
Quick Get A JSON Body Test
    ${response}=    GET  https://jsonplaceholder.typicode.com/posts/1
    Should Be Equal As Strings    1  ${response.json()}[id]
Запрос к /user/1 должен вернуть user_name равное 'A'
    ${response}=    GET  http://127.0.0.1:8000/blog/user/1
    Should Be Equal As Strings    A  ${response.json()}[user_name]
Запрос к /user/2 должен вернуть user_name равное 'B'
    ${response}=    GET  http://127.0.0.1:8000/blog/user/2
    Should Be Equal As Strings    B  ${response.json()}[user_name] 
Запрос к /topic/2 должен вернуть topic_name равное 'bb'
    ${response}=    GET  http://127.0.0.1:8000/blog/topic/2
    Should Be Equal As Strings    bb  ${response.json()}[topic_name]
Запрос к /message/3 должен вернуть text равное 'text 1 B - aa'
    ${response}=    GET  http://127.0.0.1:8000/blog/message/3
    Should Be Equal As Strings    text 1 B - aa  ${response.json()}[text]
Запрос к /message/3 должен вернуть topic равное '1 aa'
    ${response}=    GET  http://127.0.0.1:8000/blog/message/3
    Should Be Equal As Strings    1 aa   ${response.json()}[topic] 
 Запрос к /message/8 должен вернуть text равное 'test'
    ${response}=    GET  http://127.0.0.1:8000/blog/message/8
    Should Be Equal As Strings    test  ${response.json()}[text]    