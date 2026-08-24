# Lee Kuan Yew Research Chatbot

A transparent RAG-style prototype for answering questions about Lee Kuan Yew using curated public source references.

## Framing
This is a research simulation, not an authentic representation of Lee Kuan Yew. It retrieves source-grounded notes and clearly labels answers as research synthesis.

## Architecture
Question -> keyword retrieval -> top relevant source notes -> grounded response.

A production version can replace keyword retrieval with embeddings/vector search and an LLM.

## Sources
The prototype references public/official archives including the National Archives of Singapore, Prime Minister's Office Singapore, and National Library Board. It does not redistribute full copyrighted transcripts.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example questions
- What did Lee Kuan Yew emphasize about Singapore's foreign policy?
- How did he discuss education and human capital?
- How did he approach difficult national problems?
- What principles did he discuss about multiracial Singapore?
