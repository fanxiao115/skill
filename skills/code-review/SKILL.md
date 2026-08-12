# Code Review Skill

## Purpose

Analyze software changes and provide structured code review feedback.

This skill helps AI agents review source code, pull requests, and patches by identifying potential bugs, security concerns, maintainability issues, and improvement opportunities.

## Use Cases

* Reviewing pull requests
* Analyzing code changes
* Finding potential bugs
* Improving code quality
* Detecting risky implementation patterns

## Input

The agent should receive:

* Source code files
* Git diff or pull request changes
* Project context
* Programming language information
* Existing coding standards (if available)

## Workflow

### 1. Understand Context

Analyze:

* Project structure
* Existing architecture
* Coding conventions
* Dependencies

### 2. Review Changes

Check:

* Logic correctness
* Error handling
* Performance concerns
* Code readability
* Maintainability

### 3. Security Review

Look for:

* Unsafe input handling
* Authentication problems
* Authorization issues
* Sensitive data exposure
* Dangerous API usage

### 4. Generate Report

Provide:

* Summary
* Critical issues
* Recommended improvements
* Risk assessment

## Output Format

```markdown
## Review Summary

Overall assessment:

## Issues Found

### Severity: High

Problem:

Location:

Recommendation:

## Suggestions

Improvement ideas:
```

## Safety Guidelines

The agent must:

* Never execute untrusted code during review
* Never expose credentials
* Never modify files without permission
* Clearly separate findings from assumptions

## Limitations

This skill provides automated assistance and should not replace human security review for critical systems.
