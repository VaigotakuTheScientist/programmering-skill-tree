# Assignment requirements

Original requirements:

> Den ska
>
> 1. Hantera mer än en användare
> 2. Spara data så att användare kan komma tillbaka och fortsätta
> 3. Spara data "permanent", lokalt

## How Skill Tree satisfies them

### 1. More than one user

The program stores several usernames in one dictionary. On startup, a person can select an existing user or create a new one.

### 2. Return and continue

Each user's skills and progress are loaded from `users.json` when the program starts. A returning user can therefore continue from the same progress.

### 3. Permanent local storage

The `save_users()` function writes the users dictionary to `users.json` on the computer. The information remains after the Python process ends and after the computer is restarted.
