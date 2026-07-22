from playwright.sync_api import Page

from pages.wikipedia_search_page import WikipediaSearchPage


def test_restaurant_search_returns_at_least_one_result(page: Page) -> None:
    """Part 2: Search for restaurant content and validate a result."""
    search_page = WikipediaSearchPage(page)

    search_page.open()
    search_page.search_for_restaurant()
    search_page.verify_at_least_one_result()
