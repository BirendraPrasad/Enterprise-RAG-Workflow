import streamlit as st
import requests
import time

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    /* Global */
    [data-testid="stAppViewContainer"] {
        background-color: #0f1117;
    }
    [data-testid="stSidebar"] {
        background-color: #1a1d27;
        border-right: 1px solid #2e3250;
    }
    [data-testid="stSidebar"] * {
        color: #e0e4f0 !important;
    }

    /* Sidebar title */
    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #7c8ff7 !important;
        letter-spacing: 0.03em;
        padding-bottom: 0.3rem;
        border-bottom: 2px solid #2e3250;
        margin-bottom: 1rem;
    }
    .sidebar-subtitle {
        font-size: 0.78rem;
        color: #6b7280 !important;
        margin-top: -0.6rem;
        margin-bottom: 1.2rem;
    }

    /* Doc card */
    .doc-card {
        background: #22263a;
        border: 1px solid #2e3250;
        border-radius: 8px;
        padding: 0.55rem 0.75rem;
        margin-bottom: 0.45rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.82rem;
        color: #c5cae9;
        word-break: break-all;
    }
    .doc-icon { font-size: 1rem; flex-shrink: 0; }

    /* Stat badge */
    .stat-badge {
        background: #1e2235;
        border: 1px solid #3a3f6e;
        border-radius: 20px;
        padding: 0.3rem 0.9rem;
        font-size: 0.8rem;
        color: #7c8ff7;
        display: inline-block;
        margin-top: 0.5rem;
    }

    /* Chat container */
    .chat-area {
        max-width: 820px;
        margin: 0 auto;
        padding-bottom: 2rem;
    }

    /* Chat header */
    .chat-header {
        text-align: center;
        padding: 1.8rem 0 1.2rem 0;
    }
    .chat-header h1 {
        font-size: 1.9rem;
        font-weight: 700;
        background: linear-gradient(135deg, #7c8ff7, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .chat-header p {
        color: #6b7280;
        font-size: 0.88rem;
    }

    /* Message bubbles */
    .msg-row-user {
        display: flex;
        justify-content: flex-end;
        margin: 0.7rem 0;
        gap: 0.6rem;
        align-items: flex-end;
    }
    .msg-row-assistant {
        display: flex;
        justify-content: flex-start;
        margin: 0.7rem 0;
        gap: 0.6rem;
        align-items: flex-end;
    }
    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        flex-shrink: 0;
    }
    .avatar-user { background: #3b4fd6; }
    .avatar-bot  { background: #2e3250; }

    .bubble-user {
        background: linear-gradient(135deg, #3b4fd6, #5b6ef5);
        color: #fff;
        border-radius: 18px 18px 4px 18px;
        padding: 0.7rem 1.1rem;
        max-width: 72%;
        font-size: 0.92rem;
        line-height: 1.55;
        box-shadow: 0 2px 12px rgba(59,79,214,0.25);
    }
    .bubble-assistant {
        background: #1e2235;
        color: #dde1f5;
        border: 1px solid #2e3250;
        border-radius: 18px 18px 18px 4px;
        padding: 0.7rem 1.1rem;
        max-width: 80%;
        font-size: 0.92rem;
        line-height: 1.55;
        box-shadow: 0 2px 12px rgba(0,0,0,0.2);
    }

    /* Source chip */
    .source-header {
        font-size: 0.75rem;
        color: #6b7280;
        margin-top: 0.3rem;
        margin-left: 2.6rem;
        margin-bottom: 0.15rem;
    }

    /* Score pill */
    .score-pill {
        display: inline-block;
        background: #2e3250;
        color: #7c8ff7;
        border-radius: 999px;
        padding: 0.15rem 0.55rem;
        font-size: 0.72rem;
        font-weight: 600;
        margin-right: 0.35rem;
        border: 1px solid #3a3f6e;
    }
    .score-bar-bg {
        background: #2e3250;
        border-radius: 4px;
        height: 4px;
        width: 100%;
        margin-top: 0.25rem;
    }
    .score-bar-fill {
        background: linear-gradient(90deg, #7c8ff7, #a78bfa);
        border-radius: 4px;
        height: 4px;
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        color: #3a3f6e;
        padding: 3.5rem 1rem;
        font-size: 0.9rem;
    }
    .empty-icon { font-size: 2.8rem; margin-bottom: 0.5rem; }

    /* Divider */
    .section-divider {
        border: none;
        border-top: 1px solid #2e3250;
        margin: 1rem 0;
    }

    /* Override Streamlit input */
    [data-testid="stTextInput"] input {
        background-color: #1a1d27 !important;
        border: 1px solid #2e3250 !important;
        color: #e0e4f0 !important;
        border-radius: 10px !important;
    }
    [data-testid="stTextInput"] input:focus {
        border-color: #5b6ef5 !important;
        box-shadow: 0 0 0 2px rgba(91,110,245,0.2) !important;
    }

    /* Expander */
    [data-testid="stExpander"] {
        background: #14162080;
        border: 1px solid #2e3250;
        border-radius: 8px;
        margin-left: 2.6rem;
    }
    [data-testid="stExpander"] summary {
        color: #6b7280 !important;
        font-size: 0.8rem;
    }

    /* Button */
    .stButton button {
        background: linear-gradient(135deg, #3b4fd6, #5b6ef5) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: opacity 0.2s !important;
    }
    .stButton button:hover { opacity: 0.88 !important; }

    /* Success / error */
    [data-testid="stAlert"] {
        border-radius: 8px !important;
    }

    /* Hide streamlit branding */
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── Session state init ──────────────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []
if "documents" not in st.session_state:
    st.session_state.documents = []
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = 0


# ── API helpers ─────────────────────────────────────────────────────────────

def upload_pdf(file) -> dict:
    try:
        r = requests.post(
            f"{BACKEND_URL}/upload",
            files={"file": (file.name, file.getvalue(), "application/pdf")},
            timeout=60,
        )
        r.raise_for_status()
        return {"ok": True, "data": r.json()}
    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "Cannot connect to backend. Is the FastAPI server running?"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def ask_question(query: str) -> dict:
    try:
        r = requests.post(
            f"{BACKEND_URL}/query",
            params={"query": query},
            timeout=60,
        )
        r.raise_for_status()
        return {"ok": True, "data": r.json()}
    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "Cannot connect to backend."}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def get_documents() -> dict:
    try:
        r = requests.get(f"{BACKEND_URL}/documents", timeout=15)
        r.raise_for_status()
        return {"ok": True, "data": r.json()}
    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "Cannot connect to backend."}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def delete_document(filename: str) -> dict:
    try:
        r = requests.delete(f"{BACKEND_URL}/documents/{filename}", timeout=15)
        r.raise_for_status()
        return {"ok": True}
    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "Cannot connect to backend."}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def refresh_documents():
    res = get_documents()
    if res["ok"]:
        st.session_state.documents = res["data"].get("documents", [])
    st.session_state.last_refresh = time.time()


# ── Auto-load documents once ─────────────────────────────────────────────────
if st.session_state.last_refresh == 0:
    refresh_documents()


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown('<div class="sidebar-title">🧠 RAG Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Retrieval-Augmented Generation</div>', unsafe_allow_html=True)

    # ── Upload section ──────────────────────────────────────────────────────
    st.markdown("#### 📤 Upload Document")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        label_visibility="collapsed",
    )

    if st.button("Upload PDF", use_container_width=True, disabled=uploaded_file is None):
        with st.spinner("Uploading and indexing…"):
            result = upload_pdf(uploaded_file)
        if result["ok"]:
            d = result["data"]
            st.success(f"✅ **{d.get('filename', uploaded_file.name)}** — {d.get('chunks_stored', '?')} chunks stored")
            refresh_documents()
        else:
            st.error(f"❌ {result['error']}")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # ── Documents list ──────────────────────────────────────────────────────
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 📚 Documents")
    with col2:
        if st.button("↻", help="Refresh list"):
            refresh_documents()

    docs = st.session_state.documents

    if not docs:
        st.markdown(
            '<div style="color:#4a506e;font-size:0.82rem;padding:0.5rem 0;">No documents uploaded yet.</div>',
            unsafe_allow_html=True,
        )
    else:
        for doc in docs:
            name = doc if isinstance(doc, str) else doc.get("filename", str(doc))
            col_d, col_x = st.columns([5, 1])
            with col_d:
                st.markdown(
                    f'<div class="doc-card"><span class="doc-icon">📄</span>{name}</div>',
                    unsafe_allow_html=True,
                )
            with col_x:
                st.markdown("<div style='padding-top:0.15rem'>", unsafe_allow_html=True)
                if st.button("🗑", key=f"del_{name}", help=f"Delete {name}"):
                    with st.spinner(f"Deleting {name}…"):
                        res = delete_document(name)
                    if res["ok"]:
                        st.success(f"Deleted **{name}**")
                        refresh_documents()
                        st.rerun()
                    else:
                        st.error(res["error"])
                st.markdown("</div>", unsafe_allow_html=True)

    total = len(docs)
    st.markdown(
        f'<div class="stat-badge">📊 {total} document{"s" if total != 1 else ""} indexed</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # ── Clear chat ──────────────────────────────────────────────────────────
    if st.button("🗑 Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# MAIN CHAT AREA
# ══════════════════════════════════════════════════════════════════════════════

st.markdown(
    """
    <div class="chat-header">
        <h1>RAG Document Assistant</h1>
        <p>Upload your PDFs, then ask anything about them.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

chat_container = st.container()

with chat_container:
    if not st.session_state.messages:
        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-icon">💬</div>
                <div>No messages yet.</div>
                <div style="margin-top:0.4rem;font-size:0.82rem;">
                    Upload a PDF from the sidebar and start asking questions.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        for msg in st.session_state.messages:
            role = msg["role"]

            if role == "user":
                st.markdown(
                    f"""
                    <div class="msg-row-user">
                        <div class="bubble-user">{msg["content"]}</div>
                        <div class="avatar avatar-user">👤</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:
                st.markdown(
                    f"""
                    <div class="msg-row-assistant">
                        <div class="avatar avatar-bot">🤖</div>
                        <div class="bubble-assistant">{msg["content"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                sources = msg.get("sources", [])
                if sources:
                    with st.expander(f"📎 {len(sources)} source chunk{'s' if len(sources) != 1 else ''} retrieved"):
                        for i, src in enumerate(sources, 1):
                            score = src.get("score", 0)
                            text  = src.get("text", "")
                            pct   = int(score * 100)
                            st.markdown(
                                f"""
                                <div style="margin-bottom:0.9rem;">
                                    <div style="display:flex;align-items:center;gap:0.4rem;margin-bottom:0.3rem;">
                                        <span style="font-size:0.78rem;color:#6b7280;font-weight:600;">Chunk {i}</span>
                                        <span class="score-pill">⚡ {score:.3f}</span>
                                        <div style="flex:1;background:#2e3250;border-radius:4px;height:4px;">
                                            <div style="width:{pct}%;background:linear-gradient(90deg,#7c8ff7,#a78bfa);border-radius:4px;height:4px;"></div>
                                        </div>
                                        <span style="font-size:0.72rem;color:#4a506e;">{pct}%</span>
                                    </div>
                                    <div style="font-size:0.82rem;color:#9ca3c8;background:#141620;border-radius:6px;padding:0.55rem 0.75rem;border:1px solid #1e2235;line-height:1.5;">
                                        {text}
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

# ── Input bar ───────────────────────────────────────────────────────────────

st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

input_col, btn_col = st.columns([9, 1])
with input_col:
    user_input = st.text_input(
        "Ask a question…",
        key="user_query",
        placeholder="e.g. What is the main topic of this document?",
        label_visibility="collapsed",
    )
with btn_col:
    send_clicked = st.button("Send", use_container_width=True)

if send_clicked and user_input.strip():
    query = user_input.strip()

    # Append user message
    st.session_state.messages.append({"role": "user", "content": query})

    # Query backend
    with st.spinner("Thinking…"):
        result = ask_question(query)

    if result["ok"]:
        data    = result["data"]
        answer  = data.get("answer", "No answer returned.")
        sources = data.get("sources", [])
        st.session_state.messages.append({
            "role":    "assistant",
            "content": answer,
            "sources": sources,
        })
    else:
        st.session_state.messages.append({
            "role":    "assistant",
            "content": f"⚠️ Error: {result['error']}",
            "sources": [],
        })

    st.rerun()