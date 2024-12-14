from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def highlight_element(driver, element, duration=6, color="yellow", border="2px solid red"):
    """Highlights a Selenium WebDriver element."""
    # Store the original style of the element
    original_style = element.get_attribute("style")
    # Use JavaScript to change the style
    driver.execute_script(f"arguments[0].style.border='{border}'; arguments[0].style.backgroundColor='{color}';", element)
    # Wait for a duration to visualize the highlight
    time.sleep(duration)
    # Revert the style to its original
    driver.execute_script(f"arguments[0].style='{original_style}';", element)
    time.sleep(duration)

# Example usage
driver = webdriver.Chrome()  # Use the appropriate driver for your browser
driver.get("https://magento.softwaretestingboard.com/customer/account/login")

# Find an element

element = driver.find_element(By.XPATH, "//h1[@class='page-title']/span")

# Highlight the element
highlight_element(driver, element)

# Close the browser
driver.quit()
