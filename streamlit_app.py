import streamlit as st
import http.server
import socketserver
import threading
import ssl  # 引入 SSL 模組
import os
import socket

# --- 1. 支援 HTTPS 的伺服器 ---
class SecureGodotHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=r"D:\colab0516\GitPython\godot_game\HTML5", **kwargs)

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

def start_https_server():
    port = 8443
    handler = SecureGodotHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    # --- 關鍵：注入 SSL 設定 ---
    # 注意：你需要有 cert.pem 和 key.pem
    # 如果沒有，可以用 OpenSSL 產生一組
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # 這裡指向你的憑證檔案
    # context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    
    # httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    st.write(f"🔒 HTTPS 伺服器嘗試在 {port} 啟動...")
    httpd.serve_forever()

# --- 2. Streamlit 介面 ---
st.title("🛡️ 安全環境檢查")
st.warning("iPhone 要求必須在 HTTPS 環境下才能執行 Godot 4 高階功能。")

# 這裡建議顯示一個連結，引導使用者去處理 HTTPS 轉發
st.info("💡 建議方案：使用 ngrok 或 localtunnel 自動產生 https 網址。")