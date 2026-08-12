# Agent Skill Specification

## Overview

This document defines the standard structure for skills in Open Agent Skills.

A skill is a reusable capability module that provides AI agents with structured instructions, workflows, and safety guidelines.

## Skill Structure

Each skill should contain:

```
skill-name/

└── SKILL.md
```

## SKILL.md Format

A skill should include the following sections:

```markdown
# Skill Name

## Purpose

Describe what problem this skill solves.

## Use Cases

Explain when agents should use this skill.

## Input

Define required information.

## Workflow

Describe step-by-step execution process.

## Output

Define expected results.

## Safety Guidelines

Describe security limitations.
```

## Design Principles

### Reusable

Skills should solve general problems instead of one-time tasks.

### Transparent

Agent behavior should be understandable and reviewable.

### Secure

Skills should minimize:

* unnecessary permissions
* external access
* hidden instructions
* unsafe automation

### Maintainable

Skills should include documentation and examples.

## Security Requirements

Skills must not contain:

* API keys
* Passwords
* Private tokens
* Hidden commands
* Destructive operations

## Review Process

New skills should be reviewed for:

* usefulness
* safety
* documentation quality
* maintainability
