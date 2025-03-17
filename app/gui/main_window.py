import flet as ft
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class MainWindow:
    def __init__(self):
        self.page = ft.Page()
        self.page.title = "Automação de Navegação"
        self.create_ui()

    def create_ui(self):
        # Criar um botão que chama a função de automação
        automate_button = ft.ElevatedButton(
            text="Automatizar Navegação",
            on_click=self.automate_browser  # A função que irá rodar a automação
        )
        self.page.add(automate_button)

    def automate_browser(self, e):
        """Automatiza a navegação usando Selenium e WebDriver Manager"""
        driver = webdriver.Chrome(ChromeDriverManager().install())  # Baixa o chromedriver automaticamente
        driver.get('https://www.google.com')
        time.sleep(3)  # Espera o Google carregar
        driver.quit()

    def run(self):
        # Iniciar a aplicação Flet
        ft.app(target=self.page)

# Criar a instância e rodar a aplicação
window = MainWindow()
window.run()
