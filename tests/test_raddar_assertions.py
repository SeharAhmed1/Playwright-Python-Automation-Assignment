from playwright.sync_api import Page

from pages.raddar_home_page import RaddarHomePage


def test_raddar_page_title_and_visible_elements(page: Page) -> None:
    """Part 1: Verify the title and two visible elements on Raddar."""
    raddar_page = RaddarHomePage(page)

    raddar_page.open()
    raddar_page.verify_page_title()
    raddar_page.verify_two_visible_elements()
