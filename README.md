# ✅ To-Do List com Flask

Projeto simples desenvolvido para praticar lógica de programação e operações CRUD usando Python e Flask. Ideal para quem está começando no backend e quer entender o fluxo entre rotas, formulários e templates.

## 🚀 Funcionalidades

* Adicionar novas tarefas
* Marcar tarefas como concluídas
* Remover tarefas da lista
* Visualização dinâmica com atualização automática
* Frontend leve com HTML, CSS e ícones do Font Awesome

## 🛠 Tecnologias Utilizadas

* Python
* Flask
* Jinja2
* HTML5 + CSS3
* Font Awesome (para os ícones)

## 📁 Estrutura de Pastas

```bash
.
├── app/
│   ├── controllers/
│   │   └── tarefas_controller.py
│   │   └── home_controller.py
│   ├── services/
│   │   └── tarefas_service.py
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── tarefas.html
│   └──  config.py
├── run.py
└── requirements.txt
```

## 💻 Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/Ivysonin/to-do_list.git

# Acesse a pasta do projeto
cd to-do_list

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Windows)
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python run.py

# Acesse no navegador
http://localhost:5000/tarefas
```

## 📖 Aprendizados

Durante a construção desse projeto, o foco principal foi:

* Entender o fluxo de uma aplicação web simples com Flask
* Praticar conceitos de rotas, templates e redirecionamentos
* Trabalhar com formulários e métodos POST
* Organizar a aplicação com controllers e serviços separados
* Criar uma interface amigável com HTML + CSS customizado
* Evitar uso de banco de dados e sessions, focando puramente na lógica

## 📌 Observações

* O projeto **não utiliza banco de dados**, então as tarefas são armazenadas apenas em memória.
* Ideal para fins de estudo e prática de lógica com Python + Flask.
