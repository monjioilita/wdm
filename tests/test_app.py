import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class TestSeleniumAutomation(unittest.TestCase):
    
    def test_google_search(self):
        # Usando o WebDriver Manager para buscar e instalar o ChromeDriver corretamente
        service = Service(ChromeDriverManager().install())
        
        # Inicializando o WebDriver com o serviço
        driver = webdriver.Chrome(service=service)
        
        driver.get("https://www.google.com")
        time.sleep(2)  # Espera o Google carregar
        self.assertIn("Google", driver.title)  # Verifica se "Google" está no título da página
        driver.quit()

if __name__ == "__main__":
    unittest.main()
