'''
Create an outline!

Scrape the Sections H2 and H3 from this page:  https://ist256.com/fall2023/syllabus/

Print the titles, and detect the tag name so that you indent the H3 tags under the H2 tags.


'''

from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # .launch(headless=False) shows the to show the browser window. .
    page = context.new_page() # open a new page or tab
    # creates a new browser context. A browser context is an isolated environment within a browser instance. It allows you to create multiple independent sessions, each with its own cookies, cache, and other browsing data. This is useful for testing scenarios where you want to simulate different users or sessions without interference.
    page.goto("https://ist256.com/fall2023/syllabus/") # go to the page
    
    page.wait_for_selector("") # wait for table or to show before scraping
    
    headings = page.query_selector_all("h2, h3") # select all h2 and h3 tags

    
    # cleanup
    # close browser context
    # close browser to free up resources
    context.close()
    browser.close()
