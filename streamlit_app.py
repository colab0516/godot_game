import streamlit as st
import os

# 1. 定義路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 假設你的遊戲檔案在專案根目錄下的 HTML5 資料夾
HTML_FILE = os.path.join(BASE_DIR, "HTML5", "index.html")

st.title("🎮 雲端版笨笨貓遊戲")

if os.path.exists(HTML_FILE):
    # 2. 讀取 HTML 內容
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 3. 嵌入遊戲
    # 注意：Godot 的 index.html 裡面引用了 index.js
    # 在 Streamlit Cloud 上，這通常需要把所有檔案放在 static 資料夾
    # 或是將 .js / .wasm 部署到 GitHub Pages，再用 iframe 連過去
    
    st.components.v1.html(html_content, height=600, scrolling=False)
else:
    st.error("找不到遊戲檔案，請確認 HTML5 資料夾已上傳至 GitHub")