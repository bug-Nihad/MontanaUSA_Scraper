import time
from selenium import webdriver
import re
from LinkExtractor import extract_link

def extract_data(driver, file):
    try:
        for trial in range(10):
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
                    time.sleep(1)
        if many_color == 1:
            for color in colors:
                color.click()
                time.sleep(1)
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
                    file.write(stock + ',' + x + '\n')
                    continue
                time.sleep(1)
                add_to_cart.click()
                for trial in range(5):
                    try:
                        msg = driver.find_element_by_xpath('//div[@class="errors qty-error"]').text
                        break
                    except:
                        time.sleep(1)
                stock = re.findall('[0-9]+', msg)[0]
                print(stock, x)
                file.write(stock + ',' + x + '\n')
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
                return 0
            time.sleep(1)
            add_to_cart.click()
            # time.sleep(1)
            for trial in range(5):
                try:
                    msg = driver.find_element_by_xpath('//div[@class="errors qty-error"]').text
                    break
                except:
                    time.sleep(1)
            stock = re.findall('[0-9]+', msg)[0]
            print(stock, x)
            return 0
    except:
        return 1

link_set = extract_link('https://www.montanawestusa.com/collections/mens-goods')
driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

for each_link in link_set:
    driver.get(each_link)
    time.sleep(1)
    file = open('Mens_goods.csv', 'a')
    y = extract_data(driver, file)
    if y == 1:
        error_file = open('error_file_mensgood.txt', 'a')
        error_file.write(each_link + '\n')
        continue
    file.close()