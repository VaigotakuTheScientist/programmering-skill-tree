# Skill Tree

A small Python program for tracking learning progress for multiple users.

## Assignment requirements

The assignment says that the program must:

1. **Hantera mer än en användare** — the program supports multiple user profiles.
2. **Spara data så att användare kan komma tillbaka och fortsätta** — each user's skills and progress are loaded again when the program starts.
3. **Spara data permanent, lokalt** — data is stored locally in `users.json`.

## Features

- Create several users
- Switch between users
- Add skills
- Update progress from 0–100%
- Remove skills
- Show progress bars
- Save automatically after changes
- Continue from saved data after restarting the program

## Run the program

Make sure Python is installed, then run:

```bash
python main.py
```

The first time the program saves something, it creates `users.json` in the same folder as `main.py`.

## How the data is stored

Example local `users.json`:

```json
{
  "Vaigo": {
    "skills": {
      "Python": 70,
      "Physics": 40
    }
  },
  "Alice": {
    "skills": {
      "JavaScript": 30
    }
  }
}
```

`users.json` is intentionally ignored by Git because it represents local user data. The program itself remains in GitHub, while each computer keeps its own saved progress locally.

## Programming concepts used

- variables
- input/output
- `if` / `elif` / `else`
- `while` loops
- `for` loops
- functions
- dictionaries
- JSON
- reading and writing files
- error handling with `try` / `except`

## Project files

- `main.py` — the program
- `requirements.md` — the school requirements and how the program meets them
- `.gitignore` — prevents local user data and Python cache files from being committed
- `users.example.json` — example of the data format
