# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver



# https://stackoverflow.com/questions/30543698/how-to-create-a-single-webdriver-instance-in-python


def runBrowser():
    driver = webdriver.Chrome('../chromedriver')
    #driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get('https://sgpc2.pythonanywhere.com/compte/login/')
    driver.implicitly_wait(6)

#loginClient
    driver.find_element_by_id("id_username").send_keys("lkrolik1@usda.gov")
    driver.find_element_by_id("id_password").send_keys("Motdepasse1234")
    time.sleep(3)
    driver.find_element_by_id("submit").click()

    time.sleep(6)

#testSetUp
    driver.find_element_by_link_text("Mon panier").click()
    # if driver.find_element_by_tag_name("h1"):
    #     driver.find_element_by_id("retourBoutique").click()
    # else:
    #     driver.find_element_by_link_text("Vider le panier").click()
    #     driver.implicitly_wait(6)
    #     driver.find_element_by_link_text("Catalogue").click()

#testAjoutProduit
    #driver.find_element_by_link_text("acheter").click()
    driver.implicitly_wait(5)
    driver.close()
    #driver.find_element_by_link_text("Ajouter au panier").click()

    time.sleep(7)
    #driver.find_element_by_name("se déconnecter").click()

#testAugmenterQuantite

#testDiminuerQuantite

#testDiminuerUneUnite

#testPrixTotalLigne

#testRetraitArticle

#-testViderPanier

def setUp():
    runBrowser()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setUp()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

