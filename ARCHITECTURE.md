# Multi-Agent Insurance System - Architecture Design

## 1. System Overview

The Multi-Agent Insurance System is a collaborative agent-based architecture that leverages specialized AI agents to research and synthesize insurance policy information. The system uses CrewAI's built-in orchestration to manage agent coordination and task sequencing.

## 2. High-Level Architecture

```mermaid
graph TB
    Client[Client Application] --> API[API Gateway]
    API --> Crew[CrewAI Crew<br/>Built-in Orchestration]
    Crew --> Researcher[Researcher Agent]
    Crew --> Writer[Writer Agent]
    Researcher --> LLM[Ollama LLM]
    Writer --> LLM
    Researcher --> CrawlAPI[Crawl API]
    Researcher --> DB[(MongoDB<br/>Database)]
    Writer --> DB
    Crew --> StateManager[State Manager<br/>Optional]
    StateManager --> DB
```

## 3. Component Architecture

```mermaid
graph LR
    subgraph "CrewAI Orchestration"
        Crew[CrewAI Crew]
        Tasks[Tasks with Dependencies]
    end
    
    subgraph "Agent Layer"
        RA[Researcher Agent<br/>CrewAI Agent]
        WA[Writer Agent<br/>CrewAI Agent]
    end
    
    subgraph "Data Layer"
        DB[(MongoDB)]
        SM[State Manager<br/>Optional]
    end
    
    subgraph "External Services"
        LLM[Ollama LLM]
        CA[Crawl API]
    end
    
    Crew --> Tasks
    Tasks --> RA
    Tasks --> WA
    RA --> LLM
    WA --> LLM
    RA --> CA
    RA --> DB
    WA --> DB
    Crew --> SM
    SM --> DB
```

## 4. Agent Communication Flow

```mermaid
sequenceDiagram
    participant Client
    participant CrewAI
    participant Researcher
    participant Writer
    participant DB
    participant LLM

    Client->>CrewAI: Submit Research Request
    CrewAI->>Researcher: Execute Research Task
    Researcher->>LLM: Query Policy Coverage Info
    Researcher->>CrawlAPI: Fetch External Data
    Researcher->>DB: Store Research Findings
    Researcher->>CrewAI: Research Task Output
    CrewAI->>Writer: Execute Synthesis Task<br/>(with research context)
    Writer->>DB: Retrieve Research Data
    Writer->>LLM: Synthesize & Format
    Writer->>DB: Store Final Output
    Writer->>CrewAI: Synthesis Task Output
    CrewAI->>Client: Return Structured Output
```

## 5. Data Flow Architecture

```mermaid
flowchart TD
    Start[User Request] --> Parse[Parse Request]
    Parse --> Validate[Validate Input]
    Validate --> CreateCrew[Create CrewAI Crew]
    CreateCrew --> Research[Researcher Agent Task]
    Research --> Gather[Gather Information]
    Gather --> StoreRaw[Store Raw Data]
    StoreRaw --> CrewAI[CrewAI Task Context]
    CrewAI --> Synthesize[Writer Agent Task]
    Synthesize --> Format[Format Output]
    Format --> StoreFinal[Store Final Output]
    StoreFinal --> Return[Return to Client]
```

## 6. Technology Stack

| Layer | Technology |
|-------|-----------|
| Framework | CrewAI, LangChain |
| LLM | Ollama |
| Database | MongoDB |
| External API | Crawl API |
| Language | Python |
| State Management | Custom State Manager |

## 7. Key Design Principles

1. **Agent Specialization**: Each agent has a distinct role and responsibility
2. **CrewAI Orchestration**: Built-in task sequencing and agent coordination
3. **Task Dependencies**: CrewAI automatically handles data flow between tasks via context
4. **State Logging**: Optional state manager for monitoring and audit trails
5. **Fault Tolerance**: CrewAI's built-in error handling with optional custom retry logic

