# 💰 Assistente Virtual Financeiro com IA

## 📌 Sobre o projeto
Este projeto foi desenvolvido como parte do desafio final da DIO, com o objetivo de aplicar conceitos de Inteligência Artificial, experiência do usuário (UX) e desenvolvimento de sistemas interativos.

A proposta é criar um assistente virtual financeiro capaz de interpretar linguagem natural e auxiliar usuários na organização da vida financeira de forma simples e intuitiva.

---

## 🚀 Projeto Principal — Pilot AI

O **Pilot AI** é um assistente financeiro conversacional que permite registrar transações apenas escrevendo ou falando frases do dia a dia.

🔗 Acesse o projeto:
👉 moneypilot.lovable.app/app

---

## 💡 Como funciona

O usuário interage de forma natural, por exemplo:

- "Gastei 15 no almoço"
- "Recebi 2000 de salário"
- "Comprei um tênis por 300 em 3x"
- "Gastei 50 com a Maria"

O sistema interpreta automaticamente e transforma em dados estruturados:

- Tipo (receita ou despesa)
- Valor
- Categoria
- Data
- Parcelamento
- Associação com pessoas (familiares)

---

## 🧠 Arquitetura da solução

O projeto segue uma arquitetura moderna baseada em:

### 🔹 Frontend
- Interface de chat
- Entrada de texto e voz
- Experiência centrada no usuário

### 🔹 Backend (Edge Functions)
- Processamento da requisição
- Validação do usuário
- Integração com IA

### 🔹 Inteligência Artificial
- Interpretação de linguagem natural
- Conversão de frases em JSON estruturado
- Uso de modelo generativo (Gemini)

### 🔹 Banco de Dados
- Armazenamento de transações financeiras
- Categorias dinâmicas
- Relacionamento com usuários e familiares

---

## ⚙️ Fluxo da aplicação

1. Usuário envia uma mensagem (texto ou voz)
2. A mensagem é enviada para o backend
3. A IA interpreta a intenção e estrutura os dados
4. O sistema classifica (receita, despesa, parcelamento)
5. Os dados são salvos automaticamente
6. O usuário recebe confirmação no chat

---

## 🧪 Funcionalidades

- ✅ Registro automático de despesas e receitas
- ✅ Interpretação de linguagem natural
- ✅ Suporte a parcelamentos
- ✅ Reconhecimento de contexto (ex: familiares)
- ✅ Criação automática de categorias
- ✅ Interface conversacional

---

## 💻 Implementação complementar (Python)

Este repositório também inclui uma versão simplificada em Python para simular:

- Interação com usuário via terminal
- Respostas básicas sobre finanças
- Cálculo de juros compostos

### ▶️ Como executar

```bash
python main.py
