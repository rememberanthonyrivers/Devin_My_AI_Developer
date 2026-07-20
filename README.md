# Mini Devin

> An autonomous multi-agent AI software engineer that analyzes repositories, plans implementation tasks, writes code, executes tests, fixes failures, and iterates until the job is complete.

---

## Overview

Mini Devin is an autonomous AI software engineering system inspired by tools like Devin, Cursor Agent, and OpenAI Codex.

Instead of acting as a simple code generator, Mini Devin behaves like an AI software engineer capable of understanding an existing codebase, planning changes, writing production-ready code, running tests, evaluating results, recovering from failures, and continuously improving until a task is successfully completed.

The project is designed as both a learning platform and a production-style architecture that demonstrates modern AI engineering techniques used in autonomous coding systems.

---

## Goals

- Analyze existing repositories
- Understand project architecture
- Build a dependency graph
- Create implementation plans
- Generate production-quality code
- Execute terminal commands
- Run automated tests
- Detect and recover from failures
- Learn from previous attempts
- Visualize the complete execution process

---

## Core Features

### Repository Intelligence

- Repository indexing
- Tree-sitter parsing
- Abstract Syntax Tree (AST) generation
- Dependency graph creation
- Semantic code search
- Code embeddings
- Long-context retrieval

---

### Planning Agent

- Task decomposition
- Goal planning
- Context gathering
- Reflection loops
- Memory management

---

### Coding Agent

- Code generation
- File editing
- Tool calling
- Terminal execution
- Git integration

---

### Evaluation Agent

- Test execution
- Failure detection
- Automatic retries
- Self-correction
- Iterative improvement

---

### User Dashboard

- Task timeline
- Agent activity
- Execution graph
- Repository visualization
- Live progress updates

---

## Planned Architecture

```
                        User
                          │
                          ▼
                  API (FastAPI)
                          │
                          ▼
                LangGraph Orchestrator
                          │
      ┌───────────────────┼────────────────────┐
      ▼                   ▼                    ▼
Repository Agent     Planning Agent      Memory Agent
      │                   │                    │
      └──────────────┬────┴──────────────┬─────┘
                     ▼                   ▼
                Coding Agent      Evaluation Agent
                     │                   │
                     ▼                   ▼
              Terminal Tools      Test Runner
                     │
                     ▼
               Git + Filesystem
```

---

## Tech Stack

### Backend

- Python
- FastAPI
- LangGraph
- Celery
- Redis
- PostgreSQL
- Docker

### AI

- Qwen 3 32B Instruct
- OpenAI-compatible APIs
- Tool Calling
- Structured Outputs
- Reflection Loops

### Code Intelligence

- Tree-sitter
- AST Parsing
- Qdrant
- Embeddings
- Retrieval-Augmented Generation (RAG)

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

---

## Project Structure

```
mini-devin/

backend/
│
├── app/
├── tests/
├── scripts/
├── requirements.txt
└── main.py

frontend/

docker/

docs/

.gitignore

docker-compose.yml

README.md

LICENSE
```

---

## Development Roadmap

### Phase 1

Repository Intelligence

- [ ] Scan repositories
- [ ] Build file tree
- [ ] Parse source code
- [ ] Generate dependency graph

---

### Phase 2

Planning System

- [ ] Multi-step planning
- [ ] Task decomposition
- [ ] Memory
- [ ] Reflection

---

### Phase 3

Coding Agent

- [ ] File editing
- [ ] Tool calling
- [ ] Terminal execution
- [ ] Git integration

---

### Phase 4

Evaluation

- [ ] Run tests
- [ ] Capture failures
- [ ] Retry automatically
- [ ] Self-correct

---

### Phase 5

Dashboard

- [ ] Live execution
- [ ] Agent visualization
- [ ] Repository explorer
- [ ] Timeline
- [ ] Logs

---

## Future Improvements

- Distributed workers
- Parallel task execution
- Multi-repository support
- Human approval workflows
- Long-term memory
- Voice interface
- Kubernetes deployment
- Cloud execution
- Automatic pull request generation
- Autonomous issue resolution

---

## Learning Objectives

This project explores concepts including:

- Autonomous AI Agents
- Multi-Agent Systems
- AI Planning
- Reflection Loops
- Context Engineering
- Retrieval-Augmented Generation (RAG)
- Tool Calling
- Function Calling
- Memory Systems
- Long Context Management
- Code Embeddings
- Software Architecture
- Evaluation Loops
- Autonomous Execution

---

## Inspiration

This project is inspired by recent advances in autonomous software engineering from organizations such as:

- OpenAI
- Anthropic
- Cognition
- Cursor
- Augment
- Factory AI
- Codeium

The implementation is built from first principles as an educational project to better understand the architecture behind autonomous coding agents.

---

## License

This project is licensed under the MIT License.

---

## Status

🚧 Currently under active development.

The project is being built incrementally, with each subsystem implemented and tested independently before being integrated into the full autonomous software engineering platform.