
import threading
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/126.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/127.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def setup_driver(proxy=None, user_agent=None):
    options = Options()
    options.add_argument("--headless")  # Rodar em modo headless para melhor desempenho em servidores
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"user-agent={user_agent if user_agent else get_random_user_agent()}")

    if proxy:
        # Para proxies com autenticação, é mais complexo com Selenium puro.
        # A abordagem mais robusta seria usar um plugin de proxy para o Chrome
        # ou um proxy local como o browsermob-proxy. No entanto, para simplificar
        # e focar na funcionalidade principal, vamos usar a opção --proxy-server
        # que funciona para proxies sem autenticação ou com autenticação via URL.
        # Para autenticação mais complexa, o usuário precisaria de um proxy local
        # que lide com isso ou de um plugin. Por enquanto, vamos assumir que
        # o formato user:pass@host:port é suficiente para a maioria dos casos.
        options.add_argument(f'--proxy-server={proxy}')

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def run_browser_instance(url, proxy=None, instance_id=0):
    user_agent = get_random_user_agent()
    print(f"[Instância {instance_id}] Iniciando com User-Agent: {user_agent}")
    if proxy:
        print(f"[Instância {instance_id}] Usando Proxy: {proxy}")

    driver = None
    try:
        driver = setup_driver(proxy, user_agent)
        driver.get(url)
        print(f"[Instância {instance_id}] Acessou: {url}")

        # Simular interação: scroll para baixo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print(f"[Instância {instance_id}] Rolou a página.")

        # Simular interação: tentar clicar em um link ou botão genérico
        try:
            # Tenta encontrar um link ou botão visível e clicável
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a, button"))
            )
            element.click()
            print(f"[Instância {instance_id}] Clicou em um elemento.")
            time.sleep(2)
        except Exception as e:
            print(f"[Instância {instance_id}] Não foi possível clicar em um elemento: {e}")

    except Exception as e:
        print(f"[Instância {instance_id}] Erro: {e}")
    finally:
        if driver:
            driver.quit()
            print(f"[Instância {instance_id}] Driver encerrado.")

def load_proxies_from_file(filepath):
    proxies = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):  # Ignorar linhas vazias e comentários
                    proxies.append(line)
    except FileNotFoundError:
        print(f"Arquivo de proxies não encontrado: {filepath}")
    return proxies

def main(url, num_instances, proxy_file=None):
    proxies = []
    if proxy_file:
        proxies = load_proxies_from_file(proxy_file)
        if not proxies:
            print("Nenhum proxy encontrado no arquivo. Continuando sem proxies.")

    threads = []
    for i in range(num_instances):
        proxy = proxies[i % len(proxies)] if proxies else None
        thread = threading.Thread(target=run_browser_instance, args=(url, proxy, i + 1))
        threads.append(thread)
        thread.start()
        # Pequeno atraso para evitar sobrecarga inicial
        time.sleep(1)

    for thread in threads:
        thread.join()
    print("Todas as instâncias do navegador foram concluídas.")

if __name__ == "__main__":
    # Exemplo de uso:
    # Crie um arquivo 'proxies.txt' na mesma pasta com uma lista de proxies, um por linha.
    # Ex: http://user:pass@host:port ou socks5://host:port
    target_url = "https://www.google.com"
    num_concurrent_instances = 2  # Defina o número de instâncias simultâneas
    proxy_list_file = "proxies.txt"

    print(f"Iniciando {num_concurrent_instances} instâncias para {target_url}...")
    main(target_url, num_concurrent_instances, proxy_list_file)


