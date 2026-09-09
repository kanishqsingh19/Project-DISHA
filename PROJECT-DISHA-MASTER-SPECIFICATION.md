# Project DISHA — Master Specification

**Product:** Project DISHA  
**AI Assistant:** AURA  
**Document status:** Consolidated master specification  
**Purpose:** Source of truth for product, architecture, UX, security, roadmap, and MVP decisions.

---

## 1. Document Purpose

This document consolidates the major decisions made during the planning of Project DISHA and AURA.

It replaces scattered planning notes as the primary working specification. Individual future documents may expand sections of this specification, but they should not silently contradict it.

### Core rule

> Build AURA as a hybrid, user-controlled AI interaction layer—not as a simple chatbot or a wrapper around one AI provider.

---

# 2. Project DISHA

Project DISHA is the overall software/platform project.

Its purpose is to create a human-centered AI interaction layer through which a user can communicate naturally with an intelligent assistant and, where explicitly permitted, have that assistant perform useful computer and digital tasks.

DISHA is larger than a single model, API, or interface.

### DISHA aims to provide

- Natural human-computer interaction
- AI-assisted information and reasoning
- Multiple AI capabilities behind one experience
- Action/tool execution with permissions
- User-controlled memory
- Privacy and security by design
- A lightweight visual interface centered around the AURA Orb
- A modular architecture that can evolve over time

---

# 3. AURA

AURA is the intelligent AI assistant and companion inside Project DISHA.

AURA should feel like one coherent assistant even when different models, providers, tools, or local systems are used internally.

## 3.1 AURA's fundamental role

AURA should:

- Understand natural human language
- Answer general questions, including unrelated questions
- Maintain conversation context
- Handle follow-up questions
- Explain concepts and decisions
- Help with research and information gathering
- Coordinate multiple AI capabilities
- Perform approved digital/computer tasks
- Ask for clarification when required
- Ask for permission before sensitive actions
- Communicate what it is doing
- Report results honestly
- Admit uncertainty or failure instead of pretending success

AURA is not restricted to a fixed list of commands.

---

# 4. AURA Operating Principle

## Hybrid Mode Only

AURA has one user-facing operating concept:

> **Hybrid AURA**

The user does not need to select separate Local, Cloud, or Provider modes.

Internally, AURA may use:

- Local AI
- Cloud AI
- Specialized models
- External APIs
- Different AI providers

The user experiences these as one assistant.

### Conceptual flow

```text
USER
  ↓
AURA
  ↓
INTELLIGENCE ROUTER
  ↓
Appropriate AI capability
  ↓
AURA
  ↓
USER
```

The router may consider:

- Task type
- Conversation context
- Privacy requirements
- Hardware capability
- Latency
- Cost
- Reliability
- Provider availability
- Model capability

---

# 5. Provider Independence

AURA must not be architecturally dependent on one AI company or one model.

The system should be designed so providers can eventually be:

- Added
- Removed
- Replaced
- Compared
- Used as fallbacks

This creates flexibility for future model improvements, cost changes, outages, and new AI technologies.

AURA should abstract provider-specific implementation away from the user experience.

---

# 6. High-Level Architecture

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
                    ┌──────┼──────┐
                    ▼      ▼      ▼
                 LOCAL   CLOUD  SPECIALIZED
                    │      │      │
                    └──────┼──────┘
                           ▼
                      SKILL SYSTEM
                           │
                           ▼
                    TOOLS / APPS
                           │
                           ▼
                         RESULT
                           │
                           ▼
                       AURA ORB
```

Security and permission controls operate across the action/tool layer.

---

# 7. Conversation System

The Conversation Manager is responsible for turning user interaction into a coherent AURA experience.

It should support:

- Current conversation context
- Follow-up questions
- Intent understanding
- Clarification
- Response generation
- Tool/skill coordination
- Result reporting
- Appropriate interaction state

The conversation layer should not contain provider-specific logic wherever avoidable.

---

# 8. Intelligence Router

The Intelligence Router is the internal decision layer that determines which intelligence capability should handle a request.

### Example

A user asks a simple calculation:

```text
User
 ↓
AURA
 ↓
Router
 ↓
Calculator capability
 ↓
Answer
```

A complex research request may instead use:

```text
User
 ↓
AURA
 ↓
Router
 ↓
Cloud/specialized intelligence
 ↓
Research tools
 ↓
AURA
 ↓
Answer
```

The routing architecture should allow future policies without redesigning AURA.

---

# 9. Orb Interface

AURA does not use a permanent sidebar as its primary interface.

Instead, AURA is represented by a lightweight visual Orb.

## 9.1 Position

- Default position: bottom-right
- User can move the Orb anywhere on screen
- AURA may appear/pop up when needed
- The Orb should remain unobtrusive

## 9.2 Position memory

AURA should not permanently remember a custom Orb position automatically.

The user must explicitly request it, for example:

> “AURA, remember this position.”

This preserves user control.

## 9.3 Orb size

The user does not manually configure Orb size.

AURA should automatically determine an appropriate visual size based on:

- Screen
- Display context
- UI environment
- Device capability

---

# 10. Orb Visual Language

The Orb is not merely decoration.

Its animation communicates AURA's state.

### Core states

```text
IDLE
LISTENING
THINKING
WORKING
SPEAKING
```

### Meaning

**Idle:** AURA is available but inactive.

**Listening:** AURA is receiving user input.

**Thinking:** AURA is processing or reasoning.

**Working:** AURA is performing a task/tool action.

**Speaking:** AURA is delivering a response.

The visual language should make system activity understandable without requiring a permanent dashboard.

---

# 11. Skills and Actions

AURA should use a modular skill system.

Possible categories include:

- Calculator
- File operations
- Web research
- Productivity
- System utilities
- Application control
- Future integrations

Skills should be independently extendable.

Adding a new capability should not require rebuilding the AURA core.

## Action flow

```text
Intent
  ↓
Permission
  ↓
Skill / Tool
  ↓
Action
  ↓
Result
```

Sensitive operations should require explicit confirmation or an appropriate permission mechanism.

Examples include:

- Sending something
- Deleting important data
- Changing important settings
- Accessing sensitive information

---

# 12. Memory

AURA's memory must be user-controlled.

Memory should distinguish between:

### Temporary context

Information required to maintain the current conversation.

### Saved memory

Information intentionally retained beyond the immediate conversation.

### Preferences

User-approved preferences that improve future interaction.

The user should be able to request:

> “Remember this.”

and:

> “Forget that.”

AURA should not treat every conversation detail as permanent memory.

---

# 13. Privacy Principles

The guiding principle is:

> **Minimum necessary data + user control.**

AURA should:

- Prefer local processing where practical
- Use cloud processing where necessary
- Avoid unnecessary data collection
- Protect credentials
- Respect explicit permissions
- Keep provider selection abstracted from the user
- Give the user meaningful control over memory

Privacy is an architectural principle, not merely a settings-page feature.

---

# 14. Security

Security must be built into the architecture.

Key areas:

- Permission management
- Credential protection
- Sensitive-action confirmation
- Privacy boundaries
- Tool isolation where appropriate
- Honest action/result reporting
- Safe handling of external providers

AURA must never claim that an action succeeded when it did not verify success.

---

# 15. User Experience Principles

AURA should be:

- Natural
- Clear
- Helpful
- Fast where possible
- Honest about limitations
- Non-intrusive
- Visually distinctive
- User-controlled

The assistant should not expose unnecessary technical complexity.

The user should not need to understand:

- Which model was selected
- Which provider handled the request
- Which routing policy was used

unless that information becomes useful or the user asks for it.

---

# 16. MVP

The first working MVP should be intentionally limited.

### MVP components

1. AURA Orb
2. Text input
3. Voice input foundation
4. AI conversation
5. AI response
6. Orb state animations
7. Basic settings
8. Basic user-controlled memory
9. Hybrid architecture foundation

The MVP should prove the central interaction loop before expanding into advanced automation.

---

# 17. Development Roadmap

## Phase 0 — Project Setup

- Repository
- Documentation organization
- Technology stack
- Architecture skeleton
- Configuration structure
- Development conventions
- Git/GitHub setup

## Phase 1 — Basic AURA Core

- Core application structure
- Conversation foundation
- Input/output pipeline

## Phase 2 — Orb UI

- Orb rendering
- States
- Positioning
- Interaction
- Animation foundation

## Phase 3 — Voice/Text Interaction

- Text pipeline
- Microphone foundation
- Speech recognition
- Speech output

## Phase 4 — AI Connection

- Provider abstraction
- Initial AI connection
- Response pipeline

## Phase 5 — Conversation Engine

- Context
- Follow-ups
- Clarification
- Conversation state

## Phase 6 — Hybrid AI Router

- Routing layer
- Provider selection
- Local/cloud/specialized abstraction
- Fallback architecture

## Phase 7 — Skills and Actions

- Skill framework
- Tool execution
- Permissions
- Result handling

## Phase 8 — Memory

- Context memory
- User-approved long-term memory
- Preferences
- Forget controls

## Phase 9 — Security and Permissions

- Permission framework
- Credential handling
- Sensitive-action confirmation
- Privacy controls

## Phase 10 — Polish and Testing

- Reliability
- UX refinement
- Performance
- Error handling
- Testing

## Phase 11 — MVP

- Integrated working AURA
- Packaging
- Final MVP validation

---

# 18. What We Are NOT Building First

To prevent scope explosion, the initial development should not attempt everything simultaneously.

Do not begin with:

- Full autonomous computer control
- Every possible integration
- A complete emergency system
- Complex long-term memory
- Many AI providers simultaneously
- A massive UI
- Enterprise infrastructure
- Perfect voice recognition
- Every future feature

Build the core loop first.

---

# 19. Emergency / Future Capabilities

Emergency-oriented functionality may become a future capability.

Possible future concepts include:

- Fast interaction
- Configured emergency contacts
- Location-related functionality
- Minimal-interaction workflows
- Explicit permissions

This is **future functionality**, not an existing MVP capability.

Any implementation must receive dedicated safety, legal, privacy, and reliability design.

---

# 20. Technical Philosophy

Project DISHA should favor:

- Modularity
- Provider independence
- Clear interfaces
- Testability
- Security by design
- Privacy by design
- Incremental development
- Replaceable components
- Minimal unnecessary complexity

The architecture should make future change easier rather than harder.

---

# 21. Hardware Strategy

Project DISHA development can begin before the final development laptop is available.

### Without a laptop

We can prepare:

- Documentation
- Repository structure
- Architecture
- Configuration design
- Code skeletons
- Development specifications
- Git/GitHub organization
- Testing plans

### After laptop acquisition

We can execute and test:

- Desktop application
- Orb rendering
- Voice pipeline
- OS integration
- Local model execution
- Permissions
- Packaging
- Performance testing
- Full debugging

The project should not assume expensive local GPU hardware from day one.

---

# 22. Repository Direction

Initial repository:

```text
PROJECT-DISHA/
│
├── README.md
│
├── docs/
│   ├── foundation/
│   ├── architecture/
│   ├── product/
│   ├── ux/
│   ├── roadmap/
│   └── investor/
│
├── aura/
│   ├── core/
│   ├── conversation/
│   ├── router/
│   └── state/
│
├── ai/
│   ├── providers/
│   ├── local/
│   ├── cloud/
│   └── specialized/
│
├── skills/
│   ├── system/
│   ├── productivity/
│   ├── research/
│   └── utilities/
│
├── memory/
│   ├── context/
│   ├── long_term/
│   └── preferences/
│
├── security/
│   ├── permissions/
│   ├── privacy/
│   └── credentials/
│
├── ui/
│   └── orb/
│
├── tests/
│
└── config/
```

The master specification belongs under:

```text
docs/PROJECT-DISHA-MASTER-SPECIFICATION.md
```

---

# 23. Investor Positioning

Project DISHA should be presented as an AI interaction platform rather than simply a chatbot.

### Core positioning

> AURA is a next-generation AI interaction layer that hides model complexity behind a natural, intelligent, user-controlled experience.

Key differentiators:

- Hybrid intelligence
- Provider independence
- Natural interaction
- Action capability
- Visual Orb interface
- User-controlled memory
- Security and privacy by design
- Modular skill architecture

Investor materials must not present unverified traction, revenue, market-share, or financial claims as facts.

Unknown information should be marked:

`[TO BE VALIDATED]`

or

`[TO BE DETERMINED]`

---

# 24. Architectural Decisions — Current Baseline

The following decisions are considered established unless deliberately changed and recorded:

1. Project DISHA is the overall project.
2. AURA is the AI assistant inside DISHA.
3. AURA uses Hybrid Mode as its single user-facing architecture.
4. AURA can answer general/unrelated questions.
5. AURA is not limited to predefined commands.
6. AURA should be provider-independent.
7. AURA uses an Intelligence Router internally.
8. Local, cloud, and specialized intelligence can coexist.
9. There is no permanent sidebar as the primary AURA interface.
10. The Orb is AURA's primary visual interface.
11. Orb default position is bottom-right.
12. The user can move the Orb.
13. Custom Orb position is remembered only when explicitly requested.
14. Orb size is automatically determined.
15. Orb animation communicates system state.
16. Skills are modular.
17. Sensitive actions require permission/confirmation.
18. Memory is user-controlled.
19. Privacy follows minimum necessary data + user control.
20. Security is part of the architecture.
21. Emergency functionality is future scope.
22. Development proceeds incrementally through Phase 0 → Phase 11.

---

# 25. Change Management

If a future decision conflicts with this specification, do not silently overwrite the old decision.

Record:

- What changed
- Why it changed
- What parts are affected
- Date/version
- Whether implementation must change

This prevents architectural drift.

---

# 26. Current Project State

### Completed

- Project DISHA concept
- AURA concept
- Product direction
- Hybrid architecture decision
- Orb concept
- Interaction principles
- Memory concept
- Skills concept
- Security/privacy principles
- MVP direction
- Roadmap
- Investor positioning
- GitHub account
- Project DISHA GitHub repository

### Current phase

> **PHASE 0 — PROJECT SETUP**

### Immediate next milestone

> Organize this master specification in the GitHub repository, then finalize the technical stack and development architecture.

---

# 27. Final Principle

Project DISHA should grow from a strong foundation.

We are not trying to build every feature immediately.

We are building the architecture that allows AURA to become increasingly capable without losing:

- User control
- Simplicity
- Privacy
- Security
- Modularity
- Reliability
- Provider independence

**This document is the current master specification for Project DISHA and AURA.**
