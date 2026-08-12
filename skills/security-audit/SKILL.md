# Security Audit Skill

## Purpose

Perform security-focused analysis of software projects and identify potential vulnerabilities.

This skill helps AI agents review repositories for common security risks while maintaining safe analysis boundaries.

## Use Cases

* Open-source security reviews
* Repository auditing
* Dependency analysis
* Configuration review
* Secure coding assessment

## Input

The agent may analyze:

* Source code
* Configuration files
* Dependency manifests
* CI/CD workflows
* Documentation

## Workflow

## 1. Repository Analysis

Review:

* Project structure
* External dependencies
* Permission requirements
* Runtime environment

## 2. Vulnerability Detection

Identify:

### Credential Risks

Check for:

* API keys
* Tokens
* Passwords
* Private credentials

### Code Security Risks

Check for:

* Command injection
* Unsafe file operations
* Insecure deserialization
* Authentication weaknesses

### Dependency Risks

Review:

* Known vulnerable packages
* Unnecessary dependencies
* Suspicious package behavior

## 3. Agent-Specific Security

For AI agent workflows, check:

* Prompt injection risks
* Unsafe instructions
* Excessive tool permissions
* Uncontrolled external actions

## Output Format

```markdown
# Security Audit Report

## Risk Summary

Overall risk:

## Findings

Severity:

Location:

Description:

Recommendation:

## Security Improvements
```

## Safety Rules

The agent must:

* Never exploit discovered vulnerabilities
* Never execute destructive commands
* Never access secrets
* Never perform unauthorized network actions

## Goal

Improve software security through defensive analysis and responsible reporting.
