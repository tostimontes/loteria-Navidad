# loteria-Navidad-checker

## Introduction
This project is a Python-based script designed to automate the process of checking lottery numbers for the 2023 Spanish National Christmas lottery.
The project was created to experiment with Python's capabilities for web scraping. The script utilizes Selenium's WebDriver for automating interactions with a target web page, allowing users to efficiently verify lottery numbers by uploading a plain text file containing the numbers. The output of the script is a text file containing each checked number along with a custom message indicating whether it is a winning number and, if so, the corresponding prize amount.

## Installation

### Prerequisites
Download [Python 3](https://www.python.org/downloads/):
Python is essential for running the script. You can download it from the official Python website. Make sure to download Python 3, as this is the version your script is likely compatible with.

Download [Selenium WebDriver (ChromeDriver)](https://chromedriver.chromium.org/downloads):
Selenium requires a specific WebDriver for each browser. Since the script uses Chrome, you'll need the ChromeDriver. Make sure the version of ChromeDriver matches the version of Google Chrome installed on your system.

After downloading these, install Python following the provided instructions on their website. For ChromeDriver, unzip the downloaded file and place it in a known directory on your system. You will need to specify this path in your script where the Service class is used.

### Library Dependencies
- `selenium`: For automating web browser interaction.
  
  Install it using pip:
  ```
  pip install selenium
  ```

### Downloading the Scripts
- Clone or download this repository to your local machine.

### WebDriver Setup
- Ensure you have the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).
- Place the WebDriver in a known directory on your system.
    - Create a `.env` file in the project's root directory.
    - Set Environment Variables:
        - For `loteria.py`, add CHROMEDRIVER_EXE_PATH=*/path/to/chromedriver*.
        - For `loteria-windows.py`, use LINUX_CHROMEDRIVER_EXE_PATH=*/path/to/chromedriver*.
    - Replace /path/to/chromedriver with the actual path to your ChromeDriver.

## Usage

1. **Prepare Your Lottery Numbers File**:
   - Create a text file named `numeros-loteria.txt`.
   - Add your lottery numbers to this file, one number per line.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script with Python:
     ```sh
     # UNIX based systems
     python loteria.py
     ```
     or:
     ```sh
     # Windows
     python loteria-windows.py
     ```

3. **View the Results**:
   - After running the script, check the newly created `lottery_results.txt` file.
   - This file will contain each checked number with its corresponding prize information or a custom message if there's no prize.

## Customization
- To use a different WebDriver or modify the script for a different lottery, you can edit the script and adjust the parameters and web elements accordingly.
