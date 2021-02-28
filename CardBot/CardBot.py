import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.target.com/p/animal-crossing-new-horizons-nintendo-switch/-/A-82486780?preselect=76780148#lnk=sametab")

foundButton = False

while not foundButton:

    time.sleep(1)

    # find_elements returns a list instead of an exception
    if driver.find_elements_by_css_selector('[data-test=soldOutBlock]'):

        driver.refresh()

    elif driver.find_elements_by_css_selector('[data-test=shipItButton]'):

        addToCartButton = driver.find_element_by_css_selector('[data-test=shipItButton]')

        foundButton = True

    else:
        print("yo")
        driver.refresh()

addToCartButton.click()