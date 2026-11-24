# Plano: Beta gratuito do Vagas Bot

## Objetivo

Validar a confiabilidade do bot, a qualidade das vagas e o interesse de usuários antes de lançar uma oferta paga. O beta oferece acesso gratuito por 30 dias, sem cobrança nem renovação automática.

## Oferta

- Participação gratuita por 30 dias a partir da ativação individual.
- Acesso termina automaticamente ao fim dos 30 dias, salvo decisão explícita de continuar após uma oferta paga.
- Nenhum pagamento ou renovação automática durante o beta.
- Limite inicial: até 10 participantes externos, após o teste privado interno.
- Não há garantia de contratação nem de continuidade gratuita depois do beta.
- Participantes podem, opcionalmente, consentir separadamente em receber uma mensagem sobre o plano pago após o beta. Entrar no beta não significa consentir com marketing.

## Etapas

1. **Teste privado interno por alguns dias**
   - Validar `/start`, inscrição, entrega de vagas, qualidade e atualidade dos anúncios, links de candidatura e prevenção de duplicatas.
   - Verificar logs, tratamento de falhas e recuperação antes de divulgar o CTA.
   - Só avançar quando o fluxo funcionar de ponta a ponta e a entrega real tiver sido confirmada.

2. **Abrir o beta limitado**
   - Publicar CTA informando claramente 30 dias grátis, limite de participantes, fim automático e ausência de cobrança/renovação automática.
   - O bot deve aceitar até 10 participantes beta; ao atingir o limite, informar que as vagas do beta estão preenchidas. Não prometer acesso gratuito a quem não foi admitido.
   - Registrar a ativação somente após o usuário iniciar o bot e aceitar os termos do beta.

3. **Acompanhar e avaliar**
   - Acompanhar entrega, erros, vagas inválidas ou repetidas e participação ativa.
   - Solicitar feedback de forma opcional.
   - Ao fim dos 30 dias, expirar o acesso beta. Se o sistema não puder impor a expiração de forma confiável, não divulgar o beta até essa capacidade estar implementada e testada.

4. **Oferta posterior**
   - Não cobrar automaticamente.
   - Enviar uma oferta paga após o beta somente a quem tiver consentido separadamente em receber essa comunicação.
   - Registrar a decisão e a data da comunicação; respeitar pedidos para não receber mais mensagens.

## Dados mínimos

Guardar em armazenamento local/API apropriado, com acesso restrito:

```json
{
  "user_id": 123456789,
  "name": "Nome informado pelo Telegram",
  "username": "username ou null",
  "status": "beta_active",
  "joined_at": "ISO-8601 com fuso horário",
  "free_until": "ISO-8601 com fuso horário",
  "marketing_opt_in": false,
  "marketing_opt_in_at": null
}
```

Valores de `status` sugeridos: `beta_active`, `beta_expired`, `paid_active`. Calcular `free_until` como 30 dias após a ativação, usando fuso horário explícito. Não armazenar email ou outros dados pessoais sem necessidade. Limitar acesso aos registros e definir retenção/exclusão conforme a finalidade e requisitos aplicáveis.

## Texto sugerido para o CTA (PT-BR)

> 🚀 **Teste grátis por 30 dias**
>
> Estamos testando um bot de vagas de tecnologia e vamos liberar acesso gratuito por 30 dias para até 10 participantes do beta. No fim do período, o acesso termina automaticamente — sem cobrança e sem renovação automática.
>
> Se você quiser continuar depois, poderá escolher uma opção paga, caso ela seja lançada. A participação não garante candidatura ou contratação.
>
> **Entre no beta:** `t.me/seu_bot`

## Critérios para divulgar

- O bot responde ao `/start` de forma consistente.
- O cadastro registra consentimento para o beta e aplica o limite de vagas.
- Entregas reais, links e proteção contra duplicatas foram verificados.
- Expiração após 30 dias e bloqueio de entregas para usuários expirados foram testados.
- O fluxo de falha e recuperação foi observado; não confiar apenas em compilação ou processo ativo.
- O CTA público não será ativado antes de esses critérios serem comprovados.

## Estratégia do funil: LinkedIn, GitHub e bot

O funil deve transformar atenção em confiança e, depois, em uso do bot:

- **LinkedIn:** atrair audiência com conteúdo técnico, curadoria de vagas e demonstrações reais.
- **GitHub:** provar que o sistema existe, é técnico e pode ser inspecionado.
- **Telegram bot:** entregar o valor prático, com vagas remotas verificadas.

Mensagem central sugerida:

> Construí um sistema automatizado que encontra e valida vagas remotas de tecnologia. A engenharia pode ser acompanhada no GitHub e os resultados podem ser recebidos pelo bot.

### Distribuição recomendada de conteúdo

- **50% autoridade técnica:** automação, CDP, validação de vagas, Python, crons, agentes e recuperação de falhas. CTA leve para um repositório, README ou exemplo específico no GitHub.
- **30% curadoria de vagas:** uma vaga remota bem descrita por dia, demonstrando a qualidade que o bot pretende entregar. O CTA do bot só entra depois da aprovação do lançamento público.
- **20% produto e resultados:** como o bot funciona, para quem serve, como filtra vagas, exemplos anonimizados e resultados do beta. CTA direto para o bot quando o fluxo estiver comprovado.

Cada post deve contribuir para o funil, mas nem todo post deve vender. Evitar repetir a mesma chamada em todas as publicações. Usar CTA leve em aproximadamente dois de cada três posts e CTA direto em aproximadamente um de cada três posts após o lançamento.

### Papel do GitHub

O repositório público deve funcionar como camada de prova, contendo:

- README claro sobre o produto e sua arquitetura.
- Diagrama ou explicação do fluxo de coleta, validação e entrega.
- Limitações conhecidas e critérios de qualidade.
- Exemplos de pipeline e screenshots sem dados pessoais.
- Seção clara para testar o bot.
- Nenhum token, credencial, dado de usuário ou informação operacional privada.

Posts técnicos devem apontar para uma parte específica do GitHub quando houver relação direta. Não usar apenas o link da página inicial sem explicar o que o leitor encontrará.

### CTA do lançamento para as primeiras 10 pessoas

Depois que os critérios de divulgação forem comprovados, usar uma mensagem transparente semelhante a esta:

> Estou testando um bot que encontra e filtra vagas remotas de tecnologia. Vou liberar acesso gratuito para as primeiras 10 pessoas durante 30 dias, sem renovação automática e sem cobrança. A ideia é validar a qualidade das vagas, o matching e a experiência de uso antes de abrir qualquer plano pago. Para participar, envie `/start` para `@seu_bot`.

O CTA deve deixar claro que:

- o limite é de 10 participantes externos;
- o acesso é individual por 30 dias;
- não existe cobrança nem renovação automática;
- o acesso pode terminar sem continuidade gratuita garantida;
- a participação não garante candidatura ou contratação;
- eventual comunicação sobre plano pago exige consentimento separado.

### Ordem de ativação

1. Manter as publicações atuais sem CTA do bot enquanto o teste privado continua.
2. Comprovar `/start`, cadastro, onboarding, matching, entrega, expiração e recuperação de falhas.
3. Publicar o CTA do beta para as primeiras 10 pessoas.
4. Ativar o CTA direto do bot apenas em posts selecionados, começando pelas vagas e posts de produto.
5. Medir início do bot, onboarding concluído, primeira vaga entregue, retenção, erros, expirações e interesse posterior em plano pago.
6. Revisar os dados antes de qualquer oferta paga ou expansão do limite.

## Estado

Este arquivo registra a proposta acordada; não indica que o fluxo já foi implementado ou que os testes foram concluídos. O progresso e o estado operacional devem ser atualizados em `PROGRESSO_CURADORIA_TECH.md` após implementação e verificação reais.
