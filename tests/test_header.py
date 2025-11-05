from playwright.sync_api import expect
from utils.config import Config
from pages.header import Header
from utils.data import Data
from utils.selectors import HeaderSelectors
    
def test_search(header: Header):
    start_form, end_form, start_url, end_url = Data.get_formatted_range(5, 12)
    header.fill_origin("Москва")
    header.fill_destination("Тайбей")
    header.select_start_date(start_form)
    header.select_end_date(end_form)
    header.click_button_search()
    header.assert_url(f"{Config.BASE_URL}?params=MOW{start_url}TPE{end_url}1&with_request=true")
    
def test_origin_valid_city(header: Header):
    header.fill_origin("Москва")
    expect(header.page.locator(HeaderSelectors.ORIGIN_INPUT)).to_have_value("Москва")

def test_destination_valid_city(header: Header):
    header.fill_destination("Иркутск")
    expect(header.page.locator(HeaderSelectors.DESTINATION_INPUT)).to_have_value("Иркутск")

def test_change_origin_destination(header: Header):
    header.fill_origin("Москва")
    header.fill_destination("Фукуок")
    header.page.get_by_role("option", name="Фукуок").first.click()
    header.change_origin_destination()
    expect(header.page.locator(HeaderSelectors.ORIGIN_INPUT)).to_have_value("Фукуок")
    expect(header.page.locator(HeaderSelectors.DESTINATION_INPUT)).to_have_value("Москва")

def test_origin_invalid_city(header: Header):
    header.fill_origin("Ксилоран")
    expect(header.page.locator(HeaderSelectors.ORIGIN_INPUT)).to_have_value("Ксилоран")
    expect(header.page.get_by_text(HeaderSelectors.NO_RESULTS_DROPDOWN)).to_be_visible()

def test_check_calendar_open(header: Header):  
    header.page.locator(HeaderSelectors.START_DATE_FIELD).click()
    expect(header.page.locator(HeaderSelectors.CALENDAR_DROPDOWN)).to_be_visible()

def test_open_settings(header: Header): 
    header.navigate_to_settings()
    header.assert_url(f"{Config.BASE_URL}my/settings")

def test_fill_code_IATA(header: Header):
    header.fill_origin("MSQ")
    expect(header.page.locator(HeaderSelectors.ORIGIN_INPUT)).to_have_value("MSQ")