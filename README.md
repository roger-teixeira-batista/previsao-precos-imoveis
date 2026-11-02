# 🏠 Previsão de Preços de Imóveis em São Paulo

Aplicação web desenvolvida com **Python, Flask e Machine Learning** para estimar preços de imóveis localizados na cidade de São Paulo, a partir de características informadas pelo usuário.

O sistema utiliza um modelo de regressão treinado para realizar previsões de valores de imóveis com base em quatro variáveis de entrada.

## 🌐 Demonstração

<img width="1920" height="1030" alt="image" src="https://github.com/user-attachments/assets/be3981f0-aefc-4477-9eef-7d3abb736f69" />

**Acesse a aplicação:** [Previsão de Preços de Imóveis](https://previsao-precos-imoveis.onrender.com/)

## 🎯 Objetivo do Projeto

Desenvolver e disponibilizar uma aplicação web capaz de estimar o preço de imóveis em São Paulo utilizando um modelo de Machine Learning integrado a uma interface web.

O projeto demonstra a aplicação prática de técnicas de Ciência de Dados e Machine Learning em uma solução acessível por meio do navegador.

## ⚙️ Funcionalidades

- Interface web para inserção das características do imóvel.
- Processamento dos dados informados pelo usuário.
- Previsão de preços utilizando um modelo de regressão.
- Exibição do valor estimado em formato monetário brasileiro (R$).

### Variáveis utilizadas pelo modelo

| Feature | Descrição |
|---|---|
| Área do Imóvel | Área total do imóvel em metros quadrados (m²). |
| Valor do Condomínio | Valor mensal do condomínio em reais (R$). |
| Número de Quartos | Quantidade de quartos do imóvel. |
| Número de Suítes | Quantidade de suítes do imóvel. |

## 🛠️ Tecnologias e Ferramentas

- **Python:** linguagem utilizada no desenvolvimento do projeto.
- **Pandas:** manipulação e organização dos dados.
- **Scikit-learn:** utilização do modelo de Machine Learning.
- **Flask:** desenvolvimento do backend e integração com o modelo.
- **HTML:** construção da interface web.
- **Git e GitHub:** versionamento e gerenciamento do código.
- **Render:** hospedagem e disponibilização da aplicação web.

## 🧠 Modelo de Machine Learning

O sistema utiliza um modelo de regressão previamente treinado para estimar o preço de imóveis com base nas quatro variáveis de entrada.

O modelo é armazenado em formato `.pkl` e carregado pelo backend Flask durante a inicialização da aplicação.

## 📂 Estrutura do Projeto

```text
previsao-precos-imoveis/
│
├── model/
│   ├── modelo_simples.pkl
│   └── features_simples.names
│
├── templates/
│   └── home.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Executando o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/roger-teixeira-batista/previsao-precos-imoveis
```

### 2. Acesse a pasta do projeto

```bash
cd previsao-precos-imoveis
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

Windows:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python app.py
```

A aplicação estará disponível localmente em:

```text
http://127.0.0.1:5000
```

## ☁️ Deploy

A aplicação está hospedada na plataforma **Render**, utilizando Gunicorn como servidor WSGI para executar o backend Flask em ambiente de produção.

## 📌 Considerações

Este projeto possui finalidade demonstrativa e educacional, apresentando uma aplicação prática de Machine Learning integrada ao desenvolvimento web.

As previsões representam estimativas geradas pelo modelo e não devem ser interpretadas como avaliações oficiais ou garantias de valor de mercado.

---

**Desenvolvido como projeto de portfólio em Ciência de Dados e Machine Learning.**
