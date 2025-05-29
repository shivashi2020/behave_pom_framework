# 🧪 Behave BDD Automation Framework (Python + Selenium)

This project is a plug-and-play automation framework built using **Python**, **Behave (BDD)**, **Selenium**, and the **Page Object Model** design pattern. It supports **Allure reporting**, environment configuration via `.env` files, and modular test execution.

---

## 🚀 Features

- 🧱 **Page Object Model (POM)** design for maintainability
- ✅ **BDD with Behave**: Cucumber-style syntax using Gherkin
- 🌍 **Cross-browser testing** (via WebDriver)
- 🔐 **Environment variable support** using `.env` and `python-dotenv`
- 📊 **Allure reporting** with screenshots on failure
- 🧪 Modular test step definitions
- 🔁 CI/CD-friendly structure

---

## 📁 Project Structure

project-root/
│
├── features/
│ ├── steps/ # Step definitions
│ ├── pages/ # Page Object classes
│ ├── environment.py # Hooks for setup/teardown
│ └── *.feature # Feature files (Gherkin)
│
├── reports/ # Allure results and screenshots
├── .env # Secret credentials (excluded from Git)
├── requirements.txt
└── README.md


---

## 🧪 How to Run

### 📦 1. Install Dependencies
pip install -r requirements.txt
### ⚙️ 2. Set Up Environment Variables
Create a .env file in the root:
USERNAME=your_username
PASSWORD=your_password
APP_URL=https://demowebshop.tricentis.com
USE_ENV=True
### ▶️ 3. Run Tests
behave
behave -D keep_browser=True -f allure_behave.formatter:AllureFormatter -o reports/allure-results
### 📊 4. Generate Allure Report
allure serve reports/allure-results
### 🔐 Environment Management
The USE_ENV flag in .env controls whether credentials are taken from .env or from the .feature file.
All sensitive data should be stored in .env.
### 📷 Screenshots on Failure
Screenshots are captured on test failures and stored in reports/. They are automatically attached to Allure reports.
