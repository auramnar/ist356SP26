from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://finance.yahoo.com/quote/AAPL/")

    # correct selector using data-testid
    price_locator = page.locator('[data-testid="qsp-price"]')

    price = price_locator.inner_text()
    print("AAPL Price:", price)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

    