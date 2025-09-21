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
        "url": "https://ohara.ai/mini-apps/miniapp_cmfnpr1es03fu9pnxgm8t3y2n?utm_source=rantai-nexus",
        "title": "🎭 Social Media"
    },
    "Halal Chain": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmfnpzgdy03h69pnxdy4z1y3z?utm_source=rantai-nexus",
        "title": "☪ Halal Chain"
    },
    "Travel Tycoon": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmfmwpqfq0bhm0anx6kly7pnz",
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
    if title:
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)

    # Hitung tinggi iframe yang sebenarnya
    iframe_height = height + hide_top + hide_bottom
    # Hitung posisi top iframe
    top_offset = -hide_top

    st.markdown(f"""
        <div style="height:{height}px; 
                    overflow:hidden; 
                    position:relative;">
            <iframe src="{src}" 
                    width="{width}" 
                    height="{iframe_height}px" 
                    frameborder="0"
                    style="position:relative; top:{top_offset}px;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)
    
def embed_lab(url: str, title: str = "", hide_top: int = 72, hide_bottom: int = 0, height: int = 720):
    if title:
        st.markdown(f"### {title}", unsafe_allow_html=True)

    # Tinggi iframe yang sebenarnya
    iframe_height = height + hide_top + hide_bottom
    # Offset untuk menyembunyikan bagian atas
    top_offset = -hide_top
    
    # Menggunakan components.html dengan logika yang sudah diperbaiki
    components.html(f"""
      <div style="position:relative;width:100%;height:{height}px;overflow:hidden;border-radius:12px;">
        <div id="loader"
             style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
                    font-weight:600;opacity:.6;transition:opacity .3s ease">
          Loading module…
        </div>

        <iframe id="ohara" src="{url}"
          style="position:absolute; top:{top_offset}px; left:0;
                 width:100%; height:{iframe_height}px;
                 border:0; border-radius:12px; overflow:hidden"></iframe>
      </div>

      <script>
        const ifr = document.getElementById('ohara');
        ifr.addEventListener('load', () => {{
          const l = document.getElementById('loader');
          if (l) {{
            l.style.opacity = 0;
            setTimeout(() => l.style.display = 'none', 300);
          }}
        }});
      </script>
    """, height=height) # Tinggi kontainer Streamlit
    
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
    ### 🧩 STC Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ☂ RANTAI Communities
    1. [Learn3](https://learn3.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    5. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    6. [Business Intelligence](https://rantai-busi.streamlit.app/)
    7. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    8. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    9. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    10. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    11. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    12. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    13. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    14. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    15. [Real-time Social Sentiment](https://rantai-rss.streamlit.app/)

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

# === Tab 2: Learn to Earn (iframe ke Ohara) ===
with tabs[2]:
    app = OHARA_APPS["Learn to Earn"]
    
# === Tab 3: Retro Games (iframe ke Ohara) ===
with tabs[3]:
    app = OHARA_APPS["Retro Games"]
    
# === Tab 9: DID Prototype (iframe ke Ohara) ===
with tabs[9]:
    app = OHARA_APPS["DID Prototype"]

# === Tab 1: Ferix Lab (iframe ke Ohara) ===
with tabs[1]:
    app = OHARA_APPS["Ferix Lab"]
   
# === Tab 5: Social Media (iframe ke Ohara) ===
with tabs[5]:
    app = OHARA_APPS["Social Media"]
    
# === Tab 6: Halal Chain (iframe ke Ohara) ===
with tabs[6]:
    app = OHARA_APPS["Halal Chain"]

# === Tab 4: Travel Tycoon (iframe ke Ohara) ===
with tabs[4]:
    app = OHARA_APPS["Travel Tycoon"]

# === Tab 8: Cultural DAO (iframe ke Ohara) ===
with tabs[8]:
    app = OHARA_APPS["Cultural DAO"]

# === Tab 7: Zakat Manager (iframe ke Ohara) ===
with tabs[7]:
    app = OHARA_APPS["Zakat Manager"]

# === Tab 10: NFT Marketplace (iframe ke Ohara) ===
with tabs[10]:
    app = OHARA_APPS["NFT Marketplace"]
    embed_lab(app["url"], app["title"], hide_top_px=110, hide_bottom_px = 50)
