from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

max_wait_time = 20
# Headless Option
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Create driver for chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.safeway.com/shop/aisles/meat-seafood/beef.html?sort=&page=1&loc=697"
)

# Location button x out
location_button = driver.find_element(
    By.CSS_SELECTOR,
    "#onboardingCloseButton",
)
location_button.click()

# Cookie pop-up x out
cookie_button = driver.find_element(
    By.CSS_SELECTOR,
    "#onetrust-close-btn-container > button",
)
cookie_button.click()

# Load everything
while True:
    try:
        # Click load more until everything is loaded
        load_more_button = WebDriverWait(driver, max_wait_time).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#search-grid_0 > div:nth-child(1) > div.row.justify-content-center > button",
                )
            )
        )
        load_more_button.click()
    except NoSuchElementException:
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break


outer_divs = driver.find_elements(
    By.CSS_SELECTOR, ".product-card-container--with-out-ar"
)
for outer_div in outer_divs:
    # Locate the inner <div> elements inside the outer <div>
    inner_div_price = outer_div.find_element(By.CSS_SELECTOR, ".product-title__qty")
    inner_div_descr = outer_div.find_element(By.CSS_SELECTOR, ".product-title__name")

    print(inner_div_price.text, inner_div_descr.text)

# Close the driver when done
driver.quit()
