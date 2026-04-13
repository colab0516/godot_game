import streamlit as st
import http.server
import socketserver
import threading
import os
import socket

# --- 1. 自動偵測路徑 (解決 GitHub/本地路徑不一問題) ---
# 取得目前 streamlit_app.py 所在的資料夾路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 組合出 HTML5 的路徑
EXPORT_DIR = os.path.join(BASE_DIR, "HTML5")

# --- 2. 建立支援 Godot 4 的伺服器處理器 ---
class GodotRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # 這裡動態指定目錄，讓伺服器去 HTML5 資料夾找 index.html
        super().__init__(*args, directory=EXPORT_DIR, **kwargs)

    def end_headers(self):
        # 這些 Header 確保瀏覽器不會擋掉 WebAssembly 執行
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        # 防止快取，讓你更新遊戲後手機不會抓到舊檔案
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

# --- 3. 啟動伺服器的函式 ---
def run_game_server(port):
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), GodotRequestHandler) as httpd:
        httpd.serve_forever()

# --- 4. 獲取區域網路 IP (讓 iPhone 15 連線用) ---
def get_network_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

# --- 5. Streamlit 主介面 ---
st.set_page_config(page_title="笨笨貓遊戲預覽器", layout="wide")

st.title("🎮 笨笨貓 Godot 遊戲預覽")

if os.path.exists(EXPORT_DIR):
    # 設定一個固定的埠口來跑遊戲伺服器
    GAME_PORT = 8001
    
    # 確保伺服器只會啟動一次
    if 'server_running' not in st.session_state:
        thread = threading.Thread(target=run_game_server, args=(GAME_PORT,), daemon=True)
        thread.start()
        st.session_state['server_running'] = True

    # 取得網址
    ip = get_network_ip()
    game_url = f"http://{ip}:{GAME_PORT}"

    # 顯示連線資訊
    st.info(f"📱 iPhone 15 請連同一 Wi-Fi 後開啟: `{game_url}`")
    
    # 用 iframe 嵌入遊戲 (加上隨機參數 ?v=... 防止快取)
    import time
    st.components.v1.iframe(f"{game_url}?v={int(time.time())}", height=700)
    
else:
    st.error(f"❌ 找不到 HTML5 資料夾！")
    st.write(f"預期路徑: `{EXPORT_DIR}`")
    st.write("💡 請確認你已經將 Godot 遊戲匯出至該目錄。")