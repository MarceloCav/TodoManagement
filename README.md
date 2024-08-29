# Projeto Task Manager

## Visão Geral
Este é um projeto pessoal construído com Django, rodando em um contêiner Docker. O aplicativo permite aos usuários gerenciar tarefas e categorias por meio de uma interface amigável. Os usuários podem se registrar, fazer login, criar tarefas e categorias, marcar tarefas como concluídas e excluí-las.

## Funcionalidades
- **Autenticação de Usuário**: Os usuários podem se registrar e fazer login no aplicativo.
- **Gerenciamento de Tarefas**: Os usuários podem criar, visualizar, editar e excluir tarefas.
- **Gerenciamento de Categorias**: Os usuários podem criar, visualizar, editar e excluir categorias.
- **Filtragem de Tarefas**: As tarefas podem ser filtradas por status ou categoria usando filtros Django.
- **Comentários em Tarefas**: Os usuários podem adicionar comentários às tarefas.
- **REST API**: O aplicativo inclui uma REST API para gerenciar tarefas e categorias.
- **Frontend Responsivo**: O aplicativo usa AdminLTE para uma interface moderna e responsiva.
- **Paginação**: As listas de tarefas são paginadas para facilitar a navegação.
- **Perfil do Usuário**: Os usuários podem visualizar e editar seu perfil, incluindo a alteração de senha.
- **Testes Unitários**: Inclui testes para criação de usuários, criação de tarefas e outras funcionalidades principais.
- **Ambiente Dockerizado**: O projeto inclui Docker e Docker Compose para configuração e implantação fáceis.

## Instalação

### Pré-requisitos
- Docker
- Docker Compose

### Configuração
1. Clone o repositório:
    ```bash
    git clone https://github.com/your-username/task-manager.git
    cd task-manager
    ```

2. Construa e execute os contêineres Docker:
    ```bash
    docker-compose up --build
    ```

O aplicativo deve estar rodando em [http://localhost:8000](http://localhost:8000).

## Uso

### Autenticação de Usuário
- **Registrar**: Os usuários podem se inscrever para criar uma conta.
- **Login**: Os usuários fazem login para acessar as funcionalidades de gerenciamento de tarefas.

### Gerenciamento de Tarefas e Categorias
- **Criar Tarefa**: Adicione uma nova tarefa com um título, descrição e categoria.
- **Editar Tarefa**: Modifique os detalhes de uma tarefa existente.
- **Excluir Tarefa**: Remova uma tarefa da lista.
- **Marcar Tarefa como Concluída**: Marque uma tarefa como concluída.
- **Criar Categoria**: Adicione uma nova categoria para organizar as tarefas.
- **Filtrar Tarefas**: Use os filtros para encontrar tarefas com base em seu status ou categoria.

### Perfil do Usuário
- **Visualizar Perfil**: Acesse seu perfil de usuário.
- **Editar Perfil**: Atualize as informações do seu perfil ou altere sua senha.

### REST API
- **Endpoints**: O projeto inclui uma REST API para gerenciar tarefas e categorias. Verifique os endpoints `api/` para detalhes.


### Front
- **Front-end**: O front/telas/templates do projeto foram feitos a partir do https://adminlte.io/