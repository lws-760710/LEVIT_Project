# LEVIT_Project

LEVIT v2 infrastructure bootstrap (Phase 1).

## Stack

- **Backend**: Python 3.11+, FastAPI, LangGraph, Pydantic v2
- **Frontend**: Next.js, TailwindCSS

## Structure

- `/backend` - isolated Python backend package scaffold
- `/frontend` - isolated Next.js frontend app scaffold
- `/pyproject.toml` - centralized Python dependency + typing baseline
- `/.env.example` - configuration layer template to avoid hardcoded API keys
