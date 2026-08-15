# AI Telegram Assistant

AI Telegram Assistant — Telegram-бот на Python, который в дальнейшем будет интегрирован с LLM и расширен.

Проект разрабатывается как pet-project с фокусом на практическое применение технологий искусственного интеллекта, автоматизацию бизнес-задач и создание масштабируемой архитектуры.

## Current Status

**Version:** 0.1.0  
**Status:** In development

На текущем этапе реализована базовая инфраструктура Telegram-бота.

## Features

- [x] Telegram Bot
- [x] `/start` command
- [x] Message handling
- [x] Environment variables
- [x] Git version control
- [ ] LLM integration
- [ ] Conversation memory
- [ ] PostgreSQL
- [ ] RAG
- [ ] Document processing
- [ ] AI Agent
- [ ] Docker
- [ ] CI/CD

## Tech Stack

- Python 3.12
- aiogram
- python-dotenv
- Git
- GitHub

## Project Structure

```text
Bot_project/
│
├── src/
│   ├── config.py
│   │
│   └── bot/
│       ├── bot.py
│       └── handlers.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md