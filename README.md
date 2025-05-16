# 🧠 Sentiment Analyzer - FastAPI Microservice

A simple FastAPI-based microservice that performs sentiment analysis on user input text. Built with the 12-Factor App principles in mind.

---

## 🚀 Features

- REST API for sentiment analysis
- Docker & Docker Compose support
- Clean project structure
- GitHub Actions CI with test/lint steps
- Environment-based configuration using Pydantic
- Pytest test coverage
- Pre-commit hooks

---

## 🧪 API Endpoint

- `POST /api/v1/analyze`
```json
{
  "text": "I love working on this project!"
}
