

```markdown
# BookStore System

Este projeto é um sistema simples para gerenciar uma livraria, usuários e empréstimos de livros via linha de comando.

---

## Estrutura do Código

O código utiliza classes importadas do módulo `functions`:

- `BookStore`: Gerencia o cadastro e listagem de livros.
- `Users`: Gerencia criação e listagem de usuários.
- `Loan`: Gerencia empréstimos de livros.
- `Line`: Interface para comandos via linha de comando.

---

## Funcionalidades

### 1. Cadastrar livros

Comando: `cbook`

Exemplo:
```

cbook {"title": "Livro A", "author": "Autor X"}

```

Se o valor for válido, o livro será cadastrado.

### 2. Criar empréstimos de livros

Comando: `lbook`

Exemplo:
```

lbook 123 456

```

Onde `123` é o ID do usuário e `456` o ID do livro.

### 3. Listar livros emprestados de um usuário

Comando: `losbook`

Exemplo:
```

losbook 123

```

Mostra os livros emprestados pelo usuário com ID `123`.

### 4. Listar livros

Comando: `sbook`

Exemplo para listar todos os livros:
```

sbook

```

Exemplo para listar um livro específico:
```

sbook 456

```

### 5. Criar usuário

Comando: `cuser`

Exemplo:
```

cuser {"name": "João", "email": "[joao@example.com](mailto:joao@example.com)"}

```

Cria um usuário com os dados fornecidos.

### 6. Listar usuários

Comando: `suser`

Exemplo para listar todos os usuários:
```

suser

```

Exemplo para listar um usuário específico:
```

suser 123

```

---

## Como funciona o código

- Cada comando da linha de comando é registrado com a função `line.getCommand` ou `line.getTwoCommand`.
- Quando o comando é chamado, a função associada é executada com os valores passados.
- As funções manipulam as classes de livros, usuários e empréstimos para executar as operações solicitadas.
- Exemplo: ao executar `cbook`, chama `cadastroLivro(value)` que cria um novo livro.

---

## Requisitos

- Python 3.x
- Módulo `functions` contendo as classes necessárias (`BookStore`, `Users`, `Loan`, `Line`)

---

## Como executar

1. Importe o script principal.
2. Use a interface `Line` para enviar comandos conforme exemplos acima.
3. O sistema responderá com mensagens e resultados de acordo com o comando executado.

---

Se precisar de ajuda, entre em contato!
```


