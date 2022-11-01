*** Settings ***
Library           DataDriver    file=DataDriven.xls    sheet_name=2nd Sheet
Documentation     Example test cases using trezorcli.
...
...               Testing *Trezor* business logic.
Test Template     TrezorRobot
Library           TrezorRobotLibrary.py

*** Test Cases ***    
Get Address     ${Coin}    ${Path}     ${Address}     

*** Keywords ***
TrezorRobot
    [Arguments]    ${Coin}    ${Path}     ${Address}
    [Tags]    address
    Get Address    ${Coin}    ${Path}     ${Address}