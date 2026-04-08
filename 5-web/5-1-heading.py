from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.imdb.com/chart/top/")

    # wait for heading to appear
    page.wait_for_selector("h1")

    # correct selector (class names need dots)
    heading = page.query_selector("h1.ipc-title__text")
    # spaces which means "descendant selector"
    # "h1.ipc-title__text chart-layout-specific-title-text" was interpreted as:
    # chart-layout-specific-title-text inside h1.ipc-title__text (doesn't exist)
    # Alternatively we could use heading = page.locator("h1").first
    # more stable than relying on class names which can change
    
    # the tag name of the element
    tag = heading.evaluate("el => el.tagName")
    print(tag)

    # the contents of the element
    print(heading.inner_text())
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)