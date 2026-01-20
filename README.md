# AI Test Planning GitHub Workflow

This repository is an AI-assisted,
human-approved test planning pipeline.

## What this does

- Reads PR context (diff, description, comments)
- Uses an LLM to:
  1. Propose a **high-level test plan**
  2. Generate a **test structure**
- Requires **explicit human approval**
- Hands off final implementation to humans or local LLMs

## Workflow Overview

PR opened → AI Test Plan → Human Review  
Human Approval → AI Test Structure → Human Approval  
→ Local LLM / Human implements tests

## Required Secrets

| Name | Description |
|----|----|
| `LLM_API_KEY` | API key for OpenAI / Anthropic / Azure |

## Approval Commands (PR comments)

- `APPROVED_PLAN`
- `APPROVED_STRUCTURE`
- `REVISE_PLAN: <feedback>`
- `REVISE_STRUCTURE: <feedback>`

## Recommended Usage

- Cloud LLMs: planning & structure
- Local LLMs: code implementation
- Never auto-merge AI-generated code

## Supported Stacks

Language-agnostic  
Works with backend, frontend, data pipelines

