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

    # Steg 3: Klicka i fältet och skriv "Anna" (A2)
    name_field.click()
    name_field.fill("Anna")
    expect(name_field).to_have_value("Anna")

    # Steg 4: Kontrollera att inget felmeddelande visas
    error_message = page.locator("label:has-text('Namn') ~ p.error")
    expect(error_message).to_be_hidden()

    # Steg 5: Rensa fältet och lämna det tomt
    name_field.fill("")  # Rensa fältet

    # Steg 6: Kontrollera att ett felmeddelande visas: "Skriv in ditt namn" (A3)
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Skriv in ditt namn.")

    # Steg 7: Skriv in olika typer av värden: "123456", "Anna123", specialtecken
    test_values = ["123456", "Anna123", "@#%"]
    for value in test_values:
        name_field.fill(value)
        expect(name_field).to_have_value(value)

        # Steg 8: Kontrollera att inget felmeddelande visas för dessa värden
        expect(error_message).to_be_hidden()
