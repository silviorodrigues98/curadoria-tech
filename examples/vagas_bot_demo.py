"""
vagas_bot_demo.py — Exemplo sanitizado da estrutura do Bot Telegram.
Mostra o fluxo de onboarding (área, nível, escopo) e registro no SQLite.
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Exemplo de handlers de demonstração para portfólio
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Olá, <b>{user.first_name}</b>! Bem-vindo à <b>Curadoria Tech</b>. 🚀\n\n"
        "Receba vagas de tecnologia 100% remotas e auditadas.",
        parse_mode="HTML"
    )

def main():
    # token omitido no exemplo de portfólio
    print("Bot de demonstração configurado.")

if __name__ == "__main__":
    main()
