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

# ==== ELPEEF Miniapps ====
ELPEEF_APPS = {
    "Learn to Earn": {
        "url": "https://learntoearn.elpeef.com/?utm_source=rantai-nexus",
        "title": "🎸 Learn to Earn"
    },
    "Retro Games": {
        "url": "https://retrogames.elpeef.com?utm_source=rantai-nexus",
        "title": "👾 Retro Games"
    },
    "DID Prototype": {
        "url": "https://did.elpeef.com?utm_source=rantai-nexus",
        "title": "🪪 DID Prototype"
    },
    "Ferix Lab": {
        "url": "https://ferixlab.elpeef.com?utm_source=rantai-nexus",
        "title": "🚗 Ferix Lab"
    },
    "Social Media": {
        "url": "https://socialchain.elpeef.com?utm_source=rantai-nexus",
        "title": "🎭 Social Media"
    },
    "Halal Chain": {
        "url": "https://halalchain.elpeef.com?utm_source=rantai-nexus",
        "title": "☪ Halal Chain"
    },
    "Travel Tycoon": {
        "url": "https://traveltycoon.elpeef.com?utm_source=rantai-nexus",
        "title": "✈ Travel Tycoon"
    },
    "Cultural DAO": {
        "url": "https://culturaldao.elpeef.com?utm_source=rantai-nexus",
        "title": "⚖️ Cultural DAO"
    },
    "Zakat Manager": {
        "url": "https://waqf.elpeef.com?utm_source=rantai-nexus",
        "title": "🕌 Zakat Manager"
    },
    "NFT Marketplace": {
        "url": "https://nftmarketplace.elpeef.com?utm_source=rantai-nexus",
        "title": "🪙 NFT Marketplace"
    }
}

import streamlit as st
import streamlit.components.v1 as components

def iframe_with_mobile_notice(content_html, height):
    style = """
    <style>
      @media (max-width: 768px) {
          .hide-on-mobile { display:none!important; }
          .show-on-mobile {
              display:block!important;
              padding:24px 12px;
              background:#ffecec;
              color:#d10000;
              font-weight:bold;
              text-align:center;
              border-radius:12px;
              font-size:1.2em;
              margin-top:24px;
          }
      }
      @media (min-width: 769px) {
          .show-on-mobile { display:none!important; }
      }
    </style>
    """
    notice = '''
      <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
      </div>
    '''
    components.html(
        style +
        f'<div class="hide-on-mobile">{content_html}</div>' +
        notice,
        height=height
    )

def iframe(src, height=720, width="100%", hide_top=0, hide_bottom=0, title=None):
    if title:
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
    iframe_height = height + hide_top + hide_bottom
    top_offset = -hide_top
    content_html = f'''
        <div style="height:{height}px; overflow:hidden; position:relative;">
            <iframe src="{src}" width="{width}" height="{iframe_height}px"
                    frameborder="0"
                    style="position:relative; top:{top_offset}px;">
            </iframe>
        </div>
    '''
    iframe_with_mobile_notice(content_html, height)

def embed_lab(url, title="", hide_top=72, hide_bottom=0, height=720):
    if title:
        st.markdown(f"### {title}", unsafe_allow_html=True)
    iframe_height = height + hide_top + hide_bottom
    top_offset = -hide_top
    content_html = f'''
      <div style="position:relative;width:100%;height:{height}px;overflow:hidden;border-radius:12px;">
        <div id="loader"
            style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
                    font-weight:600;opacity:.6;transition:opacity .3s ease">
          Loading module…
        </div>
        <iframe id="ELPEEF" src="{url}"
          style="position:absolute; top:{top_offset}px; left:0;
                 width:100%; height:{iframe_height}px;
                 border:0; border-radius:12px; overflow:hidden"></iframe>
      </div>
      <script>
        const ifr = document.getElementById('ELPEEF');
        ifr.addEventListener('load', () => {{
          const l = document.getElementById('loader');
          if (l) {{
            l.style.opacity = 0;
            setTimeout(() => l.style.display = 'none', 300);
          }}
        }});
      </script>
    '''
    iframe_with_mobile_notice(content_html, height)
    
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
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    RANTAI Nexus adalah ruang bermain sekaligus ruang belajar, di mana fun bertemu focus, iman bertemu inovasi, wisata bertemu Web3, dan akademik bertemu eksperimen; semua terhubung lewat rantai ide dan kode, serta kolaborasi dan aksi.
   
    Pilih modul DApp dari navbar:
    1. Chat AI: Belajar dunia Web3 secara fun dan santai dengan AI multitalent.
    2. Learn to Earn: Eksperimen musik bareng AI, lalu klaim hadiah lewat Web3.
    3. Retro Games: Mainkan 12 game klasik 8-bit dan koneksikan skor dengan pemain lain via Web3.
    4. DID Prototype: Prototype identitas digital terdesentralisasi, cikal bakal KTP masa depan.
    5. Ferix Lab: Gambar mobil, adu kreasi, dan bandingkan karya lewat Web3.
    6. Social Media: Berinteraksi dan bangun jejaring sosial dengan dukungan Web3.
    7. Halal Chain: Analisis rantai pasok restoran untuk menilai status halal dengan Web3.
    8. Travel Tycoon: Jadi pengusaha pariwisata dalam game simulasi berbasis Web3.
    9. Cultural DAO: Dukung dan voting budaya Indonesia melalui DAO.
    10. Zakat Manager: Kelola zakat lebih aman, transparan, dan nyaman menggunakan Web3.
    11. NFT Marketplace: Koleksi souvenir digital berupa NFT dari destinasi wisata Indonesia.
    
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
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.ELPEEF.com/)

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
        # Fun meets Focus with Nexus 🌌
    """)
with col2:
    st.markdown("""
        ## KOLABORAKSI — rumah semua eksperimen & modul DApp Web3
    """)
st.markdown("""
        > 💡 Untuk tampilan dan pengalaman belajar yang optimal, disarankan menggunakan browser pada laptop atau PC untuk mengakses Nexus
    """)

# ===== Tab utama =====
tabs = st.tabs([
    "🤖 Chat AI",
    "🚗 Ferix Lab",
    "🎸 Learn to Earn",
    "👾 Retro Games",
    "✈ Travel Tycoon",
    "🎭 Social Media",
    "☪ Halal Chain",
    "🕌 Zakat Manager",
    "⚖️ Cultural DAO",
    "🪪 DID Prototype",
    "🪙 NFT Marketplace"
])

# ===== Tab: Chatbot =====
with tabs[0]:
    st.subheader("🤖 Chat AI")
    st.markdown("""
        Tanya AI seputar Web3 dengan vibes yang friendly.
    """)
        
    # --- Persist pilihan widget
    if "chat_widget" not in st.session_state:
        st.session_state.chat_widget = "Gateway"  # default
    
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

# === Tab 2: Learn to Earn (iframe ke ELPEEF) ===
with tabs[2]:
    app = ELPEEF_APPS["Learn to Earn"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -15)
    
# === Tab 3: Retro Games (iframe ke ELPEEF) ===
with tabs[3]:
    app = ELPEEF_APPS["Retro Games"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)
    
# === Tab 9: DID Prototype (iframe ke ELPEEF) ===
with tabs[9]:
    app = ELPEEF_APPS["DID Prototype"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)

# === Tab 1: Ferix Lab (iframe ke ELPEEF) ===
with tabs[1]:
    app = ELPEEF_APPS["Ferix Lab"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)
   
# === Tab 5: Social Media (iframe ke ELPEEF) ===
with tabs[5]:
    app = ELPEEF_APPS["Social Media"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)
    
# === Tab 6: Halal Chain (iframe ke ELPEEF) ===
with tabs[6]:
    app = ELPEEF_APPS["Halal Chain"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)

# === Tab 4: Travel Tycoon (iframe ke ELPEEF) ===
with tabs[4]:
    app = ELPEEF_APPS["Travel Tycoon"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -15)

# === Tab 8: Cultural DAO (iframe ke ELPEEF) ===
with tabs[8]:
    app = ELPEEF_APPS["Cultural DAO"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)
    
# === Tab 7: Zakat Manager (iframe ke ELPEEF) ===
with tabs[7]:
    app = ELPEEF_APPS["Zakat Manager"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)

# === Tab 10: NFT Marketplace (iframe ke ELPEEF) ===
with tabs[10]:
    app = ELPEEF_APPS["NFT Marketplace"]
    embed_lab(app["url"], app["title"], hide_top=0, hide_bottom = -25)
