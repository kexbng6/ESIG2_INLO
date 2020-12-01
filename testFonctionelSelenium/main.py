# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver

# driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()



def runBrowser():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://sgpc2.pythonanywhere.com/')
    time.sleep(25) # Let the user actually see something!
    return driver

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runBrowser()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
