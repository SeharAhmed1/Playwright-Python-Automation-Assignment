# Playwright Python Automation Assignment

## Assignment Coverage

### Part 1 – Basic Assertions

The test opens the public **Raddar** website and validates:

1. The page title contains "Raddar".
2. The main heading is visible.
3. Flyer-related content is displayed.

**Test file:**

```
tests/test_raddar_assertions.py
```

---

### Part 2 – Search

The test opens **Wikipedia**, searches for **restaurant**, and validates that restaurant-related content is displayed in the search results or article page.

**Test file:**

```
tests/test_restaurant_search.py
```

---

# Tools & Frameworks

- **Python** – Primary programming language.
- **Playwright** – Modern browser automation framework with built-in auto waiting.
- **pytest** – Test execution framework.
- **pytest-playwright** – Playwright integration for pytest.
- **pytest-html** – Generates an HTML execution report.
- **GitHub Actions** – Continuous Integration for automated test execution.

---

# Project Structure

```text
raddar-playwright-automation-assignment/
│
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
│
├── pages/
│   ├── base_page.py
│   ├── raddar_page.py
│   └── restaurant_search_page.py
│
├── tests/
│   ├── test_raddar_assertions.py
│   └── test_restaurant_search.py
│
├── test-results/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Framework Design

This project follows the **Page Object Model (POM)** design pattern.

- **pages/** contains reusable page actions and locators.
- **tests/** contains the test scenarios.
- **conftest.py** creates a clean browser instance for every test.
- **pytest.ini** stores default Playwright and pytest configuration.
- **GitHub Actions** automatically executes the test suite on every push.

---

# Prerequisites

- Python 3.10+
- Git

---

# Installation

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python -m playwright install chromium
```

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt

python -m playwright install chromium
```

---

# Running the Tests

Run the complete suite

```bash
python3 -m pytest
```

Run Part 1

```bash
python3 -m pytest tests/test_raddar_assertions.py
```

Run Part 2

```bash
python3 -m pytest tests/test_restaurant_search.py
```

Run with browser visible

```bash
python3 -m pytest --headed
```

Generate HTML report

```bash
python3 -m pytest --html=test-results/report.html --self-contained-html
```

---

# Test Artifacts

After execution, the following artifact is generated:

- **HTML Report**

```
test-results/report.html
```

The report includes:

- Test execution summary
- Passed / Failed status
- Execution duration
- Environment information

---

# Continuous Integration

The project includes a **GitHub Actions** workflow that:

- Installs Python dependencies
- Installs Playwright browsers
- Executes the test suite
- Uploads the HTML report as a workflow artifact

---

# Assumptions & Limitations

- Tests rely on the current UI structure of the public websites.
- If page layouts or locators change, the tests may require updates.
- The assignment focuses on the requested functional scenarios.

---

# Future Improvements

Given additional time, the framework could be extended to include:

- Cross-browser execution (Chromium, Firefox, WebKit)
- Parallel test execution
- Data-driven testing
- API validation
- Screenshot attachment for failed tests
- Playwright Trace Viewer integration
- Scheduled GitHub Actions execution
- Code coverage and test badges
