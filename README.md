# StoreFramework

## Overview

This repository contains a Python-based framework for automating store-related functionalities using Selenium. While no initial description was provided, this README aims to provide comprehensive information about the project based on the existing file structure and code snippets. The framework focuses on end-to-end testing, particularly around login, product selection, and checkout processes.

## Key Features & Benefits

*   **Page Object Model:** Utilizes the Page Object Model for better code organization, maintainability, and reusability.
*   **End-to-End Testing:**  Designed for performing complete end-to-end tests of a store application.
*   **Selenium WebDriver:** Leverages Selenium WebDriver for browser automation.
*   **pytest Framework:** Uses pytest for test discovery, execution, and reporting.
*   **Browser Utility Class:** Includes a `BrowserUtils` class for common browser-related tasks.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Python 3.6 or higher is required.
*   **pip:** Python package installer.
*   **Selenium:** Install using `pip install selenium`.
*   **pytest:** Install using `pip install pytest`.
*   **pytest-html:** (Optional) Install using `pip install pytest-html` to generate HTML reports.
*   **Web Browser:** A compatible web browser (e.g., Chrome, Firefox) and its corresponding WebDriver.

## Installation & Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/uditSINGH43/StoreFramework.git
    cd StoreFramework
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install selenium pytest pytest-html
    ```

4.  **Download Webdriver:**

    Download the WebDriver for your chosen browser (e.g., ChromeDriver for Chrome) and ensure it's in your system's PATH or specify its location in your test scripts. You can usually download these from the browser vendor's website.

## Usage Examples & API Documentation

This framework provides a set of page objects and test scripts for automating store-related tasks. Here's a basic overview of how to use it:

1.  **Page Objects:**

    *   `pageObjects/login.py`: Handles login functionality.
        ```python
        from selenium.webdriver.common.by import By

        from pageObjects.CartPage import ShopPage
        from utils.browserUtils import BrowserUtils


        class LoginPage(BrowserUtils):
            def __init__(self, driver):
                super().__init__(driver)
                self.driver = driver
                self.username_input = (By.ID, "username")
                self.password = (By.ID, "password")
                self.login_button = (By.ID, "signInBtn")

            def login(self, username, password):
                self.driver.find_element(*self.username_input).send_keys(username)
                self.driver.find_element(*self.password).send_keys(password)
                self.driver.find_element(*self.login_button).click()
                return ShopPage(self.driver)
        ```

    *   `pageObjects/CartPage.py`: Manages product selection and navigation to the cart.

        ```python
        from selenium.webdriver.common.by import By

        from pageObjects.checkout_confirm import checkout_confirm
        from utils.browserUtils import BrowserUtils


        class ShopPage(BrowserUtils):

            def __init__(self, driver):
                super().__init__(driver)
                self.driver = driver
                self.shopCart = (By.XPATH, "//a[contains(@href, 'shop')]")
                self.productCards = (By.XPATH, "//div[@class= 'card h-100']")
                self.cart_checkout_button = (By.CSS_SELECTOR, "a[class*= 'btn-primary']")

            def ... # Some code ommited for brevity
        ```

    *   `pageObjects/checkout_confirm.py`: Handles the checkout confirmation process.

        ```python
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions
        from selenium.webdriver.support.wait import WebDriverWait

        from utils.browserUtils import BrowserUtils


        class checkout_confirm(BrowserUtils):

            def __init__(self, driver):
                super().__init__(driver)
                self.driver = driver
                self.checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
                self.country_name = (By.ID, "country")
                self.country_option ...# Some code ommited for brevity
        ```

2.  **Running Tests:**

    Navigate to the project directory in your terminal and run the tests using pytest:

    ```bash
    pytest -v -s # For detailed output and print statements
    ```

    To generate an HTML report:

    ```bash
    pytest --html=report.html
    ```

3. **Example Test Case (Based on Files):**

   Given the existing files like `pythonSel/e2eTest.py` and the page objects, a typical end-to-end test would involve:

   * Logging into the store.
   * Adding items to the cart.
   * Proceeding to checkout.
   * Confirming the order.

   Refer to the `pythonSel/e2eTest.py` file for concrete examples once it is populated with test cases.
## Configuration Options

*   **Browser Selection:** The browser used for testing can be configured by modifying the `driver` initialization within your test scripts or through command-line arguments when running pytest.
*   **Test Data:**  The `data/test_e2eFramework.json` file (if populated) can be used to manage test data such as usernames, passwords, and product details.
*   **WebDriver Path:**  Ensure the WebDriver executable is in your system PATH, or configure the path directly in your test scripts.

## Contributing Guidelines

Contributions are welcome! To contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests to cover your changes.
5.  Submit a pull request with a clear description of your changes.

## License Information

License is not specified. All rights reserved by uditSINGH43.

## Acknowledgments

*   This project utilizes Selenium WebDriver and pytest for automated testing.
