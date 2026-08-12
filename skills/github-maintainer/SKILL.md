
# GitHub Maintainer Skill

## Purpose

Assist open-source maintainers with repository management tasks.

This skill helps automate common maintenance workflows while keeping human approval in the loop.

## Use Cases

* Issue triage
* Pull request analysis
* Release preparation
* Changelog generation

## Input

The agent may receive:

* Issue descriptions
* Pull request information
* Commit history
* Repository documentation

## Workflow

## Issue Management

Analyze:

* Issue category
* Priority
* Reproducibility
* Required information

## Pull Request Review

Check:

* Code changes
* Documentation updates
* Testing information
* Security considerations

## Release Support

Generate:

* Release notes
* Change summaries
* Migration information

## Output

Provide structured recommendations.

Example:

```markdown
Category:

Priority:

Summary:

Recommended Action:
```

## Safety Guidelines

The agent must:

* Require approval before changing repository state
* Never merge code automatically
* Never modify permissions
* Never expose private repository data
