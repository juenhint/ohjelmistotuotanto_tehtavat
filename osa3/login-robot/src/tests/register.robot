*** Settings ***
Resource  resource.robot
test setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  vi  ville123
    Output Should Contain  Username must be at least 3 characters long

Register With Sufficiently Long But Invalid Username And Valid Password
    Input Credentials  VIlle  ville123
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  ville  ville1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  villepassword
    Output Should Contain  Password must contain at least one non-letter character

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command