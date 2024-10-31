# Data Filtering Web Application

Este é um aplicativo web desenvolvido com Flask para filtrar e exibir dados de arquivos Excel de produtos Michael Kors e Fossil. A aplicação permite que os usuários consultem referências de produtos e apliquem filtros específicos para obter informações detalhadas.

## Funcionalidades

- **Carregamento de dados**: Carrega dados de dois arquivos Excel (`Michael Kors data.xlsx` e `Fossil Data.xlsx`), combinando-os em um único DataFrame para consulta.
- **Interface de pesquisa**: Usuários podem inserir múltiplas referências de produtos e aplicar filtros com base em descrições de produtos.
- **Filtro de termos específicos**: Filtra resultados com base em termos específicos, incluindo ajustes automáticos de filtro, como "caixa" que corresponde a "caixa" ou "parte central".
- **Tratamento de erros**: Página personalizada para erros 404.

## Pré-requisitos

- **Python 3.x**
- **Bibliotecas Python**:
  - `pandas`
  - `flask`
  - `waitress` (para servir o aplicativo em produção)

## Estrutura do Projeto

```plaintext
├── app.py                # Código principal da aplicação Flask
├── data
│   ├── Michael Kors data.xlsx
│   └── Fossil Data.xlsx  # Arquivos de dados Excel
├── templates
│   ├── index.html        # Página inicial com o formulário de busca
│   ├── resultados.html   # Página de resultados da pesquisa
│   └── erro.html         # Página de erro 404
└── README.md             # Este arquivo
