import time
import requests
import datetime as dt
import pytz
import os
import pandas as pd
import streamlit as st
from streamlit.components.v1 import iframe

import streamlit as st
import streamlit.components.v1 as components

# ==== Ohara Miniapps ====
OHARA_APPS = {
    "Learn to Earn": {
        "url": "https://ohara.ai/mini-apps/13b468ca-644e-4736-b06f-2141861901ec?utm_source=rantai-nexus",
        "title": "🎸 Learn to Earn"
    },
    "Token Lab": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffpcnl10o678nlkgegfgpmn?utm_source=learn3",
        "title": "🧪 Token Lab"
    },
    "DAO Sandbox": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffptu29011cb3lkcmx6h3co?utm_source=learn3",
        "title": "🗳 DAO Sandbox"
    },
    "DeFi Workshop": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffqhjpu0173b3lkbvhh7arq?utm_source=learn3",
        "title": "💱 DeFi Workshop"
    },
    "Smart Contract Studio": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffs5rj50oz18nlk6ogi2lmp?utm_source=learn3",
        "title": "⚒️ Smart Contract Studio"
    },
    "Gas & Performance": {
        "url": "https://ohara.ai/mini-apps/e33686f2-bdec-4043-b683-0fd4507979b2?utm_source=learn3",
        "title": "⚡ Gas & Performance"
    },
    "Audit Security": {
        "url": "https://ohara.ai/mini-apps/0c47e8dd-0310-4bf6-8e02-c97612856385?utm_source=learn3",
        "title": "🔐 Audit Security"
    },
    "Web3 Lab": {
        "url": "https://ohara.ai/mini-apps/6a9f756b-573c-442c-9544-792660d7a86a?utm_source=learn3",
        "title": "🔗 Web3 Lab"
    },
    "Certification": {
        "url": "https://ohara.ai/mini-apps/e86a5136-f96f-4d52-af61-8de234ed7686?utm_source=learn3",
        "title": "🎓 Certification"
    }
}

import streamlit as st
import streamlit.components.v1 as components

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
    
def embed_cropped(url: str, hide_px: int = 56, height: int = 720, title: str | None = None):
    """Embed iframe dengan 'crop' area atas setinggi hide_px (untuk menyamarkan header)."""
    if title:
        st.markdown(f"### {title}")
    components.html(
        f"""
        <div id="wrap" style="position:relative;width:100%;height:{height}px;overflow:hidden;border-radius:12px;">
          <iframe
            src="{url}"
            style="position:absolute;top:-{hide_px}px;left:0;width:100%;height:{height + hide_px}px;border:0;border-radius:12px;overflow:hidden"
            scrolling="no"
          ></iframe>
        </div>
        """,
        height=height,
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
        "https://i.imgur.com/E5LaGaa.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    RANTAI Nexus adalah rumah pusat untuk semua eksperimen RANTAI: 
    edukasi, sandbox, demo, game, simulasi, dan lain-lain.
    Pilih modul dari navbar

    Showcase dan dokumentasi ada disini [Doc](https://learn3showcase.vercel.app)
    
    ---
    #### 🔮 Vision Statement
    User belajar lewat chatbot AI, latihan simulasi DeFi & DAO, eksperimen smart contract, hingga riset cutting-edge seperti zkML.
    Setiap langkah terhubung dengan ekosistem STC (GasVision, Bench, Converter, Analytics) untuk pengalaman nyata.
    Di akhir perjalanan, user mendapatkan sertifikat Soul Bound Token (SBT) eksklusif — bukti abadi di blockchain bahwa mereka adalah bagian dari pionir Web3.

    ---
    ### ❓ How to Get the Badges
    Terdapat 10 Badge di seluruh modul yang tersebar untuk didapatkan. Jelajahi modul per modul untuk mencarinya. Kumpulkan minimal 6 Badge maka kamu berhak untuk claim sertifikat 🎓
    
    ---
    ### 🎯 Quiz Leaderboard
    Quiz disini hanya bersifat simulasi dan latihan. 
    Klik [join](https://wayground.com/join?gc=53764642) agar kamu bisa simpan progress, isi nama dan avatar sendiri, serta bandingkan peringkatmu dengan peserta lainnya. 
    Untuk mengeklaim Badge, sebaiknya masukkan nama asli disertai dengan email yang valid saaat mengisi nama peserta quiz.

    ---
    ### 🧩 STC Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)

    ---
    #### 🙌 Dukungan & kontributor
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/learn3)
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
    page_title="Learn3",
    page_icon="🚀",
    layout="wide"
)

col1, col2 = st.columns([2, 2])
with col1:
    st.markdown("""
        # Welcome to RANTAI Nexus 🌌
    """)
with col2:
    st.markdown("""
        ## KOLABORAKSI — rumah semua eksperimen & modul Web3
    """)
st.markdown("""
        > 💡 Untuk tampilan dan pengalaman belajar yang optimal, disarankan menggunakan browser pada laptop atau PC untuk mengakses Learn3
    """)

# ===== Tab utama =====
tabs = st.tabs([
    "🤖 AI Playground", 
    "🎸 Learn to Earn",
    "🧪 Token Lab",
    "🗳 DAO Sandbox",
    "💱 DeFi Workshop",
    "⚒️ Smart Contract Studio",
    "⚡ Gas & Performance",
    "🔐 Audit Security",
    "🔗 Web3 Lab",
    "🎓 Certification"
])

# ===== Tab: Chatbot =====
with tabs[0]:
    st.subheader("🤖 Chatbot AI-powered Playground")
    st.markdown("""
        Tanya jawab interaktif tentang blockchain, smart contract, dan Web3. Pilih sesuai kebutuhan kamu.
    """)
    st.markdown("""
        Belajar dasar (Bot + Chat + Tutor) → Latihan (Simulators) → Quiz → Eksplorasi lanjut (Research) → Bebas tanya (AI Gateway).
    """)
    
    # --- Persist pilihan widget
    if "chat_widget" not in st.session_state:
        st.session_state.chat_widget = "BlockTutor"  # default
    
    widget_opt = st.radio(
        " ",
        ["BlockBot","BlockChat","BlockTutor","DAO Voter Simulator","LP Simulator","Quiz","Research","AI Gateway"],
        horizontal=True, label_visibility="collapsed",
        index=["BlockBot","BlockChat","BlockTutor","DAO Voter Simulator","LP Simulator","Quiz","Research","AI Gateway"].index(st.session_state.chat_widget),
        key="chat_widget"
    )
    
    URLS = {
        "BlockBot": "https://my.artibot.ai/learn3bot",
        "BlockChat": "https://bot.writesonic.com/share/bot/a148b878-259e-4591-858a-8869b9b23604",
        "BlockTutor": "https://www.chatbase.co/chatbot-iframe/RIURX1Atx537tDeYNcw8R",
        "DAO Voter Simulator": "https://tawk.to/chat/68ba6085721af15d8752fbc5/1j4c0i358",
        "LP Simulator": "https://denser.ai/u/embed/chatbot_o90yjz0cba1ymfmzi2nwr",
        "Quiz": "https://wayground.com/embed/quiz/68bb727d3fa528df7533c75e",
        "Research": "https://zenoembed.textcortex.com/?embed_id=emb_01k4cfh76fehtte5jgmy3atz69",
        "AI Gateway": "https://learn3ai.vercel.app/"
    }
    chosen_url = URLS[widget_opt]
    
    cache_bust = st.toggle("Force refresh chat (cache-bust)", value=False)
    final_url = f"{chosen_url}?t={int(time.time())}" if cache_bust else chosen_url
    
    st.write(f"💬 Chat aktif: **{widget_opt}**")
    st.caption("Jika area kosong, kemungkinan dibatasi oleh CSP/X-Frame-Options dari penyedia.")
    
    if widget_opt == "BlockChat":
        # Botsonic: sembunyikan header atas dengan crop ~56px (atur sesuai kebutuhan)
        embed_cropped(final_url, hide_px=56, height=720, title=None)
    else:
        # Widget lain tetap pakai iframe standar
        iframe(src=final_url, height=720)
    
    if st.button(f"🔗 Klik disini jika ingin menampilkan halaman chat {widget_opt} dengan lebih baik"):
        st.markdown(f"""<meta http-equiv="refresh" content="0; url={chosen_url}">""", unsafe_allow_html=True)

# === Tab 1: Learn to Earn (iframe ke Ohara) ===
with tabs[1]:
    app = OHARA_APPS["Learn to Earn"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 2: Token Lab (iframe ke Ohara) ===
with tabs[2]:
    app = OHARA_APPS["Token Lab"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 3: DAO Sandbox (iframe ke Ohara) ===
with tabs[3]:
    app = OHARA_APPS["DAO Sandbox"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 4: DeFi Workshop (iframe ke Ohara) ===
with tabs[4]:
    app = OHARA_APPS["DeFi Workshop"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 5: Smart Contract Studio (iframe ke Ohara) ===
with tabs[5]:
    app = OHARA_APPS["Smart Contract Studio"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 6: Gas & Performance (iframe ke Ohara) ===
with tabs[6]:
    app = OHARA_APPS["Gas & Performance"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 7: Audit Security (iframe ke Ohara) ===
with tabs[7]:
    app = OHARA_APPS["Audit Security"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 8: Web3 Lab (iframe ke Ohara) ===
with tabs[8]:
    app = OHARA_APPS["Web3 Lab"]
    embed_lab(app["url"], app["title"], hide_px=100)

# === Tab 9: Certification (iframe ke Ohara) ===
with tabs[9]:
    app = OHARA_APPS["Certification"]
    embed_lab(app["url"], app["title"], hide_px=100)
