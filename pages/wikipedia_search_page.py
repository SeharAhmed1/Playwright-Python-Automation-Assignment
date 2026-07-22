import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class WikipediaSearchPage(BasePage):
    """Page object for a stable restaurant-related search flow."""

    URL = "https://en.wikipedia.org/wiki/Main_Page"
    SEARCH_TERM = "restaurant"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input = page.locator('input[name="search"]').first
        self.article_heading = page.locator("#firstHeading")
        self.search_results = page.locator(".mw-search-result")
        self.main_content = page.locator("#mw-content-text")

    def open(self) -> None:
        self.open_url(self.URL)
        expect(self.page).to_have_title(
            re.compile(r"wikipedia", re.IGNORECASE),
            timeout=30_000,
        )
        expect(self.search_input).to_be_visible(timeout=30_000)

    def search_for_restaurant(self) -> None:
        """Submit the search term through the visible search field."""
        self.search_input.fill(self.SEARCH_TERM)
        self.search_input.press("Enter")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(
            re.compile(r"wikipedia\.org/(wiki/|w/index\.php)"),
            timeout=30_000,
        )

    def verify_at_least_one_result(self) -> None:
        
        if self.search_results.count() > 0:
            first_result = self.search_results.first
            expect(first_result).to_be_visible(timeout=30_000)
            expect(first_result).to_contain_text(
                re.compile(r"restaurant", re.IGNORECASE),
                timeout=30_000,
            )
            return

        expect(self.article_heading).to_be_visible(timeout=30_000)
        expect(self.article_heading).to_contain_text(
            re.compile(r"restaurants?", re.IGNORECASE),
            timeout=30_000,
        )
        expect(self.main_content).to_be_visible(timeout=30_000)
