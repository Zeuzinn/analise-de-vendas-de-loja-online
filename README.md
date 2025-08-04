# 🛍️ Análise de Vendas de Loja Online

Projeto em Python que simula a análise de dados de uma loja virtual de roupas, calçados e acessórios.

Foi utilizada **análise exploratória de dados (EDA)** para extrair insights de negócio, utilizando **Pandas** para manipulação de dados, **Matplotlib** para visualizações e um **menu interativo em terminal** para navegar pelas análises.

---

## 📊 Funcionalidades / Análises disponíveis

- 📅 Faturamento total por mês
- 🏬 Faturamento por loja
- 🌎 Faturamento por estado
- 🧢 Produtos mais vendidos
- 🧾 Categoria com maior faturamento
- 💸 Ticket médio por venda
- 📆 Melhor dia da semana para vendas

As análises podem ser acessadas de forma interativa via terminal.

---

## 🧰 Tecnologias utilizadas

- Python 3.10+
- Pandas
- Matplotlib

---

## 📁 Estrutura de Diretórios

```
analise-de-vendas-de-loja-online/
│
├── app.py
├── controllers/
│ └── interation.py
│
│
├── views/
│ ├── lojas.py
│ ├── produtos.py 
│ ├── vendas.py
│ └── visuals.py 
│
├── data/ 
│ ├── lojas.csv
│ ├── produtos.csv
│ └── vendas.csv
│
├── README.md
└── .gitignore
```

---
## 📌 Conclusões
- 🏆 A loja com maior faturamento foi a Loja A.

- 👕 A categoria com maior receita foi Roupas.

- 📈 O dia com maior volume de vendas foi a segunda-feira.

- 🔝 O produto mais vendido foi a Camiseta Básica.

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Zeuzinn/analise-de-vendas-de-loja-online.git
cd analise-de-vendas-de-loja-online
```

2. Instale as dependências (caso necessário):

```
pip install pandas matplotlib
```
3. Execute o projeto:

```
python app.py
```
---
