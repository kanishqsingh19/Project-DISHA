# PROJECT DISHA

## AURA — The Next-Generation AI Interaction Layer

Project DISHA is a long-term AI platform designed to create a more natural, intelligent, and human-centered way to interact with computers.

At the center of DISHA is **AURA**, an intelligent AI assistant designed to understand natural language, answer questions, coordinate AI capabilities, and eventually perform approved actions across the user's digital environment.

---

## What is AURA?

AURA is the intelligent assistant inside Project DISHA.

AURA is designed to:

* Understand natural human conversation
* Answer general and domain-specific questions
* Handle follow-up conversations and context
* Explain information clearly
* Assist with research and information discovery
* Coordinate different AI capabilities
* Interact with applications and digital tools
* Ask for clarification when necessary
* Request permission before sensitive actions
* Communicate what it is doing
* Admit uncertainty instead of pretending an action succeeded

AURA is **not limited to a fixed list of commands**.

---

## Hybrid Intelligence

AURA is designed around a **Hybrid AI architecture**.

The user should not need to know which AI model or provider is being used.

AURA can intelligently coordinate:

* Local AI
* Cloud AI
* Specialized AI models
* External APIs
* Multiple future AI providers

Conceptually:

**User → AURA → Intelligence Router → AI Capability → AURA → User**

The Intelligence Router can consider factors such as:

* Task requirements
* Privacy
* Hardware capability
* Latency
* Cost
* Reliability
* Availability

This architecture is designed to prevent Project DISHA from becoming dependent on a single AI provider.

---

## The AURA Orb

AURA's primary visual interface is the **Orb**.

There is no requirement for a permanent sidebar.

The Orb is designed to:

* Appear when needed
* Start at the bottom-right of the screen
* Be movable anywhere on screen
* Automatically determine an appropriate size
* Remember a custom position only when explicitly requested by the user

The Orb is more than a visual element.

Its animation communicates AURA's current state:

**Listening → Thinking → Working → Speaking → Idle**

This creates a simple visual language between the user and the AI.

---

## Core Architecture

```text
                    USER
                      │
                      ▼
                  AURA ORB
                      │
                      ▼
             CONVERSATION MANAGER
                      │
                      ▼
          HYBRID INTELLIGENCE ROUTER
             ┌────────┼────────┐
             ▼        ▼        ▼
           LOCAL    CLOUD   SPECIALIZED
             │        │        │
             └────────┼────────┘
                      ▼
                 SKILL SYSTEM
                      │
                      ▼
              TOOLS / APPLICATIONS
                      │
                      ▼
                    RESULT
                      │
                      ▼
                  AURA ORB
```

Security and permission controls operate across the action layer.

---

## Skills & Actions

AURA will use a modular skill architecture.

Potential capabilities include:

* Web research
* Calculator
* File operations
* Productivity
* System utilities
* Application control
* Future external integrations

The architecture is designed so new capabilities can be added without rebuilding the entire AURA core.

Sensitive actions will require appropriate user permission or confirmation.

---

## Memory

AURA will distinguish between:

* Temporary conversation context
* Saved memory
* User preferences

Memory is designed around **user control**.

Users should be able to explicitly tell AURA:

> "Remember this."

or

> "Forget that."

AURA should not automatically treat every piece of information as permanent memory.

---

## Privacy & Security

Project DISHA follows the principle:

**Minimum necessary data + User control**

Key principles include:

* Explicit permissions
* Protected credentials
* User-controlled memory
* Privacy-aware AI routing
* Local processing when practical
* Cloud processing when necessary
* Provider independence
* Security built into the architecture

---

## MVP

The first working MVP will focus on the core experience rather than attempting to build everything at once.

### Initial MVP

1. AURA Orb
2. Voice/text input
3. AI conversation
4. AI responses
5. Orb animations
6. Basic settings
7. Basic memory
8. Hybrid AI architecture foundation

Advanced automation and integrations will be added progressively.

---

## Development Roadmap

### Phase 0 — Project Setup

Repository, documentation, architecture and development foundation.

### Phase 1 — AURA Core

Basic application structure and conversation foundation.

### Phase 2 — Orb UI

Visual Orb, states and animations.

### Phase 3 — Voice & Text

Input and output interaction.

### Phase 4 — AI Connection

Initial AI provider integration.

### Phase 5 — Conversation Engine

Context, follow-ups and response handling.

### Phase 6 — Hybrid AI Router

Local/cloud/specialized intelligence routing.

### Phase 7 — Skills & Actions

Modular tools and controlled computer interaction.

### Phase 8 — Memory

User-controlled memory system.

### Phase 9 — Security & Permissions

Permission architecture and protected actions.

### Phase 10 — Polish & Testing

Performance, reliability, UX and security testing.

### Phase 11 — MVP

A stable first public-ready version.

---

## What DISHA Is Not Building First

Project DISHA will not attempt to build every capability immediately.

The initial development will avoid:

* Full autonomous computer control
* Every possible integration
* Complex enterprise infrastructure
* Multiple AI providers simultaneously
* A complete emergency system
* Massive UI dashboards
* Perfect voice recognition
* Extremely complex memory

The priority is to build a strong foundation first.

---

## Long-Term Vision

Project DISHA aims to become an intelligent interaction layer between people and computers.

The long-term goal is for users to communicate naturally with their digital environment instead of learning complex software interfaces and commands.

AURA is intended to become the intelligent interface through which this interaction happens.

---

## Project Status

**Current stage:** Foundation & Architecture

The project is currently focused on:

* Product definition
* Architecture
* Documentation
* Repository setup
* MVP planning
* Technical preparation

Implementation will progress incrementally.

---

## Documentation

The current source of truth for the project architecture and product decisions is:

`docs/PROJECT-DISHA-MASTER-SPECIFICATION.md`

---

## Important Principle

> **AURA should make technology easier to interact with, not make the user learn more technology.**

---

**Project DISHA**
**AURA — Intelligent interaction, redesigned.**
