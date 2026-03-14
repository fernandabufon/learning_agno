# 💼 Job Application Helper — Multi-Agent System with Agno

> A learning project built with the [Agno](https://docs.agno.com) framework, exploring multi-agent collaboration through a practical and relatable use case.

---

## 💡 Overview

**Job Application Helper** is a multi-agent application that helps users apply for jobs more effectively. The user provides a job listing and their resume, and a team of specialized agents works together to analyze the fit, critique the resume, and write a personalized cover letter — all displayed through an interactive Gradio interface.

---

## 🤖 The Agents

### `AnalystAgent`
Reads the job listing and extracts the most important requirements, responsibilities, and keywords that the employer is looking for.

### `CriticAgent`
Compares the user's resume against the requirements identified by the `AnalystAgent`, pointing out strengths, gaps, and areas where the candidate stands out or falls short.

### `WriterAgent`
Uses the analysis and the critique to write a compelling, personalized cover letter tailored to both the job and the candidate's profile.

---

## 🖥️ Interface — Gradio

The interface should allow the user to:

- Paste the **job listing** text
- Paste their **resume** text
- Click a button to **run the agent pipeline**
- See each agent's output in **separate tabs** as they finish
- **Download** the final cover letter

---

## ⚙️ Requirements

- Python 3.10+
- An **OpenAI API key**

### Dependencies

> 📝 Fill this in yourself as you set up the project.

### Environment Variables

> 📝 Fill this in yourself as you set up the project.

---

## 🚀 How to Run

> 📝 Fill this in yourself as you set up the project.

---

## 🧹 Code Constraints

These rules exist to make sure you write code that is clean, readable, and easy to maintain — not just code that works.

- **One file per agent** — each agent lives in its own file, never group them together
- **No logic in `app.py`** — the Gradio file should only handle the interface; all agent logic lives elsewhere
- **No hardcoded strings** — model names, instructions, and any configuration go into constants or a config file, never inline
- **Functions do one thing** — if a function is doing more than one job, split it
- **Meaningful names** — variables, functions, and files must clearly describe what they are (`get_job_requirements`, not `func1`)
- **No commented-out code** — if you don't need it, delete it
- **`.env` for secrets** — never write API keys directly in the code
- **Type hints everywhere** — all function parameters and return values must have type annotations
- **Docstrings on every function** — a single line explaining what the function does is enough
- **Consistent formatting** — use a formatter like `black` or `ruff` to keep the style uniform across all files

---

## 📚 What You Will Learn

- How to create agents with specific roles and instructions in Agno
- How to pass context between agents (one agent's output feeds the next)
- How to orchestrate multiple agents using an Agno Team
- How to build an interactive interface with Gradio
- How to structure a real-world AI application from scratch

---

## 🔗 Useful Resources

- [Agno Documentation](https://docs.agno.com)
- [Agno GitHub](https://github.com/agno-agi/agno)
- [Agno Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook)
- [Gradio Documentation](https://www.gradio.app/docs)

---

## 📄 License

MIT