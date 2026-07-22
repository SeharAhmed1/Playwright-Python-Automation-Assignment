from playwright.sync_api import Page


class BasePage:
    """Common page-object functionality."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open_url(self, url: str) -> None:
        response = self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=40_000,
        )

        if response is not None and response.status >= 400:
            raise AssertionError(
                f"Navigation to {url} returned HTTP status {response.status}."
            )

        self.page.locator("body").wait_for(state="visible", timeout=20_000)
