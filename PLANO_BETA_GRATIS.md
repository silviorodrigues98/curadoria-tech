# Plano: Beta gratuito do Vagas Bot

## Objetivo

Validar a confiabilidade do bot, a qualidade das vagas e o interesse de usuários antes de lançar uma eventual oferta paga. O beta é gratuito e ilimitado durante a fase pública de testes, sem cobrança nem renovação automática.

## Oferta

- Acesso gratuito por tempo indeterminado durante o beta público (trial de 999 dias, `status: beta_unlimited`).
- Não há limite de participantes externos.
- Nenhum pagamento ou renovação automática durante o beta.
- Não há garantia de contratação nem de continuidade gratuita depois do beta.
- Os usuários podem, opcionalmente, consentir separadamente em receber uma mensagem sobre um eventual plano pago no futuro. Entrar no beta não significa consentir com marketing.

## Etapas

1. **Teste privado interno**
   - Validar `/start`, inscrição, entrega de vagas, qualidade e atualidade dos anúncios, links de candidatura e prevenção de duplicatas.
   - Verificar logs, tratamento de falhas e recuperação antes de divulgar o CTA.

2. **Abertura ao público (beta ilimitado)**
   - Publicar CTA informando acesso gratuito, sem limite de participantes e sem cobrança/renovação automática.
   - O bot aceita novos usuários livremente via `/start`.
   - Registrar a ativação somente após o usuário iniciar o bot e aceitar os termos do beta.

3. **Acompanhamento e avaliação**
   - Acompanhar entrega, erros, vagas inválidas ou repetidas e participação ativa.
   - Analisar logs por usuário (`logs/user_<id>.log`) para identificar fricções no onboarding e pontos de melhoria.
   - Solicitar feedback de forma opcional.

4. **Eventual oferta futura**
   - Não cobrar automaticamente.
   - Enviar uma oferta paga somente a quem tiver consentido separadamente em receber essa comunicação.
   - Respeitar pedidos para não receber mais mensagens.

## Dados mínimos

Guardar em `usuarios.db` (SQLite) com espelho em `user_profiles.json`:

```json
{
  "user_id": "5096578356",
  "name": "Nome informado pelo Telegram",
  "username": "username ou null",
  "status": "beta_unlimited",
  "joined_at": "ISO-8601 com fuso horário",
  "free_until": "2029-08-19",
  "trial_days": 999,
  "marketing_opt_in": 0,
  "area": ["frontend", "fullstack", "devops"],
  "seniority": ["junior", "pleno", "especialista"],
  "scope": "ambos",
  "active": 1,
  "updated_at": "ISO-8601 com fuso horário"
}
```

Valores de `status`: `beta_unlimited` (beta público), `paid_active` (futuro).

## Critérios para divulgação pública

- O bot responde ao `/start` de forma consistente.
- O cadastro registra consentimento para o beta (via onboarding de 3 passos).
- Entregas reais, links e proteção contra duplicatas foram verificados.
- O fluxo de falha e recuperação foi observado.
- Os logs por usuário estão ativos para análise de testadores.

## Estratégia do funil: LinkedIn, GitHub e bot

O funil transforma atenção em confiança e, depois, em uso do bot:

- **LinkedIn:** atrair audiência com conteúdo técnico, curadoria de vagas e CTA direto para o bot (`t.me/curadoria_tech_bot`).
- **GitHub:** repositório público como camada de prova de portfólio, contendo README, arquitetura e exemplos sanitizados (sem código de produção nem dados de usuários).
- **Telegram bot:** entregar o valor prático, com vagas remotas verificadas.

Mensagem central sugerida:

> Construí um sistema automatizado que encontra e valida vagas remotas de tecnologia. A engenharia pode ser acompanhada no GitHub e os resultados podem ser recebidos pelo bot.

### Distribuição recomendada de conteúdo

- **50% autoridade técnica:** automação, CDP, validação de vagas, Python, crons, agentes e recuperação de falhas.
- **30% curadoria de vagas:** uma vaga remota bem descrita por dia, com CTA para o bot.
- **20% produto e resultados:** como o bot funciona, para quem serve, como filtra vagas, exemplos anonimizados e resultados do beta.

Cada post deve contribuir para o funil, mas nem todo post deve vender. Usar CTA leve em aproximadamente dois de cada três posts e CTA direto em aproximadamente um de cada três posts após o lançamento.

### Papel do GitHub

O repositório público (`silviorodrigues98/curadoria-tech`) deve funcionar como camada de prova, contendo:

- README claro sobre o produto e sua arquitetura.
- Fluxo de coleta, validação e entrega.
- Exemplos de pipeline sanitizados (sem dados pessoais).
- Seção clara para testar o bot.
- Nenhum token, credencial, dado de usuário ou informação operacional privada.

Posts técnicos devem apontar para uma parte específica do GitHub quando houver relação direta. Não usar apenas o link da página inicial sem explicar o que o leitor encontrará.

## Estado

Este arquivo registra o modelo atualmente implementado: trial ilimitado (999 dias), sem limite de usuários, com marketing opt-in separado e logs por usuário.
