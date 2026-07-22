from pathlib import Path

import pytest
from playwright.sync_api import Page


RESULTS_DIRECTORY = Path("test-results")
SCREENSHOTS_DIRECTORY = RESULTS_DIRECTORY / "screenshots"


@pytest.fixture(scope="session", autouse=True)
def create_results_directories() -> None:
    """Create report and screenshot directories before the test session."""
    SCREENSHOTS_DIRECTORY.mkdir(parents=True, exist_ok=True)


@pytest.fixture(autouse=True)
def configure_page(page: Page) -> None:
    """Apply consistent timeouts and viewport settings to every test."""
    page.set_default_timeout(20_000)
    page.set_default_navigation_timeout(40_000)
    page.set_viewport_size({"width": 1440, "height": 900})


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    """Capture a full-page screenshot when a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    safe_test_name = "".join(
        character if character.isalnum() or character in "-_" else "_"
        for character in item.nodeid
    )
    screenshot_path = SCREENSHOTS_DIRECTORY / f"{safe_test_name}.png"

    try:
        page.screenshot(path=str(screenshot_path), full_page=True)
    except Exception:
        pass
