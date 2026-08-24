# Technical Approach & Implementation Notes

## Retrieval
A transparent keyword retriever ranks a curated knowledge base containing source title, date, topic, paraphrased research note, keywords, and source URL.

## RAG flow
1. User asks a question.
2. Question is tokenized.
3. Source notes are ranked by keyword overlap.
4. Top relevant notes are passed to the response layer.
5. The answer links back to retrieved sources and avoids presenting invented quotations as authentic.

## Model choice
The prototype does not require a paid API key, so an evaluator can run it immediately. A production version would add an LLM after retrieval with instructions to remain source-grounded and never invent quotations.

## Evaluation
`eval_questions.json` provides a small test set for source relevance, groundedness, quotation accuracy, and uncertainty behavior.

## Data provenance
Primary/public references include National Archives of Singapore and Prime Minister's Office Singapore. National Library Board documents the multi-volume Papers of Lee Kuan Yew collection.
