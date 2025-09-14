# app.py — RANTAI Nexus (Streamlit)
# Requirements: streamlit
# Optional: streamlit-authenticator or streamlit-oauth for auth, web3 libs for deeper wallet integration.

import streamlit as st
import json
from datetime import datetime
import os
import streamlit.components.v1 as components

# -------------------------
# App config / branding
# -------------------------
st.set_page_config(page_title="RANTAI Nexus", layout="wide", initial_sidebar_state="expanded")
BRAND = "RANTAI Nexus"
TAGLINE = "KOLABORAKSI — rumah semua eksperimen & modul Web3"

# -------------------------
# Helper: storage for simple badges/progress (file-based)
# -------------------------
DATA_FILE = "user_progress.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(d):
    with open(DATA_FILE, "w") as f:
        json.dump(d, f, indent=2)

data = load_data()

# -------------------------
# Sidebar - global navigation
# -------------------------
with st.sidebar:
    st.image("https://placehold.co/200x80?text=RANTAI+Nexus", width=200)  # ganti logo
    st.markdown(f"### {BRAND}")
    st.caption(TAGLINE)

    page = st.radio("Explore", [
        "Home",
        "Learn3 (Embed)",
        "SmartFaith (Embed)",
        "SmartTourismChain",
        "DID Explorer",
        "Token Lab",
        "DAO Playground",
        "Admin / Analytics"
    ])

    st.divider()
    st.markdown("**Quick links**")
    st.write("- Docs · Community · GitHub")
    st.markdown("[GitHub](https://github.com/your-org) • [Community](#)")

# -------------------------
# Top header (wide)
# -------------------------
col1, col2 = st.columns([3,1])
with col1:
    st.title(BRAND)
    st.write(TAGLINE)
with col2:
    st.markdown("**Status**")
    st.info("Sandbox · Testnet Sepolia (dev)")

# -------------------------
# Page contents
# -------------------------
def embed_iframe(src, height=700):
    # components.iframe is easiest; some apps may block embedding (X-Frame-Options)
    components.iframe(src, height=height, scrolling=True)

if page == "Home":
    st.header("Welcome to RANTAI Nexus")
    st.write("""
    RANTAI Nexus adalah rumah pusat untuk semua eksperimen RANTAI: 
    edukasi, sandbox, demo SmartWisataChain, DAO mini, dan token lab.
    Pilih modul dari sidebar.
    """)
    st.markdown("### Highlights")
    st.markdown("- 🔗 Single navbar experience untuk semua modul")
    st.markdown("- 🧩 Modular — tinggal embed iframe tiap app")
    st.markdown("- 🏷 Badge & progress (local file, can upgrade ke DB)")
    st.markdown("### Quick start")
    st.markdown("1. Pilih modul dari sidebar. 2. Coba modul (embed). 3. Klaim badge jika tersedia.")

    st.markdown("---")
    st.subheader("Recent activity")
    entries = data.get("activity", [])
    if entries:
        for e in reversed(entries[-6:]):
            st.write(f"- {e['ts']} — {e['note']}")
    else:
        st.write("Belum ada aktivitas — mulai coba modul!")

elif page == "Learn3 (Embed)":
    st.header("Learn3 (embedded)")
    st.write("Embedded instance Learn3 — hide its native navbar to keep UX consistent.")
    # Ganti URL ini ke URL yang mau di-embed (streamlit app / other)
    embed_iframe("https://learn3.streamlit.app", height=800)

elif page == "SmartFaith (Embed)":
    st.header("SmartFaith (embedded)")
    embed_iframe("https://smartfaith.example.app", height=800)

elif page == "SmartTourismChain":
    st.header("SmartTourismChain")
    st.markdown("Pilih sub-modul:")
    tab = st.selectbox("Sub-modul", ["Booking Demo", "STC Analytics (GasVision)", "STC Certification Lite"])
    if tab == "Booking Demo":
        st.subheader("Booking Demo (on-chain simulation)")
        embed_iframe("https://stc-booking.example.app", height=700)
    elif tab == "STC Analytics (GasVision)":
        st.subheader("STC Analytics")
        st.write("Upload CSV/NDJSON output dari GasVision atau lihat visualisasi.")
        uploaded = st.file_uploader("Upload GasVision CSV/NDJSON", type=["csv","ndjson","json"])
        if uploaded:
            st.success("File diterima. (Preview)")
            st.write("... parsing preview ...")
    else:
        st.subheader("STC Certification Lite")
        st.write("Flow: upload .sol -> static analysis -> test -> certificate (placeholder).")
        if st.button("Run demo certification (mock)"):
            note = {"ts": datetime.now().isoformat(), "note": "Ran certification demo"}
            data.setdefault("activity", []).append(note)
            save_data(data)
            st.success("Certification demo complete (mock). Badge available in Profile.")

elif page == "DID Explorer":
    st.header("DID Explorer")
    st.write("Simple DID lookup / registry explorer (embed or internal).")
    embed_iframe("https://did-explorer.example.app", height=700)

elif page == "Token Lab":
    st.header("Ohara Token Lab (RANTAI Token Lab)")
    st.write("Guided steps to create ERC-20 / ERC-721 on testnet. (This is a guided embed + docs.)")
    cols = st.columns(2)
    with cols[0]:
        st.markdown("**Quick guides**")
        st.markdown("- Token Basics")
        st.markdown("- Deploy to Sepolia (demo)")
        st.markdown("- Minting flow")
    with cols[1]:
        embed_iframe("https://tokenlab.example.app", height=600)

elif page == "DAO Playground":
    st.header("DAO Playground")
    st.write("Create proposals, vote (simulation). Use tokens/badges as voting power.")
    if st.button("Create sample proposal"):
        note = {"ts": datetime.now().isoformat(), "note": "Created sample DAO proposal"}
        data.setdefault("activity", []).append(note)
        save_data(data)
        st.success("Proposal created (mock).")

elif page == "Admin / Analytics":
    st.header("Admin / Analytics")
    st.write("Light admin: activity log, user progress, quick deploy buttons.")
    st.write("Activity log:")
    st.write(data.get("activity", []))
    st.markdown("---")
    st.write("Badges / progress (local):")
    st.json(data.get("badges", {}))
    if st.button("Clear activity (dev)"):
        data["activity"] = []
        save_data(data)
        st.info("Cleared.")

# -------------------------
# Footer: quick actions
# -------------------------
st.markdown("---")
c1, c2, c3 = st.columns([1,1,6])
with c1:
    if st.button("Claim Badge (demo)"):
        badges = data.setdefault("badges", {})
        badges["starter"] = {"ts": datetime.now().isoformat(), "name": "Starter Explorer"}
        save_data(data)
        st.success("Badge 'Starter Explorer' diberikan (local).")
with c2:
    if st.button("Report Issue"):
        st.info("Open GitHub issue: https://github.com/your-org/rantai-nexus/issues")
with c3:
    st.write("© RANTAI Nexus • KOLABORAKSI")

