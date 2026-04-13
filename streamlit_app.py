import streamlit as st
import os

# 取得目前腳本所在的目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "HTML5", "index.html")

st.title("🎮 笨笨貓遊戲預覽器")

if os.path.exists(html_path):
    # 讀取並顯示遊戲
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600, scrolling=True)
else:
    st.error(f"❌ 找不到遊戲檔案！")
    st.write(f"目前嘗試讀取的路徑是: `{html_path}`")