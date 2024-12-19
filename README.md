# Formulatrix QA Automation Test
This repository contains automation scripts for testing the functionality of the DemoBlaze Website. The scripts are written using Selenium WebDriver in Python and are designed to validate key functionalities such as login, add-to-cart, cart verification, and logout.


## 📋 Project Overview
The automation scripts in this project perform the following tasks:
- 🔑 Login Test: Verify that a user can log in with valid credentials.
- 🛒 Add to Cart Test: Validate the "Add to Cart" feature.
- 📦 Cart Verification: Ensure added products appear correctly in the cart.
- 🚪 Logout Test: Verify that a user can log out successfully.

## These scripts are designed to be:
- ✅ Simple: Easy to use and understand.
- 🚀 Efficient: Perform tests quickly and reliably.
- 🔄 Extendable: Easy to add new test cases or modify existing ones.
- 🛠 Prerequisites

## To run the scripts, ensure you have the following installed:

- Python 3.7 or above
- Google Chrome (latest version)
- ChromeDriver (matching your Chrome browser version)
- Selenium
- pytest (for test execution and reporting)

## ⚙️ Setup and Installation
### 1️⃣ Clone this repository:
- bash
- Copy code
- git clone https://github.com/yourusername/formulatrix-qa-test.git
- cd formulatrix-qa-test

### 2️⃣ Install dependencies:
Ensure pip is installed, then run:
- bash
- Copy code

The requirements file includes:
- selenium
- pytest

### 3️⃣ Download ChromeDriver:
- Visit ChromeDriver Downloads.
- Download the version matching your Chrome browser.
- Add the chromedriver.exe file to your system’s PATH or specify its location in the scripts.
- 🚀 Running the Tests

To run the tests, navigate to the project directory in the terminal and execute:
- bash
- Copy code
- pytest test_demoblaze.py

## 📄 Test results will be displayed directly in the terminal.
## 📊 Test Scenarios
- 🔑 Login =	Verify that a user can log in with valid credentials.
- 🛒 Add to Cart =	Test that products can be added to the shopping cart.
- 📦 Cart = Check	Ensure added products appear correctly in the cart.
- 🚪 Logout =	Test that a user can log out successfully.


## 📁 File Structure
- bash
- Copy code
- formulatrix-qa-test/
├── test_demoblaze.py         # Main test script
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation

## 🔧 How to Modify or Extend the Tests
Add new test cases:
Create a new function in test_demoblaze.py using the pytest framework.
Example:
- python
- Copy code
- def test_example():
    assert True
- Add new dependencies:

Update requirements.txt with the new library name.
Run:
- bash
- Copy code
- pip install -r requirements.txt

Commit changes to the repository:
- bash
- Copy code
- git add .
- git commit -m "Added new test cases"
- git push origin main
- 🐞 Common Issues and Troubleshooting


## Issue	Solution
- ❌ chromedriver not found	Ensure chromedriver.exe is in PATH or specify its location in the script.
- ❌ Login test fails	Verify the username and password are correct in the script.
- ❌ Python not recognized as a command	Ensure Python is installed and added to PATH.
- ❌ ModuleNotFoundError: selenium	Run pip install selenium to install the Selenium library.

## 🤝 Contributing
Contributions are welcome!
Please fork the repository, create a feature branch, and submit a pull request.
Ensure all new features are tested before submission.

## 👤 Author
Name: Yori Fiandika
Email: yfiandika@gmail.com
GitHub: ygustam

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
