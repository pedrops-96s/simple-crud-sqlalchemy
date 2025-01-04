# Projeto de Gerenciamento de Usuários com SQLAlchemy

Este é um projeto simples de gerenciamento de usuários utilizando o SQLAlchemy para interação com um banco de dados SQLite. O projeto permite realizar operações básicas de CRUD (Criar, Ler, Atualizar e Deletar) em uma tabela de usuários.

## Funcionalidades

- **Inserir um usuário:** A função `insert_usuario` permite cadastrar um novo usuário no banco de dados, com nome e tipo definidos.
- **Consultar usuários:** A função `select_usuarios` retorna a lista de usuários cadastrados. Também é possível buscar um usuário específico pelo nome.
- **Atualizar o nome de um usuário:** A função `update_nome_usuario` permite atualizar o nome de um usuário existente, dado o seu ID.
- **Deletar um usuário:** A função `delete_usuario` permite excluir um usuário pelo seu ID.

## Estrutura do Banco de Dados

A tabela de usuários possui os seguintes campos:

- **id** (Integer): Identificador único do usuário (chave primária).
- **nome** (String): Nome do usuário.
- **tipo** (String): Tipo de usuário (ex: 'Administrador', 'Convidado comum', etc.).

## Dependências

- **SQLAlchemy:** Biblioteca para interação com bancos de dados relacionais.
- **SQLite:** Banco de dados embutido utilizado para armazenar os dados dos usuários.

Para instalar as dependências, execute o comando:

```bash
pip install sqlalchemy
```

## Como Utilizar

### 1. Configuração do Banco de Dados

O banco de dados é configurado com o SQLite e o arquivo gerado é `database.db`. Caso o arquivo não exista, ele será criado automaticamente.

### 2. Funções

O arquivo contém várias funções que podem ser utilizadas para interagir com o banco de dados.

- **Inserir um usuário**  
  Para inserir um usuário, descomente a linha no final do código onde chama a função `insert_usuario` e passe os parâmetros desejados:

  ```python
  insert_usuario('Luky', 'Convidado comum')
  ```

- **Consultar usuários**  
  A função `select_usuarios` permite listar todos os usuários ou buscar um específico pelo nome. Exemplo de uso:

  ```python
  select_usuarios('Goku')  # Busca o usuário 'Goku'
  ```

- **Atualizar o nome de um usuário**  
  Para atualizar o nome de um usuário, utilize a função `update_nome_usuario` passando o ID do usuário e o novo nome. Exemplo de uso:

  ```python
  update_nome_usuario(2, 'Vegeta')
  ```

- **Deletar um usuário**  
  Para deletar um usuário, utilize a função `delete_usuario` passando o ID do usuário a ser deletado. Exemplo de uso:

  ```python
  delete_usuario(2)
  ```

### 3. Criando a Tabela

Ao executar o script pela primeira vez, a tabela de usuários será criada automaticamente, se ainda não existir, devido à chamada `Base.metadata.create_all(engine)`.

### 4. Executando o Script

Para rodar o script, execute o arquivo diretamente no terminal:

```bash
python script.py
```

Isso irá executar o script e mostrar o resultado das funções de consulta, inserção, atualização ou deleção, conforme o que está configurado no código.

## Exemplo Completo de Execução

No final do script, um exemplo de execução das funções está comentado:

```python
# Inserindo um usuário
# insert_usuario('Luky', 'Convidado comum')

# Consultando um usuário pelo nome
select_usuarios('Goku')

# Atualizando o nome de um usuário
# update_nome_usuario(2, 'Vegeta')

# Deletando um usuário
# delete_usuario(2)
```

Descomente e modifique essas linhas conforme necessário para realizar as operações.

## Considerações Finais

Este projeto é uma implementação simples de um sistema CRUD utilizando SQLAlchemy. Ele pode ser estendido para incluir mais funcionalidades, como validação de dados ou interação com diferentes tipos de bancos de dados.

Caso queira experimentar com outro banco de dados, basta alterar a string de conexão no código:

```python
engine = create_engine("sqlite:///database.db")  # Para SQLite
```

Você pode substituir o `sqlite:///database.db` por outros motores, como PostgreSQL ou MySQL, desde que instale as dependências correspondentes e altere a string de conexão adequadamente.

## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para abrir um pull request ou relatar problemas encontrados. 

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
