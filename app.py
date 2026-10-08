import random
import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "guess_input_id" not in st.session_state:
    st.session_state.guess_input_id = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = None

st.subheader("Make a guess")

st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

with st.form("guess_form"):
    raw_guess = st.text_input(
        "Enter your guess:",
        # A changed key clears the previous value after each submission or reset.
        key=f"guess_input_{st.session_state.guess_input_id}",
    )
    submit = st.form_submit_button("Submit Guess 🚀")

col1, col2 = st.columns(2)
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # Start a clean round and assign a fresh widget key to clear the old guess.
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.guess_input_id += 1
    st.session_state.feedback = {
        "level": "success",
        "message": "New game started.",
    }
    st.rerun()

if st.session_state.feedback:
    feedback = st.session_state.feedback
    if feedback["level"] == "error":
        st.error(feedback["message"])
    elif feedback["level"] == "success":
        st.success(feedback["message"])
    else:
        st.warning(feedback["message"])

if st.session_state.status != "playing":
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        # Invalid input must not consume an attempt or be added to history.
        st.session_state.feedback = {"level": "error", "message": err}
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)
        outcome = check_guess(guess_int, st.session_state.secret)

        if outcome == "Win":
            message = "🎉 Correct!"
        elif outcome == "Too High":
            message = "📉 Go LOWER!"
        else:
            message = "📈 Go HIGHER!"

        st.session_state.feedback = (
            {"level": "warning", "message": message} if show_hint else None
        )

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.session_state.feedback = {
                "level": "success",
                "message": (
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                ),
            }
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.session_state.feedback = {
                "level": "error",
                "message": (
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                ),
            }

    st.session_state.guess_input_id += 1
    st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
