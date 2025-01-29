from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Caminho para o ChromeDriver
CHROME_DRIVER_PATH = "C:\\chromedriver\\chromedriver.exe"


# Inicializa o driver do navegador
def initialize_driver():
    service = Service(CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Inicia com janela maximizada
    return webdriver.Chrome(service=service, options=options)

# Aceita cookies no site, se necessário
def accept_cookies(driver):
    try:
        accept_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Aceitar todos os cookies")]'))
        )
        accept_button.click()
        print("Cookies aceitos com sucesso!")
    except Exception as e:
        print("Nenhum botão de cookies encontrado ou erro ao aceitá-los:", e)

# Preenche o formulário no modal
def test_all_fields_completes(driver):
    try:
        # Espera o modal aparecer
        dialog_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog' and @data-state='open']"))
        )
        print("Modal de diálogo encontrado com sucesso!")

        # Preenche os campos do formulário
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "CPF"))
        ).send_keys("123.456.789-00")
        
        driver.find_element(By.ID, "Nome").send_keys("Teste Selenium")
        driver.find_element(By.ID, "E-mail").send_keys("teste@selenium.com")
        driver.find_element(By.ID, "Celular").send_keys("11999999999")

        # Preenchendo o campo "Data de nascimento"
        birth_date_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Data de nascimento*']"))
        )
        birth_date_field.send_keys("01/01/2000")
        print("Campos preenchidos com sucesso!")

        # Aceita os termos e envia o formulário
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "terms"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @form='leads-form']"))
        ).click()
        print("Formulário enviado com sucesso!")

        # Identificando mensagem de erro (caso exista)
        identify_error_message(driver)

    except Exception as e:
        print(f"Erro ao interagir com o formulário: {e}")
        raise

def test_all_fields_void(driver):
    try:
        # Espera o modal aparecer
        dialog_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog' and @data-state='open']"))
        )
        print("Modal de diálogo encontrado com sucesso!")

        # Preenche os campos do formulário
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "CPF"))
        ).send_keys("")
        
        driver.find_element(By.ID, "Nome").send_keys("")
        driver.find_element(By.ID, "E-mail").send_keys("")
        driver.find_element(By.ID, "Celular").send_keys("")
        birth_date_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Data de nascimento*']"))
        )
        birth_date_field.send_keys("")
        print("Campos vazios com sucesso!")

        # Aceita os termos e envia o formulário
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "terms"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @form='leads-form']"))
        ).click()
        print("Formulário enviado com sucesso!")

        # Identificando mensagem de erro (caso exista)
        identify_error_message(driver)

    except Exception as e:
        print(f"Erro ao interagir com o formulário: {e}")
        raise

def test_refresh_with_partial_data(self):
        """Testar comportamento ao atualizar a página com dados preenchidos."""
        driver = self.driver
        driver.find_element(By.ID, "first_name").send_keys("João")
        driver.find_element(By.ID, "last_name").send_keys("Silva")
        driver.find_element(By.ID, "email").send_keys("joao.silva@example.com")
        driver.refresh()

        # Verifica se os dados foram limpos após o refresh
        self.assertEqual(driver.find_element(By.ID, "first_name").get_attribute("value"), "", "Os dados não foram limpos após o refresh.")
    
#limpa os campos do formulario
def clear_form_fields(driver):
    try:
        # Limpa o campo CPF
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "CPF"))
        ).clear()

        # Limpa o campo Nome
        driver.find_element(By.ID, "Nome").clear()

        # Limpa o campo E-mail
        driver.find_element(By.ID, "E-mail").clear()

        # Limpa o campo Celular
        driver.find_element(By.ID, "Celular").clear()

        # Limpa o campo Data de Nascimento
        birth_date_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Data de nascimento*']"))
        )
        birth_date_field.clear()

        print("Campos limpos com sucesso!")
    except Exception as e:
        print(f"Erro ao limpar os campos do formulário: {e}")
        raise


# Identifica mensagens de erro
def identify_error_message(driver):
    try:
        # Aguarda que a mensagem de erro apareça
        error_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sc-3i1sdu-0"))  # Substitua pela classe correta do seu caso
        )
        print("Mensagem de erro encontrada:", error_element.text)
    except Exception as e:
        print("Nenhuma mensagem de erro foi encontrada ou erro ao buscar a mensagem:", e)

# Clica no botão "Abrir conta"
def click_open_account(driver):
    try:
        cpf_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "picpay-lp-parent-cpf-value"))
        )
        cpf_input.click()
        cpf_input.send_keys(Keys.ENTER)
        print("Campo CPF clicado e Enter pressionado!")
    except Exception as e:
        print(f"Erro ao clicar no campo CPF: {e}")
        raise

# Função principal
def main():
    driver = initialize_driver()
    try:
        # Abre o site
        driver.get("https://www.picpay.com")
        accept_cookies(driver)  # Aceita cookies, se necessário
        click_open_account(driver)  # Simula a interação com o campo CPF
        time.sleep(3)  # Pequena espera para o modal carregar

        print("--------teste todos os campos vazios-------")
        test_all_fields_void(driver)
        time.sleep(5)  # Espera para verificar respostas (opcional)
        clear_form_fields(driver)

        print("--------teste todos os campos preenchidos-------")
        test_all_fields_completes(driver) 
        time.sleep(5)
        clear_form_fields(driver)
        
    except Exception as e:
        print(f"Erro no fluxo principal: {e}")
    finally:
        driver.quit()  # Garante que o navegador será fechado

# Executa o código
if __name__ == "__main__":
    main()
