import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

class Funciones_Globales:
    # Constructor
    def __init__(self, page: Page):
        self.page = page
    
    def Esperar(self, tiempo: int):
        """Espera la cantidad de milisegundos especificada."""
        self.page.wait_for_timeout(tiempo * 1000)  # Playwright espera en milisegundos
    
    def scroll_xy(self, x: int, y: int, tiempo: int):
        """Desplaza la página a las coordenadas especificadas con un tiempo de espera."""
        # Alternativa 1: Usar el método de desplazamiento del mouse
        self.page.mouse.wheel(x, y)
        self.page.wait_for_timeout(tiempo * 1000)

        # Alternativa 2: Usar JavaScript para desplazarse a una posición específica (reemplaza la línea anterior si prefieres esta opción)
        # self.page.evaluate(f"window.scrollBy({x}, {y});")
        # self.page.wait_for_timeout(tiempo * 1000)

    def Texto(self,selector,texto,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        time.sleep(tiempo)