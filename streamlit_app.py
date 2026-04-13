import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="我的 Godot 遊戲工廠")

st.title("🎮 笨笨貓遊戲預覽器")

# 假設你的 Godot 導出資料夾名稱是 "HTML5"
game_folder = "HTML5"
game_entry = "index.html"
game_path = os.path.join(game_folder, game_entry)

if os.path.exists(game_path):
    # 使用 components.html 嵌入 iframe，讓瀏覽器去讀取子目錄資源
    # 這是確保 .wasm 檔案能被找到的關鍵
    components.html(
        f"""
        <iframe 
            src="{game_path}" 
            width="100%" 
            height="720px" 
            style="border: 2px solid #4A90E2; border-radius: 10px;"
            allow="autoplay; fullscreen; shared-array-buffer"
        ></iframe>
        """,
        height=750,
    )
    st.success(f"✅ 成功偵測到遊戲入口：{game_path}")
else:
    st.error(f"❌ 找不到遊戲檔案！請確認 {game_folder} 目錄是否存在。")

st.info("💡 小撇步：如果遊戲黑屏，請在 Godot 導出設定中將 Variant 改為 'Single-Threaded'。")