import re

from playwright.sync_api import Page, expect

def test_name_field(page: Page):
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")
    # Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Registrera dig"))
