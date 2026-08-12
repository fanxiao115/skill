# Agent Workflow Example

## Example: Code Review Workflow

This example demonstrates how an AI agent can use a skill during software development.

## Scenario

A developer submits a pull request.

## Workflow

```
Developer
    |
    v
Pull Request
    |
    v
AI Agent
    |
    v
Code Review Skill
    |
    v
Review Report
```

## Input

The agent receives:

* Changed files
* Git diff
* Project context
* Existing coding rules

## Processing

The skill analyzes:

* Code quality
* Potential bugs
* Security concerns
* Maintainability

## Output

The agent produces:

* Review summary
* Issues found
* Suggested improvements

## Human Review

AI suggestions should be reviewed by maintainers before changes are merged.

## Security Considerations

The workflow should:

* Avoid executing untrusted code
* Protect credentials
* Require approval for repository changes
