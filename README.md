# Digital gland bot

Telegram-бот, который генерирует темы для лук-челленджа: `/challenge`.

Слова и шаблоны фраз лежат в `data.py`: их можно менять, не трогая код бота.

## Запуск

Токен берётся у @BotFather и передаётся через переменную окружения `BOT_TOKEN`.
В код его не пишем: репозиторий публичный.

```bash
pip install -r requirements.txt
BOT_TOKEN=<токен> python digital_gland_bot.py
```

Или в Docker:

```bash
docker build -t digital_gland_bot .
docker run -e BOT_TOKEN=<токен> digital_gland_bot
```

## На домашнем сервере (potato_home)

Бот описан в `bots/compose.yml` проекта potato_home и собирается прямо из этого
репозитория на GitHub. Обновить после `git push`:

```bash
docker compose build digital_gland_bot && docker compose up -d digital_gland_bot
```

`botstats.py` считает, как используют бота (сообщения, команды, пользователи, ошибки), и
отправляет это сервису botwatch. Без переменной `BOTWATCH_URL` он ничего не делает.
Это копия `bots/botstats.py` из potato_home.
