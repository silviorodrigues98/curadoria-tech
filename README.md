# Curadoria Tech — Bot de Vagas 100% Remotas 🚀

Bot do Telegram open-source / portfólio para entrega automatizada de vagas de tecnologia 100% remotas e auditadas.

## 🤖 O Projeto

O **Curadoria Tech** é um agente automatizado que varre fontes de vagas globais e brasileiras, valida se a vaga realmente está aberta (bypassando Cloudflare e testando o botão de candidatura), e as entrega no Telegram com base nas preferências do usuário (área, nível de senioridade e escopo geográfico).

👉 **Experimente o bot:** [t.me/curadoria_tech_bot](https://t.me/curadoria_tech_bot)

---

## 🛠️ Arquitetura e Stack

- **Linguagem:** Python 3.14
- **Interface:** Telegram Bot API (`python-telegram-bot` v20+)
- **Banco de Dados:** SQLite (`usuarios.db`) com espelho JSON para retrocompatibilidade
- **Verificação:** Playwright (headless Chrome com stealth para contornar Cloudflare)
- **Infância/Resiliência:** Task Scheduler do Windows com daemon de monitoramento e reinício automático
- **Logs:** Rastreamento estruturado por usuário (`logs/user_<id>.log`)

---

## 📋 Funcionalidades Principais

1. **Onboarding Guiado de 3 Passos:**
   - Passo 1: Área de atuação (Frontend, Backend, Fullstack, DevOps, Mobile, QA, Data, etc.)
   - Passo 2: Senioridade (Junior, Pleno, Senior, Especialista)
   - Passo 3: Escopo geográfico (Brasil, Global ou Ambos)
2. **Matching Inteligente:**
   - Algoritmo de pontuação e filtragem por palavra-chave com word-boundaries (evita falso positivo como `go` em `django`).
3. **Trial Ilimitado / Beta Público:**
   - Arquitetura preparada para monetização futura (campos `trial_days`, `free_until`, `status`), operando atualmente com trial ilimitado de 999 dias para o beta.
4. **Consentimento de Marketing:**
   - Pergunta integrada ao fim do onboarding para recebimento opcional de novidades sobre planos futuros.
5. **Logs de Testadores:**
   - Rastreamento por usuário para análise de engajamento e correção de fricções no funil.

---

## 📂 Estrutura do Repositório (Portfólio)

```
├── README.md               # Documentação e demonstração
├── requirements.txt        # Dependências do projeto
├── PLANO_BETA_GRATIS.md    # Planejamento do beta e modelo de trial
└── examples/               # Exemplos de código sanitizados (sem dados sensíveis)
    ├── vagas_bot_demo.py   # Estrutura dos handlers e onboarding
    └── job_matcher_demo.py # Lógica de matching e filtragem
```

> **Nota:** O código-fonte completo de produção e o banco de dados com dados de usuários reais não são versionados neste repositório por motivos de segurança e privacidade.

---

## 📄 Licença

Este projeto é disponibilizado para fins de portfólio. Todos os direitos reservados.
