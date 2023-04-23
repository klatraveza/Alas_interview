import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://www.saucedemo.com/"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@id='user-name']")
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")

    def load(self):
        self.driver.get(base_url)

    def action0(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class ItemsPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_info = (By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")
        self.t_shirt_info = (By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")
        self.backpack_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.t_shirt_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.cart = (By.XPATH, "//a[@class='shopping_cart_link']")

    def action1(self):
        self.driver.find_element(*self.backpack_cart).click()
        self.driver.find_element(*self.t_shirt_info).click()
    def action2(self):
        self.driver.find_element(*self.t_shirt_cart).click()
        self.driver.find_element(*self.cart).click()

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.remove_item_1 = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
        self.chek_out= (By.XPATH, "//button[@id='checkout']")
    def action_3(self):
        self.driver.find_element(*self.remove_item_1).click()
        self.driver.find_element(*self.chek_out).click()

class CheckOut:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.XPATH, "//input[@id='first-name']")
        self.lname_input = (By.XPATH, "//input[@id='last-name']")
        self.postal_c_input = (By.XPATH, "//input[@id='postal-code']")
        self.check_out_b = (By.XPATH, "//input[@id='continue']")
        self.finish_b=(By.XPATH, "//button[@id='finish']")
    def action4(self, f_name,l_name,postal_c ):
        self.driver.find_element(*self.name_input).send_keys(f_name)
        self.driver.find_element(*self.lname_input).send_keys(l_name)
        self.driver.find_element(*self.postal_c_input).send_keys(postal_c)
        self.driver.find_element(*self.check_out_b).click()
        time.sleep(2)
        self.driver.find_element(*self.finish_b).click()
        time.sleep(3)


def testcheck():
    # Initialize the webdriver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    # Create instances of the page classes
    login_page = LoginPage(driver)
    items_page = ItemsPage(driver)
    cart_page = CartPage(driver)
    checkout = CheckOut (driver)
    # Load the login page
    login_page.load()

    # Login to the site
    login_page.action0("standard_user", "secret_sauce")

    # Putting backpack in a cart and looking at T-Shirt details
    items_page.action1()
    if driver.find_element(By.XPATH, "//span[contains(text(),'1')]"):
        driver.save_screenshot("Test 1 success.png")
        print("Test №1 pass")
    else:
        print("Product is not in the box")

    # Putting T-shirt in the cart and going to the cart
    items_page.action2()
    if driver.find_element(By.XPATH, "//span[contains(text(),'2')]"):
        driver.save_screenshot("Test 2 success.png")
        print("Test №2 pass")
    else:
        print("Product 2 was not added to the box")
    # Removing item 1 and checking out
    cart_page.action_3()
    if driver.find_element(By.XPATH, "//span[contains(text(),'1')]"):
        driver.save_screenshot("Test 3 success.png")
        print("Test №3 pass")
    else:
        print("Product was not removed")
    # Finishing
    checkout.action4("Andrey","Shmatko","210101")
    if driver.find_element(By.XPATH, "//div[contains(text(),'Your order has been dispatched, and will "
                                                "arrive just as fast as the pony can get there!')]"):
        driver.save_screenshot("Test DONE.png")
        print("The order is complete")
    else:
        print("Something went wrong Andrey")
    # Close the browser
    driver.quit()

testcheck()
