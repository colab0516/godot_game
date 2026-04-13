import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🎮 我的 Godot 遊戲")

components.iframe(
    "https://colab0516.github.io/godot_game/index.html",
    height=700,
    scrolling=True
)