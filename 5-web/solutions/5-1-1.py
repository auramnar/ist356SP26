'''
Scrape the Title off this page:  https://ist256.com/fall2023/about/ 

Use the #ID selector to select the title.


'''
from playwright.sync_api import Playwright, sync_playwright, expect

# Function perform the browser automation tasks
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) #  # Launch the Chromium browser (headless=False shows the browser window)
    context = browser.new_context() # create a new browser context
    page = context.new_page() # open a new page or tab
    page.goto("https://ist256.com/fall2023/about/") # go to the page
    
    heading = page.query_selector("h1#about-ist256") 
    print(heading.inner_text()) # select the heading using the ID selector
    
    
    # cleanup
    # close browser context
    # close browser to free up resources
    context.close()
    browser.close()

# launch playwright
# ensure it shuts down
with sync_playwright() as playwright:
    run(playwright)