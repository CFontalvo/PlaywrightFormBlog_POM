import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

tiempo=2

def test_formulario1(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={'width': 1500, 'height': 800}  # Corrige también el typo en 'height'
    )
    page = context.new_page()
    page.goto("https://christianfontalvo.com/")
    F = Funciones_Globales(page)
    expect(page).to_have_title(re.compile("Home"))
    page.screenshot(path="Imagenes/home.png")
    
    page.locator("(//a[@class='menu-link'][normalize-space()='Contacto'])[1]").click()
    expect(page).to_have_title(re.compile("Contacto"))
    page.screenshot(path="Imagenes/contacto.png")
    
    F.scroll_xy(0, 800, 5)    
    F.Texto("(//input[@id='wpforms-1513-field_0'])[1]","Christian",tiempo)
    F.Texto("//input[@id='wpforms-1513-field_1']","david.fontalvo@gmail.com",tiempo)
    F.Texto("//textarea[@id='wpforms-1513-field_2']","Este es un menaje automatizado con Playwright en Python, estoy practicando.",tiempo)
    page.screenshot(path="Imagenes/formulario_lleno.png")  
    F.Esperar(tiempo)
    page.locator("(//button[normalize-space()='Enviar'])[1]").click()
    F.Esperar(6)
    expect(page.locator("#wpforms-confirmation-1513 p")).to_have_text(re.compile("Gracias por contactarme")) 
    page.screenshot(path="Imagenes/boton_enviar.png")
    context.close()
    browser.close()
    

