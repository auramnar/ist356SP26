from playwright.sync_api import Playwright, sync_playwright
import json

def stock_scraper(playwright: Playwright, stock, date) -> dict:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )

    page = context.new_page()
    page.goto(f"https://finance.yahoo.com/quote/{stock}/")

# To complete


    context.close()
    browser.close()

    return {
        "symbol": stock,
        "date": date,
        "price": price,
        "open": open_price
    }


if __name__ == "__main__":
    from datetime import datetime

    portfolio = ["AAPL", "AMZN", "GM", "HD", "META", "NET"]
    date = datetime.today().strftime('%Y-%m-%d')

    portfolio_data = []

    with sync_playwright() as playwright:
        for stock in portfolio:
            stock_dict = stock_scraper(playwright, stock, date)
            portfolio_data.append(stock_dict)
            print(stock_dict)

    with open(f"./5-web/cache/{date}-portfolio_data.json", "w") as f:
        json.dump(portfolio_data, f, indent=2)