import json
import re
from pathlib import Path
import streamlit as st

DATA = json.loads(Path("knowledge_base.json").read_text(encoding="utf-8"))

def tokens(text):
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))

def retrieve(question, k=3):
    q = tokens(question)
    ranked = []
    for item in DATA:
        searchable = " ".join([item["title"], item["topic"], item["summary"], " ".join(item["keywords"])])
        ranked.append((len(q & tokens(searchable)), item))
    ranked.sort(key=lambda x: x[0], reverse=True)
    return [item for score, item in ranked[:k] if score > 0]

def answer(question, sources):
    if not sources:
        return "I do not have enough source material in this prototype to answer reliably. Please add a relevant primary source."
    evidence = " ".join(s["summary"] for s in sources[:2])
    return (
        "Based on the retrieved historical sources, a reasonable interpretation is that "
        "the issue should be approached pragmatically, with attention to constraints, "
        "national interests, institutions, and long-term outcomes. " + evidence +
        " This is a research synthesis, not a verbatim quotation from Lee Kuan Yew."
    )

st.set_page_config(page_title="Lee Kuan Yew Research Chatbot", page_icon="🇸🇬")
st.title("Lee Kuan Yew Research Chatbot")
st.caption("Source-grounded historical research prototype — not an authentic impersonation.")

question = st.text_input("Ask a question", placeholder="What did Lee Kuan Yew emphasize about foreign policy?")

if question:
    sources = retrieve(question)
    st.subheader("Answer")
    st.write(answer(question, sources))
    st.subheader("Retrieved sources")
    for source in sources:
        st.markdown(f"**{source['title']} ({source['date']})**")
        st.write(source["summary"])
        st.link_button("Open source", source["url"])
else:
    st.info("Ask a question to retrieve relevant historical source notes.")
