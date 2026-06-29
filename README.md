# 👤 Customer Registration Automation

> Automação do processo de cadastro de clientes, desenvolvida como projeto prático da trilha **Automação Inteligente para Negócios** — Senac Tech Porto Alegre RS.

---

## 📋 About the Project

This project automates the **customer registration workflow**, covering all stages from document collection to final registration confirmation.

The algorithm follows a structured **Input → Processing → Output** flow:

| Stage | Step | Description |
|---|---|---|
| **Input** | 1 | Request mandatory documents (CPF, RG, proof of address) |
| **Input** | 2 | Receive and digitize the customer's information into the system |
| **Processing** | 3 | Validate entered data (CPF format with 14 characters, required fields) |
| **Processing** | 4 | Check internal database for duplicate registrations |
| **Processing** | 5 | Generate a unique customer ID (e.g., CLI-4823) |
| **Processing** | 6 | Save validated information to the database |
| **Output** | 7 | Display "Registration Completed Successfully" and emit the registration receipt |

---

## 🐍 Python Concepts Applied

Este projeto aplica os seguintes conceitos de repetição em Python:

- **`while`** — mantém o sistema ativo enquanto houver tentativas disponíveis (máx. 3)
- **`for`** — percorre os campos obrigatórios para verificar preenchimento
- **`else`** (no `while`) — executado apenas quando o loop termina sem `break`, indicando tentativas esgotadas
- **`break`** — encerra o loop ao concluir o cadastro com sucesso ou ao usuário desistir
- **`continue`** — retorna ao início do loop para nova tentativa após erro de validação

---

## 🚀 How to Run

```bash
# Clone o repositório
git clone https://github.com/matheusscherer/customer-registration-automation.git

# Acesse a pasta do projeto
cd customer-registration-automation

# Execute o script
python customer_registration.py
```

### Test Cases

| CPF de teste | Resultado esperado |
|---|---|
| `123.456.789-09` | ⚠️ Duplicata — cliente já cadastrado |
| `987.654.321-00` | ⚠️ Duplicata — cliente já cadastrado |
| Qualquer CPF novo no formato correto | ✅ Cadastro realizado com sucesso |
| CPF com formato errado | ✘ Erro de validação |

---

## 🗂️ Project Structure

```
customer-registration-automation/
│
├── customer_registration.py   # Script principal da automação
└── README.md                  # Documentação do projeto
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `random` (nativa)
- **Paradigm:** Procedural com funções organizadas por etapa do fluxo

---

## 👨‍💻 Author

**Matheus Scherer** — Software Engineer | Automation & AI Specialist  
[@mtscfit](https://instagram.com/mtscfit) · [LinkedIn](https://linkedin.com/in/mtscfit) · [GitHub](https://github.com/matheusscherer)

---

*Projeto desenvolvido durante a aula de 22/06/2026 — Senac Tech Porto Alegre RS*
