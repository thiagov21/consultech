import pandas as pd 
from flask import Flask, render_template, request 
from waitress import serve 

app = Flask(__name__)

# Carrega os arquivos Excel
df_MK = pd.read_excel('data/Michael Kors data.xlsx')
df_Fossil = pd.read_excel('data/Fossil Data.xlsx')
df_combined = pd.concat([df_MK, df_Fossil], ignore_index=True)

# Remove espaços dos nomes das colunas
df_combined.columns = [col.strip() for col in df_combined.columns]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados', methods=['POST'])
def resultados():
    # Obtém as referências e o filtro do formulário
    referencias_input = request.form.get('referencias', '')
    filtro = request.form.get('filtro', '').strip()

    # Processa as referências
    referencias = [ref.strip() for ref in referencias_input.split('\n') if ref.strip()]
    referencias = referencias[:50]

    # Verifica se há referências
    if not referencias:
        return render_template('resultados.html', resultados=[], filtro=filtro, referencias_input=referencias_input)

    # Busca inicial nas referências
    resultados_df = pd.DataFrame()
    for referencia in referencias:
        # Garante que 'referencia' seja uma string
        referencia = str(referencia)
        print(f"Buscando referência: {referencia}")  # Debugging
        mask = df_combined['Referencia'].str.contains(referencia, case=False, na=False)
        resultados_df = pd.concat([resultados_df, df_combined[mask]])

    # Aplica o filtro nas colunas 'Descrição' e 'Descrição Especifica'
    if filtro:
        filtro = str(filtro)
        print(f"Aplicando filtro: {filtro}")  # Debugging
        # Normaliza o filtro para buscar por termos específicos como "caixa" e "parte central"
        filtro_ajustado = filtro
        if filtro == "caixa":
            filtro_ajustado = "caixa|parte central"
        mask_descricao = resultados_df['Descrição'].str.contains(filtro_ajustado, case=False, na=False)
        mask_descricao_especifica = resultados_df['Descrição Especifica'].str.contains(filtro_ajustado, case=False, na=False)
        resultados_df = resultados_df[mask_descricao | mask_descricao_especifica]

    # Debugging: exibir o DataFrame após o filtro
    print(f"Resultados após filtro:\n{resultados_df}")

    resultados = resultados_df.to_dict('records')

    return render_template('resultados.html', resultados=resultados, filtro=filtro, referencias_input=referencias_input)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
