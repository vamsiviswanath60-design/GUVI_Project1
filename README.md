# Automation Testing of EdTech Platform Web Application

## Project Title
Automated Testing of the Web Application https://www.guvi.in

## Project Objective
The objective of this project is to automate the testing of the GUVI web application using Selenium with Python and Pytest. The framework validates key UI functionalities including page navigation, login, logout, menu validation, chatbot verification, and other core features.

## Tools & Technologies
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Report
- WebDriver Manager
- Chrome Browser
- Visual Studio Code

## Framework
- Page Object Model (POM)
- Object-Oriented Programming (OOP)

## Project Structure

```
project_1_EdTech Platform/
│
├── pages/
│   ├── base_page.py
│   └── guvi_home_page.py
│
├── testcases/
│   └── test_home_page.py
│
├── utilities/
│   ├── config.py
│   └── driver_factory.py
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Cases

- TC-01 Verify Home Page URL
- TC-02 Verify Home Page Title
- TC-03 Verify Login Button
- TC-04 Verify Sign Up Button
- TC-05 Verify Sign Up Page Navigation
- TC-06 Verify Login with Valid Credentials
- TC-07 Verify Login with Invalid Credentials
- TC-08 Verify Navigation Menu Items
- TC-09 Verify Dobby GUVI Assistant
- TC-10 Verify Logout Functionality

## Features
- Selenium Automation Framework
- Page Object Model (POM)
- Explicit Waits
- Implicit Wait
- HTML Test Reports
- Driver Factory Design
- Reusable Page Methods
- Object-Oriented Programming

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Execute the Test Suite

```bash
python -m pytest testcases/test_home_page.py --html=reports/report.html --self-contained-html
```

## Test Report

The HTML report is generated inside the **reports** folder after test execution.

## Author

Vamsi Viswanath (vamsiviswanath9@gmail.com)