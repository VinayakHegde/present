# zeroheight · Product Engineering Interview Prep

**Internal prep only** — not for presentation or sharing during the interview.

Open: [index.html](./index.html)

## Snapshot

| Field | Value |
|-------|-------|
| Company | zeroheight |
| Role | Senior AI Product Engineer |
| Stage | Product Engineering Interview |
| Topic | Developer Documentation Update System |
| Interviewers | Seth Corker & Chace Stewart |
| Duration | 1 hour |
| Setup | Fully remote · £110k+ |

**Mantra:** Trust first, automation later.

**Core line:** I would treat this as a trust and workflow problem first, and an AI generation problem second.

## Main framing

Human-in-the-loop documentation drift system:

1. Detect code changes (PR merged)
2. Identify potentially affected documentation
3. Generate explainable suggestions
4. User reviews, edits, accepts or rejects
5. Feedback improves future suggestions

**Not:** an AI bot that automatically rewrites and publishes documentation.

## MVP (in / out)

**In:** GitHub · one CMS · PR trigger · async jobs · doc index · retrieval · suggestions with evidence · review UI · CMS draft · feedback capture.

**Out:** auto-publish · multi-CMS · fine-tuning · multi-agent · perfect recall · full automation.

## Architecture (high level)

Repository event → Ingestion API → Event store → Job queue → Change classifier → Doc index → Relevance engine → Suggestion generator → Suggestion store → Review UI → CMS draft → Feedback store.

Side: auth, audit log, observability, retry/DLQ, admin view.

## Trust

- Draft-first · diff view · evidence · confidence · accept/edit/reject · rejection reasons · audit trail · no hidden changes.

## Core message

I would rather start with a system users trust and manually review, then earn the right to automate more later.

---
# Product requirement

## Introduction

We’re looking for **user-centric** product engineers that value **collaboration** and **teamwork** when solving problems. For this interview, you'll work through a product brief with 1 or 2 of our engineers and figure out how best to design and build a system.

We recommend spending **up to half an hour** before the interview researching the problem to better emulate a real world situation where you'd have alone thinking time, but please don't go overboard with prep - we want to respect your time.

You will be pitching your approach to our engineers, who will be asking clarifying questions, providing guidance and answering any questions you have. Come **prepared with any questions** and your initial ideas for tackling the problem.

## The problem

We want to build a system that helps teams keep their developer documentation up-to-date.

Developer documentation exists in a third-party headless CMS which has a public API.

The system should monitor changes in a codebase (for example, when a pull request is merged), understand what has changed, and suggest updates to the relevant documentation.

Users should be able to review, edit, and accept or reject these suggestions. Over time, the system should improve based on user feedback and past changes.

## User journeys

The system should support flows such as:

- A pull request is merged into a repository
- Our system detects the change and processes it
- A suggested documentation update is generated
- A user reviews and either accepts, edits, or rejects the suggestion
- Our system learns from this feedback and improves future suggestions

## What we care about

Please think about:

- The user experience and overall flow
- How the system evolves over time as changes happen
- How work is triggered and processed beyond a single interaction
- High-level architecture (frontend, backend, storage, integrations)
- How the system behaves when things go wrong
- Why a user would trust and act on the output

We are not looking for a highly optimised or large-scale system – focus on something that could realistically be built and operated early, while handling real-world behaviour over time.

## Communicating your ideas

We ask for you to have a drawing tool set up to illustrate your ideas while we discuss the problem. We don’t mind what tool; whatever you feel most comfortable using to sketch out ideas during the interview. Some examples are Google Drawings, Excalidraw, diagrams.net, miro, FigJam or Figma.

<aside>
⚠️ Please be prepared to share your screen. On Zoom you may need to grant permissions if this is your first time screen sharing.

</aside>