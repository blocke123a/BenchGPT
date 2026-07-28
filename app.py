import streamlit as st

from src.rag import ask

def display_sources(chunks):

    seen = set()

    for source in chunks:

        metadata = source["metadata"]

        title = metadata.get(
            "title",
            metadata.get("filename", "Unknown Source")
        )

        url = metadata.get("url")

        filename = metadata.get("filename")

        key = url if url else filename

        if key in seen:
            continue

        seen.add(key)

        st.markdown(
            f"**📄 {title}**"
        )

        if url:

            st.link_button(
                "Open Source",
                url
            )

        else:

            st.caption(
                "Source document available in knowledge base"
            )

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="BenchGPT",
    page_icon="🏀",
    layout="wide"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🏀 BenchGPT")

    st.markdown(
        """
BenchGPT is a Retrieval-Augmented Generation (RAG) assistant
trained on a curated basketball knowledge base.

It can answer questions about:

- 📖 Rules
- 📊 Analytics
- 🧠 Strategy
- 📝 Scouting
- 🏆 NBA History
"""
    )

    st.divider()

    st.subheader("Knowledge Base")

    st.write("📂 Categories: **5**")
    st.write("📄 Documents: **Curated Collection**")
    st.write("🧠 Embeddings: **BAAI/bge-small-en-v1.5**")
    st.write("🤖 LLM: **Llama 3.3 via Groq**")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.rerun()


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🏀 BenchGPT")

st.markdown(
"""
Your basketball knowledge assistant.

Ask questions about:

- NBA & FIBA Rules
- Basketball Analytics
- Coaching Strategy
- Scouting Reports
- NBA History

Powered by Retrieval-Augmented Generation (RAG).
"""
)


# --------------------------------------------------
# Suggested Questions
# --------------------------------------------------

if len(st.session_state.messages) == 0:

    st.markdown("### 💡 Try asking...")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
- What is drop coverage?

- Explain true shooting percentage.

- Why were the 2014 Spurs so successful?

- How does ICE defense work?
""")

    with col2:

        st.markdown("""
- Compare Michael Jordan and LeBron James.

- Explain Box Plus Minus.

- What is a continuation foul?

- What is the scouting report on Cooper Flagg?
""")


st.divider()


# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            if "sources" in message:

                st.markdown("#### 📚 Sources")

                display_sources(message["sources"])


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask BenchGPT a basketball question..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)


    with st.chat_message("assistant"):

        with st.spinner("Searching basketball knowledge base..."):

            answer, chunks = ask(question)

        st.markdown(answer)
        
        st.markdown("#### 📚 Sources")

        display_sources(chunks)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": chunks
        }
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
"""
Built by **Blake Wood**

Python • Streamlit • ChromaDB • Groq • Sentence Transformers
"""
)