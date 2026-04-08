def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) #  # Launch the Chromium browser (headless=False shows the browser window)
    context = browser.new_context() # create a new browser context
    page = context.new_page() # open a new page or tab
    page.goto("https://www.imdb.com/chart/top/") # go to the page
    #page.wait_for_selector("table, ul") # wait for table or to show before scraping
    content = page.content() # get the page content 
    print(content)
    
    # cleanup
    # close browser context
    # close browser to free up resources
    context.close()
    browser.close()