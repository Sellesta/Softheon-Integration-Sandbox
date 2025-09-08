# Git Workflow Guide (SCRUM-3)

This document defines the branching strategy and workflow for the **Softheon-Integration-Sandbox** project.

---

## Branching Strategy
- **main** → Always stable. Production-ready code only.
- **feature/** → New features and tasks (e.g., `feature/SCRUM-3-git-workflow-doc`).
- **bugfix/** → Hotfixes and patches.
- **release/** → Used for preparing releases if needed.

---

## Workflow
1. **Sync main before starting work**
   ```bash
   git checkout main
   git pull company main
