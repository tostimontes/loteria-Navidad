from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service  # Import the Service class
import time


def check_lottery_numbers(numbers, driver, url):
    results = []

    for number in numbers:
        # Load the page
        driver.get(url)

        # Find the input field and submit button
        number_input = driver.find_element(By.ID, "numero_sorteo_navidad")
        submit_button = driver.find_element(By.ID, "submit_buscar_decimos_navidad")

        # Enter the number and click the button
        number_input.clear()
        number_input.send_keys(number)
        submit_button.click()

        # Wait for response and extract it
        time.sleep(2)  # Adjust this sleep time as necessary
        response_element = driver.find_element(By.CSS_SELECTOR, "#result_navidad p")
        response = response_element.text
        results.append(f"Number: {number}, Result: {response}")

    return results



def main():
    # URL of the page containing the lottery checker
    url = 'https://www.rtve.es/components/loteria/navidad/embeber.html'

    # Read numbers from file
    with open('numeros-loteria.txt', 'r') as file:
        numbers = [line.strip() for line in file.readlines()]

    # Set up the Selenium driver
    service = Service(executable_path='/home/tostimontes/Webdrivers/chromedriver-linux64/chromedriver')  # Update the path to your chromedriver
    driver = webdriver.Chrome(service=service)

    # Check numbers and get results
    results = check_lottery_numbers(numbers, driver, url)

    # Write results to a file
    with open('lottery_results.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

    driver.quit()

if __name__ == "__main__":
    main()
