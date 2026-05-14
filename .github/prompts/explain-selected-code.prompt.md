---
description: "Explain selected code with structure, intent, and actionable improvements"
name: "Explain Selected Code"
argument-hint: "Optional focus (e.g., performance, bugs, security, beginner-friendly)"
agent: "agent"
---
Explain the user's selected code clearly and accurately.

Use this process:
1. Start with a 1-2 sentence plain-English summary of what the code does.
2. Break down the logic step by step (control flow, key conditions, data transformations).
3. Identify key symbols (functions/classes/variables) and their roles.
4. Call out assumptions, edge cases, and possible failure modes.
5. Suggest concrete improvements (readability, correctness, performance, maintainability).
6. If relevant, include a small example input/output walkthrough.

Input handling:
- Primary context is the user's selected code.
- If an optional argument is provided, prioritize that focus area while preserving overall explanation.

Output format:
- Keep explanations concise but complete.
- Use short sections and bullet points.
- Avoid speculation; if context is missing, state the uncertainty explicitly.
- Preserve technical accuracy over simplification.
