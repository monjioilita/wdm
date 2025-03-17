import flet as ft
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Função para automatizar a busca no Google
def automate_google_search(query):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Executar sem abrir a janela do navegador
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())  # Configura o WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.google.com")  # Abre o Google
        time.sleep(2)  # Aguarda carregar

        # Localiza a barra de pesquisa e insere a consulta
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()

        time.sleep(2)  # Espera os resultados carregarem

        # Captura os 10 primeiros resultados
        results = []
        search_results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")[:10]
        for result in search_results:
            title = result.find_element(By.CSS_SELECTOR, "h3").text
            link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            results.append(f"{title}\n{link}")

        return results
    except Exception as e:
        return [f"Erro ao buscar: {e}"]
    finally:
        driver.quit()  # Fecha o navegador

# Função que cria a interface gráfica usando Flet
def main(page: ft.Page):
    page.title = "Pesquisa no Google"

    # Campo de entrada para o usuário digitar a pesquisa
    search_input = ft.TextField(label="Digite o que deseja pesquisar", autofocus=True)

    # Área para mostrar os resultados
    results_list = ft.Column(scroll=True)

    # Mensagem de status
    status_text = ft.Text("Digite um termo e pressione 'Pesquisar'.")

    # Função chamada ao clicar no botão
    def start_search(e):
        query = search_input.value.strip()
        if not query:
            status_text.value = "Por favor, digite um termo para pesquisar."
            page.update()
            return
        
        status_text.value = "Pesquisando no Google..."
        page.update()

        results = automate_google_search(query)  # Executa a pesquisa

        # Atualiza a interface com os resultados
        results_list.controls.clear()
        for item in results:
            results_list.controls.append(ft.Text(item))
        
        status_text.value = "Pesquisa concluída!"
        page.update()

    # Botão para iniciar a pesquisa
    search_button = ft.ElevatedButton("Pesquisar", on_click=start_search)

    # Adicionando os elementos à interface
    page.add(search_input, search_button, status_text, results_list)

# Inicia o aplicativo Flet
ft.app(target=main)

