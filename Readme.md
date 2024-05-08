# CRAS App

Bem-vindo ao **CRAS App**! Este é um aplicativo que permite gerenciar usuários, seus cônjuges e filhos para um Centro de Referência de Assistência Social (CRAS). A aplicação foi desenvolvida usando Flask.

## Funcionalidades

- **Cadastro de Usuários**: Adicionar novos usuários com informações detalhadas.
- **Cadastro de Cônjuge e Filhos**: Registrar cônjuge e filhos vinculados ao usuário.
- **Edição de Dados**: Alterar os detalhes cadastrados de um usuário, cônjuge ou filho.
- **Exclusão de Usuários**: Remover usuários do sistema.

## Requisitos

- **Python** (3.8 ou superior)
- **Flask** (2.x.x)
- **SQLAlchemy** (1.4.x)
- Outros requisitos listados no arquivo `requirements.txt`.

## Instalação

1. **Clone o Repositório**:

    ```bash
    git clone https://github.com/seu-usuario/cras-app.git
    cd cras-app
    ```

2. **Crie e Ative um Ambiente Virtual** (opcional):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate  # Windows
    ```

3. **Instale as Dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o Banco de Dados**:

    Certifique-se de que a string de conexão no arquivo `app.py` está correta. Depois, inicialize o banco de dados:

    ```bash
    flask db upgrade
    ```

## Executando o Projeto

1. Inicie o servidor Flask:

    ```bash
    flask run
    ```

2. Acesse o aplicativo no seu navegador:

    - `http://127.0.0.1:5000`

## Estrutura do Projeto

- **`app.py`**: Arquivo principal com as rotas e a configuração do aplicativo.
- **`models.py`**: Definição dos modelos de dados usando SQLAlchemy.
- **Templates**:
    - **`register.html`**: Formulário para cadastro de novos usuários.
    - **`edit_user.html`**: Formulário para editar os dados de um usuário.
    - Outros arquivos HTML relacionados a cônjuge, filhos, etc.

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie um branch para a sua feature (`git checkout -b minha-feature`).
3. Faça o commit das suas alterações (`git commit -m 'Adiciona minha feature'`).
4. Faça um push do branch (`git push origin minha-feature`).
5. Crie um Pull Request.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
