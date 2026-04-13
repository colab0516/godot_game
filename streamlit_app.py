# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(layout="wide")

# st.title("🎮 我的 Godot 遊戲")

# components.iframe(
#     "https://colab0516.github.io/godot_game/index.html",
#     height=700,
#     scrolling=True
# )

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 使用 CSS 去除 Streamlit 頂部與側邊的空白 padding
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    iframe {
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎮 我的 Godot 遊戲")

# 設定匯出後的 docs/index.html 路徑（或你的網址）
# 加入 allow="fullscreen" 才能讓 Godot 內部的全螢幕按鈕生效
components.iframe(
    "https://your-username.github.io/your-repo-name/", 
    height=800, # 根據螢幕高度調整
    scrolling=False
)