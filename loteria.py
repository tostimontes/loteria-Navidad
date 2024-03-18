import os
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

        # Wait for response to be visible
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "result_navidad")))

        # Check if it's a winning message
        content_div = driver.find_element(By.ID, "total_navidad")
        if "¡Enhorabuena!" in content_div.text:
            # Extract details for winning scenario
            prize_message = content_div.find_element(By.CSS_SELECTOR, "p.num").text
            prize_amount_text = content_div.find_element(By.CSS_SELECTOR, "p.prem").text

            # Check the prize amount
            if "100" in prize_amount_text:
                detailed_prize_info = "Una mijita."
            else:
                detailed_prize_info = prize_message + " " + prize_amount_text

            results.append(f"Número: {number}, Premio: {detailed_prize_info}")
        else:
            # Handle no prize scenario
            no_prize_message = "Nada y menos."
            results.append(f"Número: {number}, Premio: {no_prize_message}")

    return results


def main():
    # URL of the page containing the lottery checker
    url = "https://www.rtve.es/loterias/loteria-navidad/buscador/"

    # Read numbers from file and extract only the first 5-digit numbers from each line
    with open("numeros-loteria.txt", "r") as file:
        numbers = [
            line[:5]
            for line in file.readlines()
            if line[:5].isdigit() and len(line[:5]) == 5
        ]

    # Set up the Selenium driver
    service = Service(executable_path=os.environ.get("LINUX_CHROMEDRIVER_EXE_PATH"))
    if not executable_path:
        raise ValueError("CHROMEDRIVER_EXE_PATH environment variable is not set")
    # Update the path to your chromedriver
    driver = webdriver.Chrome(service=service)

    # Check numbers and get results
    results = check_lottery_numbers(numbers, driver, url)

    # Write results to a file
    with open("lottery_results.txt", "w") as file:
        for result in results:
            file.write(result + "\n")

    driver.quit()


if __name__ == "__main__":
    main()
