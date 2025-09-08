# Git Workflow Documentation

## Branching Strategy
- **Main branch**: `main`
  - Always stable and production-ready.
  - Direct commits to `main` are not allowed.
- **Feature branches**: `feature/SCRUM-<ID>-description`
  - Example: `feature/SCRUM-3-git-workflow-doc`
- **Hotfix branches**: `hotfix/SCRUM-<ID>-description`

---

## Workflow

### Starting Work
```bash
git checkout main
git pull company main
git checkout -b feature/SCRUM-<ID>-description
