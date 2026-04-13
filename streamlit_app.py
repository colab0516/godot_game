import streamlit as st
import http.server
import socketserver
import threading
import os
import socket

# --- 1. 定義支援 Godot 4 的伺服器處理器 ---
class GodotRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 關鍵：加入這些 Header 才能讓多執行緒模式在瀏覽器跑起來
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

# --- 2. 啟動背景伺服器的函式 ---
def start_godot_server(path, port):
    os.chdir(path)
    handler = GodotRequestHandler
    # 使用 allow_reuse_address 避免重啟時埠口卡住
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

# --- 3. 獲取本機區域網路 IP (為了讓 iPhone 15 能連) ---
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

# --- 4. Streamlit 介面設定 ---
st.set_page_config(page_title="笨笨貓遊戲預覽器", layout="wide")

st.title("🎮 笨笨貓 Godot 遊戲預覽")

# 設定遊戲路徑
export_dir = r"D:\colab0516\GitPython\godot_game\HTML5"
game_port = 8001  # 避開 Streamlit 的 8501

if os.path.exists(export_dir):
    # 確保背景伺服器只啟動一次
    if 'server_started' not in st.session_state:
        thread = threading.Thread(
            target=start_godot_server, 
            args=(export_dir, game_port), 
            daemon=True
        )
        thread.start()
        st.session_state['server_started'] = True
        st.success(f"✅ 遊戲伺服器已在埠口 {game_port} 啟動")

    # 取得網址
    local_ip = get_local_ip()
    game_url = f"http://{local_ip}:{game_port}"

    # 顯示連線資訊（方便 iPhone 掃描）
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info(f"📱 手機請連同一 Wi-Fi 後訪問: `{game_url}`")
    with col2:
        if st.button("🔄 重新載入遊戲"):
            st.rerun()

    # --- 關鍵：使用 iframe 嵌入遊戲 ---
    st.components.v1.iframe(game_url, height=700, scrolling=False)

else:
    st.error(f"❌ 找不到遊戲資料夾：{export_dir}")
    st.info("請先確認 Godot 已經成功匯出 index.html 到該目錄。")