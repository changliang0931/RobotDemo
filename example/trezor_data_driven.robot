*** Settings ***
Documentation     Example test cases using trezorcli.
...
...               Testing *Trezor* business logic.
Test Template     TrezorRobot
Library           TrezorRobotLibrary.py

*** Test Cases ***    Coin    Path     Address    tags 
Get Address          eth    44'/60'/0'/0/0    0x4213C85B259D95a3BeA639b3668604847F03283A    
                     btc    44'/0'/0'/0/0    1NyK66tHd9RnWZzQWnq5A6QEo2e8LH8zxW

*** Keywords ***
TrezorRobot
    [Arguments]    ${Coin}    ${Path}     ${Address}
    Get Address    ${Coin}    ${Path}     ${Address}