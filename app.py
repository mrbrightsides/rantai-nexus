import time
import requests
import datetime as dt
import pytz
import os
import pandas as pd
import streamlit as st
from streamlit.components.v1 import iframe
from html import escape

import streamlit as st
import streamlit.components.v1 as components

# ==== Ohara Miniapps ====
OHARA_APPS = {
    "Learn to Earn": {
        "url": "https://ohara.ai/mini-apps/13b468ca-644e-4736-b06f-2141861901ec?utm_source=rantai-nexus",
        "title": "🎸 Learn to Earn"
    },
    "Retro Games": {
        "url": "https://ohara.ai/mini-apps/b3f29b78-f623-4d9e-b0be-e81c7a8d5dd0?utm_source=rantai-nexus",
        "title": "👾 Retro Games"
    },
    "DID Prototype": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmfix4aur0g98nulkbdou3zlg?utm_source=rantai-nexus",
        "title": "🪪 DID Prototype"
    },
    "Ferix Lab": {
        "url": "https://ohara.ai/mini-apps/36b8c4fb-64ea-4f6d-8dec-3a632865b9ef?utm_source=rantai-nexus",
        "title": "🚗 Ferix Lab"
    },
    "Social Media": {
        "url": "https://ohara.ai/mini-apps/27ff0d99-01d2-4cff-ac22-adab36dbb5f8?utm_source=rantai-nexus",
        "title": "🎭 Social Media"
    },
    "Halal Chain": {
        "url": "https://ohara.ai/mini-apps/f3731395-8e3c-45e2-b222-c838ea3834d9?utm_source=rantai-nexus",
        "title": "☪ Halal Chain"
    },
    "Travel Tycoon": {
        "url": "https://ohara.ai/mini-apps/6f842cbf-3265-4a3a-921f-d16e70794123?utm_source=rantai-nexus",
        "title": "✈ Travel Tycoon"
    },
    "Cultural DAO": {
        "url": "https://ohara.ai/mini-apps/6302c6c4-4b49-4c30-9131-bb8d553fa7c5?utm_source=rantai-nexus",
        "title": "⚖️ Cultural DAO"
    },
    "Zakat Manager": {
        "url": "https://ohara.ai/mini-apps/3e563d43-387d-4f9b-9022-094f6e060172?utm_source=rantai-nexus",
        "title": "🕌 Zakat Manager"
    },
    "NFT Marketplace": {
        "url": "https://ohara.ai/mini-apps/09652207-5a8d-4a72-b409-cab19d4aa4f6?utm_source=rantai-nexus",
        "title": "🪙 NFT Marketplace"
    }
}

import streamlit as st
import streamlit.components.v1 as components

def iframe(src, height=720, width="100%", hide_top=0, hide_bottom=0, title=None):
    """
    Render iframe dengan opsi crop atas/bawah.
    """
    container_height = height - hide_bottom
    st.markdown(f"""
        <div style="height:{container_height}px; 
                    overflow:hidden; 
                    position:relative;">
            <iframe src="{src}" 
                    width="{width}" 
                    height="{height}px" 
                    frameborder="0"
                    style="position:relative; top:-{hide_top}px;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)

def embed_lab(url: str, title: str = "", hide_px: int = 72):
    st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)

    components.html(f"""
      <div id="wrap" style="position:relative;width:100%;height:100vh;overflow:hidden;border-radius:12px;">
        <div id="loader"
             style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
                    font-weight:600;opacity:.6;transition:opacity .3s ease">
          Loading module…
        </div>

        <!-- iframe full viewport -->
        <iframe id="ohara" src="{url}"
          style="position:absolute; top:-{hide_px}px; left:0;
                 width:100%; height:calc(100vh + {hide_px}px);
                 border:0; border-radius:12px; overflow:hidden"></iframe>
      </div>

      <script>
        // Loader fade-out saat iframe ready
        const ifr = document.getElementById('ohara');
        ifr.addEventListener('load', () => {{
          const l = document.getElementById('loader');
          if (l) {{
            l.style.opacity = 0;
            setTimeout(() => l.style.display = 'none', 300);
          }}
        }});
      </script>
    """, height=1080)
    
def embed_cropped(
    url: str,
    hide_px: int = 56,
    height: int = 720,
    hide_bottom: int = 100,
    title: str | None = None
):
    """
    Embed iframe dengan crop atas (hide_px) dan crop bawah (hide_bottom).
    """
    if title:
        st.markdown(f"### {escape(title)}", unsafe_allow_html=True)

    iframe_height = height + hide_px + hide_bottom
    top_offset = -hide_px if hide_px else 0

    components.html(
        f"""
        <div style="position:relative;width:100%;height:{height}px;overflow:hidden;border-radius:12px;">
          <iframe
            src="{escape(url, quote=True)}"
            style="position:absolute;top:{top_offset}px;left:0;width:100%;height:{iframe_height}px;
                   border:0;border-radius:12px;"
            scrolling="yes"
          ></iframe>
        </div>
        """,
        height=height + 16,
    )

if st.query_params.get("ping") == "1":
    st.write("ok"); st.stop()

# Quick CSS theme (dark + teal accents)
st.markdown("""
<style>
:root { --accent:#20c997; --accent2:#7c4dff; }
.block-container { padding-top: 1rem; }
section[data-testid="stSidebar"] .st-expander { border:1px solid #313131; border-radius:12px; }
div[data-testid="stMetric"]{
  background: linear-gradient(135deg, rgba(32,201,151,.08), rgba(124,77,255,.06));
  border: 1px solid rgba(128,128,128,.15);
  padding: 12px; border-radius: 12px;
}
.stButton>button, .stDownloadButton>button{
  border-radius:10px; border:1px solid rgba(255,255,255,.15);
}
.stTabs [data-baseweb="tab-list"] { gap: 6px; }
.stTabs [data-baseweb="tab"]{
  background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.08);
  border-radius: 10px; padding: 6px 12px;
}
[data-testid="stHeader"] { background: transparent; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/n1m1LJf.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    RANTAI Nexus adalah ruang bermain sekaligus ruang belajar, di mana fun bertemu focus, iman bertemu inovasi, wisata bertemu Web3, dan akademik bertemu eksperimen; semua terhubung lewat rantai ide-kode serta kolaborasi-aksi.
   
    Pilih modul dari navbar:
    1. Chat AI: Belajar dunia Web3 yang fun dan santai menggunakan AI
    2. Learn to Earn: Belajar musik menggunakan AI dan Klaim Hadiah menggunakan Web3
    3. Retro Games: 12 pilihan permainan klasik 8-bit yang bisa di hubungkan dengan pemain lainnya menggunakan Web3
    4. DID Prototype: Cikal bakal Decentralized Identification untuk KTP masa depan
    5. Ferix Lab: Menggambar mobil dan membandingkan karya dengan pengguna lainnya menggunakan Web3
    6. Social Media: Berinteraksi dengan pengguna lain menggunakan Web3
    7. Halal Chain: Menganalisa halalnya suatu restoran dalam supply chain menggunakan Web3
    8. Travel Tycoon: Permainan simulasi menjadi pengusaha pariwisata dengan teknologi Web3
    9. Cultural DAO: Memberikan dukungan berupa vote untuk budaya Indonesia menggunakan Web3
    10. Zakat Manager: Bersedekah lebih aman dan nyaman memanfaatkan teknologi Web3
    11. NFT Marketplace: Belanja souvenir berupa NFT dari tempat wisata yang ada di Indonesia 
    
    ---
    #### 🔮 Vision Statement
    RANTAI Nexus hadir sebagai ruang kolaboraksi yang menjembatani nilai iman, eksplorasi wisata, semangat akademik, dan inovasi Web3—menciptakan ekosistem belajar, bermain, dan berkreasi yang santai, inklusif, dan terhubung lewat teknologi blockchain.

    ---
    ### ❓ How to Log in
    Pastikan sudah memiliki wallet. Tiap modul merupakan app standalone jadi harus login di tiap modulnya untuk merasakan pengalaman maksimal dalam menjelajahi dunia Web3.
    
    ---
    ### 🎯 Leaderboard
    Beberapa modul disertai leaderboard yang berbeda-beda fungsi dan tujuannya. Tingkatkan peringkat dan bersaing dengan pengguna lain untuk menjadi yang terbaik.

    ---
    ### 🧩 RANTAI Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [SmartFaith](https://smartfaith.streamlit.app/)
    8. [Learn3](https://learn3.streamlit.app/)

    ---
    #### 🙌 Dukungan & kontributor
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/rantai-nexus)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

# ===== Page setup =====
st.set_page_config(
    page_title="RANTAI Nexus",
    page_icon="🌌",
    layout="wide"
)

col1, col2 = st.columns([2, 2])
with col1:
    st.markdown("""
        # Fun meets Focus on Nexus 🌌
    """)
with col2:
    st.markdown("""
        ## KOLABORAKSI — rumah semua eksperimen & modul Web3
    """)
st.markdown("""
        > 💡 Untuk tampilan dan pengalaman belajar yang optimal, disarankan menggunakan browser pada laptop atau PC untuk mengakses Nexus
    """)

# ===== Tab utama =====
tabs = st.tabs([
    "🤖 Chat AI", 
    "🎸 Learn to Earn",
    "👾 Retro Games",
    "🪪 DID Prototype",
    "🚗 Ferix Lab",
    "🎭 Social Media",
    "☪ Halal Chain",
    "✈ Travel Tycoon",
    "⚖️ Cultural DAO",
    "🕌 Zakat Manager",
    "🪙 NFT Marketplace"
])

# ===== Tab: Chatbot =====
with tabs[0]:
    st.subheader("🤖 Chat AI")
    st.markdown("""
        Tanya AI dan Admin tentang website ini.
    """)
        
    # --- Persist pilihan widget
    if "chat_widget" not in st.session_state:
        st.session_state.chat_widget = "Chat"  # default
    
    widget_opt = st.radio(
        " ",
        ["Chat", "Gateway"],
        horizontal=True, label_visibility="collapsed",
        index=["Chat","Gateway"].index(st.session_state.chat_widget),
        key="chat_widget"
    )
    
    URLS = {
        "Chat": "https://tawk.to/chat/68c62f434321191926759616/1j532h7vl",
        "Gateway":"https://rantai-nexus.vercel.app/"
    }
    chosen_url = URLS[widget_opt]
    
    cache_bust = st.toggle("Force refresh chat (cache-bust)", value=False)
    final_url = f"{chosen_url}?t={int(time.time())}" if cache_bust else chosen_url
    
    st.write(f"💬 Chat aktif: **{widget_opt}**")
    st.caption("Jika area kosong, kemungkinan dibatasi oleh CSP/X-Frame-Options dari penyedia.")
    
    iframe(src=final_url, height=720)
    
    if st.button(f"🔗 Klik disini jika ingin menampilkan halaman chat {widget_opt} dengan lebih baik"):
        st.markdown(f"""<meta http-equiv="refresh" content="0; url={chosen_url}">""", unsafe_allow_html=True)

# === Tab 1: Learn to Earn (iframe ke Ohara) ===
with tabs[1]:
    app = OHARA_APPS["Learn to Earn"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 2: Retro Games (iframe ke Ohara) ===
with tabs[2]:
    app = OHARA_APPS["Retro Games"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 3: DID Prototype (iframe ke Ohara) ===
with tabs[3]:
    app = OHARA_APPS["DID Prototype"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 4: Ferix Lab (iframe ke Ohara) ===
with tabs[4]:
    app = OHARA_APPS["Ferix Lab"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 5: Social Media (iframe ke Ohara) ===
with tabs[5]:
    app = OHARA_APPS["Social Media"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 6: Halal Chain (iframe ke Ohara) ===
with tabs[6]:
    app = OHARA_APPS["Halal Chain"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 7: Travel Tycoon (iframe ke Ohara) ===
with tabs[7]:
    app = OHARA_APPS["Travel Tycoon"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 8: Cultural DAO (iframe ke Ohara) ===
with tabs[8]:
    app = OHARA_APPS["Cultural DAO"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 9: Zakat Manager (iframe ke Ohara) ===
with tabs[9]:
    app = OHARA_APPS["Zakat Manager"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 10: NFT Marketplace (iframe ke Ohara) ===
with tabs[10]:
    app = OHARA_APPS["NFT Marketplace"]
    embed_lab(app["url"], app["title"], hide_px=100)
