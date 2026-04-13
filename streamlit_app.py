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

# 1. 寬版模式
st.set_page_config(layout="wide")

# 2. 注入 CSS 隱藏所有邊距、標題、選單，讓內容填充整個螢幕
st.markdown("""
    <style>
        /* 隱藏頂部標題、選單與底部資訊 */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 移除內容區域的 Padding */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        
        /* 讓 st.components.v1.iframe 的容器撐滿 */
        iframe {
            position: fixed;
            height: 100vh;
            width: 100vw;
            top: 0;
            left: 0;
            border: none;
            z-index: 999;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. 呼叫 iframe (網址填入你匯出的 Godot 遊戲路徑)
# 注意：height 雖然在這裡有設定，但會被上面的 CSS "100vh" 覆蓋，確保全螢幕
components.iframe(
    "https://colab0516.github.io/godot_game/index.html",
    scrolling=False
)