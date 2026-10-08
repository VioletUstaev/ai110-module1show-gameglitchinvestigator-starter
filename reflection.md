# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

Copilot helped identify the Streamlit state issue and move game rules into `logic_utils.py`. Its first suggestion was to switch to `.venv-1`, where Streamlit was installed, but Pylance continued using `.venv`, so that alone did not fix the import; installing Streamlit in the active `.venv` cleared the diagnostic. The logic refactor and validation changes were checked with pytest and a Streamlit `AppTest` interaction check. This showed me to verify that a proposed environment change actually changed the interpreter in use rather than assuming it did.

---

## 3. Debugging and testing your fixes

I ran `python -m pytest tests`; all 7 tests passed, including tests for valid bounds, out-of-range input, non-integer input, and numeric high/low comparisons. A Streamlit `AppTest` check verified that `-1` shows an error without consuming an attempt, New Game resets the game and input, and submitting `25` adds exactly one guess and clears the field. That UI check also caught that an immediate rerun hid feedback, so feedback is now kept in session state and shown after the rerun. Pylance reports no diagnostics in the edited Python files.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
