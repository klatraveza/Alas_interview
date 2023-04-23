#Hello it's Andrey's Task 1 Automation assigment. Please not that I used Python to create this script.
# Using the "#" sign I will explain most of the steps just so we get an understanding what I am doing.
###
#Setting up my enviroment, Importing Selenium WD extantion
from selenium import webdriver
#Just making some things shorter cause we gonna use it alot. So the code looks a bit cleaner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
# Time modul for breaks so we can make pauses.
import time

# Setting up ChromeSearch class
class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def test_chrome_max(self):
        driver = self.driver
        driver.maximize_window()
        # Just making some variables so the code looks a bit cleaner.
        wait = WebDriverWait(driver, 10)
        url = "https://www.saucedemo.com/"
        #Just puting the data in.
        user_name="standard_user"
        user_pass="secret_sauce"
        f_name="Andrey"
        l_name="Shmatko"
        zip_c="21101"

        #And so it goes
        driver.get(url)
        #deleting Cookies
        driver.delete_all_cookies()
        # Printing page title just to know that we are in the right place
        print(driver.title)
        #And URL
        print(driver.current_url)
        time.sleep(3)
        #Reasuring we are on the right web page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Swag Labs')]")))


        # Let's Log in
        # Finding to user_name field and clicking
        driver.find_element(By.XPATH, "//input[@id='user-name']").click()
        time.sleep(2)
        #Sending keys to user_name
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user_name)
        #Let's insert the password
        driver.find_element(By.XPATH, "//input[@id='password']").click()
        #Sending keys to password section
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(user_pass)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()


        #Let's now make sure we are where we need to by identifing that we are on the Products page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Products')]")))
        #Sometimes webpages are downloaded slowly so we make sure we can click the product
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        # I love cool Backpacks :-)
        #Before we add product to a chart lets open it and look for the description
        driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]").click()


        #Ok we read it, lets go back.
        driver.back()
        #Lets put our product in the Cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        #Lets wait until it is added and Verify it has been added
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'1')]")))
        #* My wait timer is a bit long but u can change it in line 24
        #Let's just make sure that the right product was added.
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        #Let's make sure it is the right product
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))


        #Let's go back
        driver.back()
        #Let's find T-Shirt
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")))
        #Let's go look at the T-Shirt
        driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]").click()
        #Let's add T-Shirt to a cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()


        #Let's go to the cart
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        #Verify the first product (Backpack)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]")))
        #Verify the second product(T-Shirt)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")))


        #Removing the first Item (Backpack)
        driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']").click()
        #Let's make sure it is deleted.
        wait.until(EC.invisibility_of_element((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))
        #Let's make sure the right item stayed
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")))
        #Let's make sure that the marker near the cart changed from "2" back to "1"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'1')]")))


        #Let's Checkout
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        #Make sure the that lines for insert are viviable
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']")))
        #Let's put the data in and continue
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(f_name)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(l_name)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(zip_c)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        #Lets make sure we made it to overview page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Checkout: Overview')]")))
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        #Lets make sure that the order is complete
        or_compl= driver.find_element(By.XPATH, "//div[contains(text(),'Your order has been dispatched, and will "
                                                "arrive just as fast as the pony can get there!')]")
        if or_compl.is_displayed():
            print("Order is Complete!")
        else:
            print("Something went wrong")

    def tearDown(self):
        self.driver.quit()


class FierFox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_firefox_max(self):
        driver = self.driver
        driver.maximize_window()
        # Just making some variables so the code looks a bit cleaner.
        wait = WebDriverWait(driver, 10)
        url = "https://www.saucedemo.com/"
        # Just puting the data in.
        user_name = "standard_user"
        user_pass = "secret_sauce"
        f_name = "Andrey"
        l_name = "Shmatko"
        zip_c = "21101"

        # And so it goes
        driver.get(url)
        # deleting Cookies
        driver.delete_all_cookies()
        # Printing page title just to know that we are in the right place
        print(driver.title)
        # And URL
        print(driver.current_url)
        time.sleep(3)
        # Reasuring we are on the right web page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Swag Labs')]")))

        # Let's Log in
        # Finding to user_name field and clicking
        driver.find_element(By.XPATH, "//input[@id='user-name']").click()
        time.sleep(2)
        # Sending keys to user_name
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user_name)
        # Let's insert the password
        driver.find_element(By.XPATH, "//input[@id='password']").click()
        # Sending keys to password section
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(user_pass)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        # Let's now make sure we are where we need to by identifing that we are on the Products page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Products')]")))
        # Sometimes webpages are downloaded slowly so we make sure we can click the product
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        # I love cool Backpacks :-)
        # Before we add product to a chart lets open it and look for the description
        driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]").click()

        # Ok we read it, lets go back.
        driver.back()
        # Lets put our product in the Cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        # Lets wait until it is added and Verify it has been added
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'1')]")))
        # * My wait timer is a bit long but u can change it in line 24
        # Let's just make sure that the right product was added.
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        # Let's make sure it is the right product
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))

        # Let's go back
        driver.back()
        # Let's find T-Shirt
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")))
        # Let's go look at the T-Shirt
        driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]").click()
        # Let's add T-Shirt to a cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

        # Let's go to the cart
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        # Verify the first product (Backpack)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))
        # Verify the second product(T-Shirt)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")))

        # Removing the first Item (Backpack)
        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
        # Let's make sure it is deleted.
        wait.until(EC.invisibility_of_element((By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")))
        # Let's make sure the right item stayed
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]")))
        # Let's make sure that the marker near the cart changed from "2" back to "1"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'1')]")))

        # Let's Checkout
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        # Make sure the that lines for insert are viviable
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']")))
        # Let's put the data in and continue
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(f_name)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(l_name)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(zip_c)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        # Lets make sure we made it to overview page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Checkout: Overview')]")))
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        # Lets make sure that the order is complete

        or_compl = driver.find_element(By.XPATH, "//div[contains(text(),'Your order has been dispatched, and will "
                                                 "arrive just as fast as the pony can get there!')]")
        if or_compl.is_displayed():
            print("Order is Complete!")
        else:
            print("Something went wrong")

    def tearDown(self):
        self.driver.quit()