import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="我的 Godot 遊戲")

st.title("🎮 我的遊戲")

# 讀取 HTML5 遊戲入口
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# 嵌入遊戲畫面
components.html(html_code, height=600, scrolling=True)