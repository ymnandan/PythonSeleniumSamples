from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/nandan/WebDrivers/geckodriver")

driver.get("http://www.google.com")

element=driver.find_element_by_name("q")

element.send_keys("python program")

element.submit()
driver.quit()
