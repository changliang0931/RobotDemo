*** Settings ***
Documentation     Example test cases using trezorcli.
...
...               Testing *Trezor* business logic.
Library           TrezorRobotLibrary.py

*** Test Cases ***
Get Address By Coin And Path
    [Tags]    address
    Get Address    eth    44'/60'/0'/0/0    0x4213C85B259D95a3BeA639b3668604847F03283A 
    Get Address    btc    44'/0'/0'/0/0    1NyK66tHd9RnWZzQWnq5A6QEo2e8LH8zxW


