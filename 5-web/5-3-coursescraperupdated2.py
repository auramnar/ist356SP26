from playwright.sync_api import Playwright, sync_playwright
import json


# function takes browser automation and searches for course
def course_scraper(playwright: Playwright, course: str):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to the Syracuse course search page
    page.goto("https://coursecatalog.syracuse.edu/course-search/")
    page.get_by_placeholder("Keyword").fill(course)
    page.get_by_role("button", name="SEARCH").click()

    # Wait for search results and click the first matching course
    course_code = course.split()[0].upper()
    page.wait_for_selector(f"a:has-text('{course_code}')", timeout=15000)
    page.locator(f"a:has-text('{course_code}')").first.click()

    # Wait for detail page
    page.wait_for_load_state("networkidle")

    # Extract title
    title_locator = page.locator(
        "div.text.detail-title.margin--tiny.text--semibold.text--big"
    )
    title = title_locator.first.inner_text() if title_locator.count() > 0 else "N/A"

    # Extract credits
    credits_locator = page.locator(
        "div.text.detail-hours_html.margin--tiny.text--semibold.text--big"
    )
    credits = credits_locator.first.inner_text() if credits_locator.count() > 0 else "N/A"

    # Extract description
    try:
        desc_locator = page.locator(
            "div.section.section--description > div.section__content"
        )
        if desc_locator.count() > 0:
            description = desc_locator.first.inner_text()
        else:
            description = page.locator("p").first.inner_text()
    except:
        description = "N/A"

    # create dictionary
    course_data = {
        "course_code": course,
        "title": title.strip(),
        "credits": credits.strip(),
        "description": description.strip(),
    }

    print(json.dumps(course_data, indent=2))

    context.close()
    browser.close()

    return course_data   # ← IMPORTANT FIX


if __name__ == "__main__":
    courses = "IST 256, IST 387, IST 101, IST 356"
    course_data = []

    with sync_playwright() as playwright:
        for course in courses.split(","):
            course_dict = course_scraper(playwright, course.strip())
            course_data.append(course_dict)

    # save json
    with open("course_data.json", "w", encoding="utf-8") as f:
        json.dump(course_data, f, indent=2)

    print("Saved to course_data.json")