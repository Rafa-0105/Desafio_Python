from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def scrape_website():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get("https://www.vriconsulting.com.br/guias/guiasIndex.php?idGuia=22")

    tabela = navegador.find_element(By.XPATH, '//*[@id="corpoGuia"]/table[1]')
    linhas = tabela.find_elements(By.XPATH, 'tr')

    data = []
    for linha in linhas:
        celulas = linha.find_elements(By.XPATH, 'td')
        row_data = [celula.text for celula in celulas]
        data.append(row_data)

    navegador.quit()
    return data

@app.route('/tabela', methods=['GET'])
def get_tabela():
    dados = scrape_website()
    return make_response(
        jsonify(
            dados=dados,
            mensagem='Lista da tabela.'
        )
    )

@app.route('/tabela', methods=['POST'])
def create_registro():
    novo_registro = request.json
    dados = scrape_website()
    dados.append(novo_registro)
    return jsonify(
        mensagem='Registro com sucesso.',
        tabela=dados
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')