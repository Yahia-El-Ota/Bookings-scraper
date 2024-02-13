from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFilters:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        
    def apply_star_rating(self, *star_values):
        star_filter_box = self.driver.find_element(By.ID,"filter_group_class_:r21:")
        star_child_elements = star_filter_box.find_elements(By.CSS_SELECTOR,"*")
        print(len(star_child_elements))
        
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
    
    def sort_by_lowest_price(self):
        sort_by_list = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        sort_by_list.click()

        lowest_price_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        lowest_price_element.click()

        