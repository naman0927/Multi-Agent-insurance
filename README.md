# Multi-Agent Insurance System

## Project Overview

A collaborative multi-agent system for researching and synthesizing insurance policy information. The system features specialized agents (Researcher and Writer) that work together through CrewAI's built-in orchestration to deliver structured, high-quality outputs.

## Documentation

- **[ARCHITECTURE.md](./ARCHITECTURE.md)**: System architecture, component diagrams, and data flow
- **[LLD.md](./LLD.md)**: Low-Level Design document with detailed component specifications

## Key Features

- **Researcher Agent**: Sources policy coverage information from LLM and external APIs
- **Writer Agent**: Synthesizes and formats research data into structured outputs
- **CrewAI Orchestration**: Built-in task sequencing and agent coordination
- **State Management**: Optional logging and monitoring of workflow execution
- **Database**: MongoDB for document storage and workflow logging

## Technology Stack

- **Framework**: CrewAI, LangChain
- **LLM**: Ollama
- **Database**: MongoDB
- **External API**: Crawl API
- **Language**: Python

## Architecture Highlights

- Agent specialization with clear responsibilities
- CrewAI's built-in orchestration for task sequencing
- Automatic data flow between tasks via CrewAI context
- Scalable and fault-tolerant design

