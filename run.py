from booking.booking import Booking 
import booking.constants as c

try:
    with Booking() as bot:
        bot.land_home_page()
        bot.close_popup()
        # bot.change_currency(currency=c.BASE_CURRENCY)
        bot.where_to_go("Osaka")
        bot.select_dates(check_in_date='2024-02-11', check_out_date='2024-02-26')
        bot.config_occupancy(4)
        bot.click_search()
        bot.apply_filters()

except Exception as e:
    if 'in PATH' in str(e):
        print("there is an PATH error")
    else:
        raise