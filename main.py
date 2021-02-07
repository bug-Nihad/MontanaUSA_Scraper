import time
from selenium import webdriver
import re

def extract_data(driver):
    while True:
        try:
            color_table = driver.find_element_by_xpath('//span[@class="webyzeSwatches"]')
            colors = color_table.find_elements_by_xpath('./span')
            many_color = 1
            break
        except:
            try:
                color = driver.find_element_by_xpath('//span[@class="it-is"]')
                many_color = 0
                break
            except:
                pass
    if many_color == 1:
        for color in colors:
            color.click()
            x = driver.find_element_by_xpath('//span[@class="variant-sku"]').text
            for i in range(10):
                try:
                    driver.find_element_by_xpath('//input[@name="quantity"]').send_keys('10000')
                    break
                except:
                    pass
            # driver.find_element_by_xpath('//input[@name="quantity"]').send_keys('1000')

            add_to_cart = driver.find_element_by_xpath('//input[@type="submit"]')
            if add_to_cart.get_attribute('value') == 'Sold Out':
                stock = 0
                print(stock, x)
                continue
            time.sleep(1)
            add_to_cart.click()
            while True:
                try:
                    msg = driver.find_element_by_xpath('//div[@class="errors qty-error"]').text
                    break
                except:
                    pass
            stock = re.findall('[0-9]+', msg)[0]
            print(stock, x)
            # time.sleep(1)
    if many_color == 0:
        x = driver.find_element_by_xpath('//span[@class="variant-sku"]').text
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@name="quantity"]').send_keys('10000')
                break
            except:
                pass
        add_to_cart = driver.find_element_by_xpath('//input[@type="submit"]')
        if add_to_cart.get_attribute('value') == "Sold Out":
            stock = 0
            print(stock, x)
            return
        time.sleep(1)
        add_to_cart.click()
        # time.sleep(1)
        while True:
            try:
                msg = driver.find_element_by_xpath('//div[@class="errors qty-error"]').text
                break
            except:

                pass
        stock = re.findall('[0-9]+', msg)[0]
        print(stock, x)


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.montanawestusa.com/collections/new-arrival')
driver.maximize_window()

table = driver.find_element_by_xpath('//div[@id="product-loop"]')
first_product = table.find_element_by_xpath('//div[@class="prod-container"]').find_element_by_tag_name('a')
first_product.click()
time.sleep(1)
for i in range(100):
    print(i)
    # while True:
    #     try:
    #         driver.find_elements_by_xpath('//i[@class="fa fa-angle-right"]')[1].click()
    #         time.sleep(1)
    #         extract_data(driver)
    #         break
    #     except:
    #         time.sleep(1)
    # time.sleep(1)
    extract_data(driver)
    driver.execute_script("scroll(0, 0);")
    time.sleep(2)
    while True:
        try:
            driver.find_elements_by_xpath('//i[@class="fa fa-angle-right"]')[1].click()
            break
        except:
            pass
    # time.sleep(1)