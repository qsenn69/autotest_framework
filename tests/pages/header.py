from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage
from utils.config import locator

class Header(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_locator = 'div[class*="s__GkNOd0J0D3cppEDs s___Ih4FphCv9oj087o s__l_V_9vGK0U9NXGCh"]'

    def _get(self, selector: str) -> Locator:
        return self.page.locator(f"{self.base_locator} {selector}")

    def navigate_to_home(self):
        self._get(locator("header", "logo_button")).click()

    def navigate_to_magazine(self):
        self._get(locator("header", "magazine_button")).click()

    def navigate_to_support(self):
        self._get(locator("header", "support_button")).click()

    def navigate_to_settings(self):
        self._get(locator("header", "profile_button")).click()
        self.page.get_by_text(locator("header", "settings_button")).click()

    def navigate_to_hotels(self):
        self.page.get_by_role('link', name="Отели").click()

    def navigate_to_guides(self):
        self.page.get_by_role('link', name="Коро́че").click()

    def navigate_to_favorites(self):
        self.page.get_by_role('link', name="Избранное").click()

    def navigate_to_b2b(self):
        self.page.get_by_role('link', name="Для бизнеса").click()

    def change_origin_destination(self):
        self._get(locator("header", "change_of_directions_button")).click()

    def fill_origin(self, city: str):
        self._get(locator("header", "origin_input")).fill(city)

    def fill_destination(self, city: str):
        self._get(locator("header", "destination_input")).fill(city)

    def select_start_date(self, start_date: str):
        self._get(locator("header", "start_date_field")).click()
        self.page.locator(f'[data-test-id="date-{start_date}"]').click()

    def select_end_date(self, end_date: str):
        self._get(locator("header", "end_date_field")).click()
        self.page.locator(f'[data-test-id="date-{end_date}"]').click()

    def click_button_search(self):
        self._get(locator("header", "search_button")).click()

    def origin_input(self) -> Locator:
        return self._get(locator("header", "origin_input"))

    def no_results_message(self) -> Locator:
        return self.page.get_by_text(locator("header", "no_results_dropdown"))

    def calendar_dropdown(self) -> Locator:
        return self._get(locator("header", "calendar_dropdown"))