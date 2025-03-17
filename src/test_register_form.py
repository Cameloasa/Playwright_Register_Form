import re

from playwright.sync_api import Page, expect

def test_name_field(page: Page):
    """
    Testscenario T1: Testa namnfältet enligt acceptanskriterier A1–A3
    """
    # Steg 1: Navigera till registreringssidan
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")
    # Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Registrera dig"))

    # Steg 2: Kontrollera att ett namn-fält finns (A1)
    name_field = page.locator("label:has-text('Namn') input[type='text']") # label:  , input
    expect(name_field).to_be_visible()
