"""
Телеграм-бот для генерации тем лук-челленджа.
Зависимости: pip install python-telegram-bot==20.*
Запуск:  BOT_TOKEN=<ваш_токен> python bot.py
         или задайте токен прямо в переменной BOT_TOKEN ниже.
"""

import random
import logging
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from data import COLORS, TEXTURES, MOODS, PLACES, ASSOCIATIONS, PHRASES

# ── Настройки ──────────────────────────────────────────────────────────────────
# BOT_TOKEN = os.getenv("BOT_TOKEN", "PASTE_YOUR_TOKEN_HERE")
BOT_TOKEN = ""

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ── Хелпер ─────────────────────────────────────────────────────────────────────
def generate_challenge() -> str:
    """Собирает одно случайное слово из каждой группы и возвращает готовый текст."""
    w1 = random.choice(COLORS)
    w2 = random.choice(TEXTURES)
    w3 = random.choice(MOODS)
    w4 = random.choice(PLACES)
    w5 = random.choice(ASSOCIATIONS)

    # Берём 4 слова из 5 групп в случайном порядке, чтобы каждый раз
    # комбинация была живой, а не всегда «цвет→текстура→…».
    words = random.sample([w1, w2, w3, w4, w5], 4)

    template = random.choice(PHRASES)
    return template.format(w1=words[0], w2=words[1], w3=words[2], w4=words[3])


# ── Обработчики команд ─────────────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "Привет! 👋\n\n"
        "Я генерирую темы для лук-челленджа.\n\n"
        "Команды:\n"
        "• /challenge — получить новую тему\n"
        "• /help — показать это сообщение"
    )
    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def challenge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = generate_challenge()
    await update.message.reply_text(message, parse_mode="Markdown")
    logger.info(
        "Challenge sent to user %s: %s",
        update.effective_user.id,
        message.replace("\n", " "),
    )


# ── Точка входа ────────────────────────────────────────────────────────────────
def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("challenge", challenge))

    logger.info("Бот запущен. Ожидаю команды…")
    app.run_polling()


if __name__ == "__main__":
    main()
