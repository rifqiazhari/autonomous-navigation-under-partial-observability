# Autonomous Navigation Under Partial Observability

## Problem

An autonomous agent must navigate toward a goal in an environment that will eventually contain obstacles, incomplete observations, and uncertainty.

## Current Scope

The project currently implements a minimal 2D navigation environment with:

- An agent represented by a 2D position
- Four discrete actions: UP, DOWN, LEFT, RIGHT
- A fixed navigation goal
- Environment boundaries
- Static obstacles
- Movement validation
- Feedback for successful and blocked movements

## Current System

The agent proposes an action, which produces a candidate next position.
The environment determines whether that position is valid before the
agent's state is updated.

Current State → Action → Candidate State → Environment Validation → Next State

A movement is valid only if the candidate position:

1. Remains within the environment boundaries
2. Does not collide with an obstacle