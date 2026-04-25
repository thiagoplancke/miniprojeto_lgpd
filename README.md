# miniprojeto_lgpd

# 📊 Projeto LGPD — Anonimização e Tratamento de Dados

## 🧠 Contexto

Este projeto foi desenvolvido como parte da avaliação conjunta das disciplinas de **Estrutura de Dados** e **Linguagem de Programação II**, com foco na aplicação prática da **Lei Geral de Proteção de Dados (LGPD)**.

A LGPD estabelece diretrizes sobre como dados pessoais devem ser coletados, armazenados e tratados, garantindo **privacidade, segurança e transparência** no uso dessas informações.

---

## 🎯 Objetivo do Projeto

Simular um cenário real de tratamento de dados pessoais, aplicando técnicas de:

* 🔒 **Anonimização de dados sensíveis**
* 📁 **Organização e exportação de dados**
* ⚡ **Medição de desempenho**

---

## 🗄️ Fonte de Dados

Os dados são obtidos de um banco PostgreSQL contendo informações como:

* Nome
* CPF
* E-mail
* Telefone
* Data de nascimento

---

## 🧩 Estrutura do Projeto

O projeto está dividido em 4 atividades principais:

---

### 🔐 Atividade 1 — Anonimização de Dados

Implementação de uma função responsável por proteger informações sensíveis.

#### Regras de anonimização:

| Campo    | Transformação                                         |
| -------- | ----------------------------------------------------- |
| Nome     | Mantém a primeira letra, restante substituído por `*` |
| CPF      | Oculta parte dos números com `*`                      |
| E-mail   | Mantém domínio, anonimiza o usuário                   |
| Telefone | Mostra apenas os últimos dígitos                      |

💡 **Objetivo conceitual:**
Aprender que anonimização não é apagar dados, mas reduzir a possibilidade de identificação.

---

### 📂 Atividade 2 — Exportação por Ano

Geração de arquivos separados (CSV ou XLS), agrupando usuários por **ano de nascimento**.

📁 Exemplos:

* `1990.csv`
* `1991.csv`

✔️ Dados exportados devem estar **anonimizados**.

💡 **Insight importante:**
Aqui você pratica filtragem de dados + organização por critério específico.

---

### 📊 Atividade 3 — Exportação Completa

Criação de um único arquivo contendo todos os registros.

📁 Exemplo:

* `todos.csv`

✔️ Contém apenas:

* Nome
* CPF
  ❗ **Sem anonimização**

💡 **Reflexão:**
Nem sempre anonimizar é necessário — depende do contexto e finalidade dos dados.

---

### ⏱️ Atividade 4 — Medição de Tempo

Uso de um **decorador** para medir o tempo de execução das atividades 2 e 3.

✔️ Registro em logs do tempo gasto

💡 **Conceito-chave:**
Entender custo computacional e desempenho — essencial para sistemas reais.

---

## ⚙️ Tecnologias Utilizadas

* Python
* SQLAlchemy
* PostgreSQL
* Manipulação de arquivos (CSV/XLS)

---

## 🚀 Como Executar

1. Configure o ambiente Python
2. Instale as dependências necessárias
3. Utilize as credenciais fornecidas para acesso ao banco
4. Execute o script principal

---

## 📚 Aprendizados Esperados

Este projeto desenvolve habilidades fundamentais:

* Estruturação de dados
* Manipulação de banco de dados
* Boas práticas de segurança
* Pensamento crítico sobre privacidade
* Organização e exportação de dados
* Análise de desempenho

---

## 🧭 Próximos Passos (Sugestões)

Se quiser evoluir esse projeto:

* Implementar diferentes níveis de anonimização
* Criar interface simples para seleção de filtros
* Adicionar testes automatizados
* Trabalhar com grandes volumes de dados (escalabilidade)

---

## 🏁 Conclusão

Este projeto conecta teoria e prática ao mostrar como conceitos de proteção de dados são aplicados no desenvolvimento real. Mais do que cumprir a LGPD, ele ajuda a desenvolver uma mentalidade responsável sobre o uso de dados.

---
