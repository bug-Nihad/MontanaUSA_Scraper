import time
import re
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')

def extract_link(url):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    nav = driver.find_element_by_xpath('//span[@class="count"]')
    msg = nav.text
    msg = re.findall('[0-9]+', msg)
    limit = int(msg[-1])
    page_no = 2
    link_set = set()
    while True:
        nav = driver.find_element_by_xpath('//span[@class="count"]')
        msg = nav.text
        msg = re.findall('[0-9]+', msg)
        current = int(msg[-2])
        product_table = driver.find_element_by_xpath('//div[@id="product-loop"]')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        for each in product_table.find_elements_by_tag_name('a'):
            link_set.add(each.get_attribute('href'))
        if current < limit:
            driver.get(url+'?page='+str(page_no))
            page_no += 1
            time.sleep(2)
        else:
            break

    # file = open(file_name + '.txt', 'w')
    # for i in link_set:
    #     file.write(i +'\n')
    # file.close()
    driver.close()
    return link_set