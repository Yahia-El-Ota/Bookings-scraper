import booking.constants as c
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from booking.booking_filters import BookingFilters

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exception_type, exception_value, traceback):
        if self.teardown:
            self.quit()

    def land_home_page(self):
        self.get(c.BASE_URL)
        time.sleep(3)

    def close_popup(self):
        exit_element = self.find_element(By.CSS_SELECTOR,
            'button[aria-label="Dismiss sign in information."]'
        )
        exit_element.click()
   
    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()
        is_currency_found = False
        default_currency = 'USD'
        btn_default_currency = None
        btns = self.find_elements(By.CSS_SELECTOR, 'button[data-testid="selection-item"]')
        for btn in btns:
            currency_value = btn.find_element(By.CSS_SELECTOR, 'div.ea1163d21f').text
            if currency_value == default_currency:
                btn_default_currency = btn
            if currency_value == currency:
                btn.click()
                is_currency_found = True
                break

        if not is_currency_found:
            print("No matching currency found, USD is used as default currency")
            btn_default_currency.click()

    def where_to_go(self, place):
        search_field = self.find_element(By.ID, ":re:")
        search_field.clear()
        search_field.send_keys(place)
        time.sleep(3)

        selected_place = self.find_element(By.ID, "autocomplete-result-0")
        selected_place.click()
        time.sleep(2)

    def select_dates(self, check_in_date, check_out_date):
        
        check_in_element = self.find_element(By.CSS_SELECTOR,
            f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR,
            f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def config_occupancy(self,count):
        config_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        config_element.click()

        
        adults_element = self.find_element(By.CSS_SELECTOR, 'input[id="group_adults"]')
        adults_value = int(adults_element.get_attribute('value'))


        if count == adults_value:
            print("it is 2")
            
        # if the count value is not the default value then click minus button until value is 1 and click plus button for count-1
        elif count != adults_value:
            minus_element = self.find_element(By.CSS_SELECTOR, 
                'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 e91c91fa93"]'
            )
            plus_element = self.find_element(By.CSS_SELECTOR, 
                'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a"]'
            )
            for i in range(adults_value-1):
                minus_element.click()

            for i in range(count-1):
                plus_element.click()
    

    def click_search(self):
        search_element = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'                                   
        )
        search_element.click()

    def apply_filters(self):
        filter = BookingFilters(driver=self)
        filter.apply_star_rating(4,5)
        filter.sort_by_lowest_price()
