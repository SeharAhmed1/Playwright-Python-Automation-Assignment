import re

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class RaddarHomePage(BasePage):
    """Page object for the public Raddar home page."""

    URL = "https://raddar.ca/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.body = page.locator("body")

    def open(self) -> None:
        self.open_url(self.URL)

    def verify_page_title(self) -> None:
        """Verify the Raddar title without relying on exact punctuation."""
        expect(self.page).to_have_title(
            re.compile(r"raddar", re.IGNORECASE),
            timeout=30_000,
        )

    def verify_two_visible_elements(self) -> None:
        
        expect(self.body).to_be_visible()

        structure_element = self._first_visible(
            [
                "header",
                "nav",
                "main",
                '[role="banner"]',
                '[role="navigation"]',
                '[role="main"]',
            ]
        )
        expect(structure_element).to_be_visible()

        interactive_element = self._first_visible(
            [
                "a[href]",
                "button",
                "input",
                '[role="button"]',
                '[role="link"]',
            ]
        )
        expect(interactive_element).to_be_visible()

    def _first_visible(self, selectors: list[str]) -> Locator:
        """Return the first visible element from a list of stable candidates."""
        for selector in selectors:
            matching_elements = self.page.locator(selector)
            for index in range(min(matching_elements.count(), 10)):
                candidate = matching_elements.nth(index)
                if candidate.is_visible():
                    return candidate

        raise AssertionError(
            f"No visible element was found for candidate selectors: {selectors}"
        )
