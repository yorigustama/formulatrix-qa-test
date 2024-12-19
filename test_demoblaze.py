from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

# Initialize WebDriver
driver = webdriver.Chrome()

class TestDemoBlaze:

    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown(self):
        # Setup
        driver.get("https://www.demoblaze.com/index.html")
        driver.maximize_window()
        yield
        # Teardown
        driver.quit()

    def test_login(self):
        """Test login functionality"""
        driver.find_element(By.ID, "login2").click()
        time.sleep(2)  # Wait for modal to appear
        driver.find_element(By.ID, "loginusername").send_keys("tesq123")
        driver.find_element(By.ID, "loginpassword").send_keys("123")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(3)
        
        # Verify login success
        assert "Welcome test user" in driver.page_source

    def test_add_to_cart(self):
        """Test adding a product to the cart"""
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(2)
        
        # Handle alert
        alert = driver.switch_to.alert
        assert "Product added" in alert.text
        alert.accept()

    def test_cart_verification(self):
        """Verify the product appears in the cart"""
        driver.find_element(By.ID, "cartur").click()
        time.sleep(3)
        
        # Verify product in cart
        product_in_cart = driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']")
        assert product_in_cart.is_displayed()

    def test_logout(self):
        """Test logout functionality"""
        driver.find_element(By.ID, "logout2").click()
        time.sleep(2)
        
        # Verify logout success
        assert "Log in" in driver.page_source

# To run the test
if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_demoblaze.py"])
