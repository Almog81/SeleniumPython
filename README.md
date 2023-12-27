# SeleniumPython

SeleniumPython is a test automation project that uses Selenium WebDriver and Python to perform various tests on web applications.

## Requirements and Dependencies

To run this project, you need to have the following:

- Python 3.6 or higher
- Selenium 3.141.0 or higher
- ChromeDriver 87.0.4280.88 or higher
- PyTest 6.2.1 or higher
- Allure 2.13.8 or higher

## Project Structure

The project has the following structure:

- **config:** This folder contains the configuration files for the project, such as the base URL, browser options, and test data.
- **pages:** This folder contains the page objects for each web page that is tested. A page object is a class that represents a web page and provides methods to interact with its elements.
- **tests:** This folder contains the test cases for each web page. A test case is a function that uses PyTest and Selenium to perform a specific test scenario.
- **utils:** This folder contains the utility functions and classes that are used by the test cases, such as the driver manager, the logger, and the Allure reporter.
- **requirements.txt:** This file lists the dependencies for the project.
- **conftest.py:** This file contains the PyTest fixtures and hooks that are used by the test cases.
- **run_tests.py:** This file is the main script that runs the test cases and generates the allure report.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
