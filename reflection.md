# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game launched, but its feedback did not reliably match the guess. The high/low hint text was backwards, and comparing a guess with a secret that alternated between an integer and a string could produce incorrect results. Out-of-range guesses such as `-1` were accepted, and starting a new game could leave old game state or the previous input behind.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| With secret 24, guess 23 | Say the guess is too low and tell the player to guess higher | Hint text could say “Go LOWER!” even though the guess was lower | None |
| Enter `-1` (or a number above 100, such as `400`) | Show an out-of-range error; do not score or count an attempt | The value was accepted and treated as a low/high guess | None |
| Submit a guess, then start a new game or submit another guess | Start with a blank input and record each submitted guess once | Previous text/state could remain, making the input feel one turn behind or duplicated in history | None |

---

## 2. How did you use AI as a teammate?

I used Copilot in VS Code to investigate the import warning, refactor game rules into `logic_utils.py`, and test the UI behavior. One suggestion was to switch to `.venv-1`, where Streamlit was installed; it was not an effective fix in this workspace because Pylance remained on `.venv`, so I instead installed Streamlit in the active environment and confirmed the import diagnostic cleared. A useful suggestion was to reset the game fields and change the text-input widget key; Streamlit `AppTest` verified the new game reset and cleared input. I also used `AppTest` to check the behavior after reruns rather than assuming the UI feedback remained visible.

---

## 3. Debugging and testing your fixes

I ran `.venv\Scripts\python.exe -m pytest tests`; all 7 tests passed, covering the inclusive input bounds, out-of-range and non-integer inputs, and high/low comparisons. A Streamlit `AppTest` interaction check verified that `-1` shows an error without consuming an attempt, New Game resets the score/history/status and clears the input, and submitting `25` records exactly one guess and clears the field. That UI check initially exposed a feedback message disappearing on rerun, so I kept the feedback in session state and reran the check successfully. Pylance reported no diagnostics in `app.py`, `logic_utils.py`, or `tests/test_game_logic.py`.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns a script from the top when a user interacts with a widget. Values that should survive those reruns, such as the secret number, score, and attempts, belong in `st.session_state`; otherwise they may be recreated or lost. Widget keys also identify a particular input, so assigning a new key is a way to present a fresh input after a new round or submission.

---

## 5. Looking ahead: your developer habits

I want to keep writing small tests for boundary cases and then exercising the actual UI path, because the UI check found a rerun problem that the logic tests could not catch. Next time, I would check which interpreter VS Code is actually using before changing environments, and I would work through and commit each assignment phase separately. This project reminded me that AI-generated code and suggestions need to be reviewed against the codebase and verified with tests; a plausible change is not proof that the bug is fixed.
