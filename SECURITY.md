# Security Policy

## Overview

Open Agent Skills is designed to provide reusable workflows for AI agents.

Because skills may influence agent behavior, tool usage, and automated workflows, security is treated as a core part of the project.

## Security Risks

Potential security concerns include:

### Prompt Injection

Malicious instructions inside skill definitions may attempt to override intended behavior or manipulate agent decisions.

### Unsafe Execution

Skills that interact with commands, files, or external services must avoid unsafe operations and unnecessary permissions.

### Credential Exposure

Skills must not contain:

* API keys
* Access tokens
* Passwords
* Private credentials

Sensitive information should always be handled through secure environment variables.

### Supply Chain Risks

Third-party contributions may introduce:

* Malicious code
* Hidden instructions
* Unsafe dependencies
* Unexpected network behavior

All contributions should be reviewed before merging.

## Reporting a Vulnerability

If you discover a security issue:

1. Do not publicly disclose the vulnerability immediately.
2. Provide a detailed description of the issue.
3. Include reproduction steps if possible.
4. Allow time for investigation and remediation.

## Security Principles

This project follows these principles:

* Least privilege
* Transparent workflows
* Reviewable instructions
* Minimal external access
* Safe automation practices
