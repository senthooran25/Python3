*** Settings ***
Documentation  This is testing scrip
Library  Selenium2Library
Library  SeleniumLibrary

*** Variables ***
$[BROWER] chrome

*** Test Cases ***
Open Browser  https://www.google.com/ Safari

