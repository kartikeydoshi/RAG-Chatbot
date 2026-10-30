Demo Link: https://psvtqwf7a9q9bupzaqugjj.streamlit.app/

# RAG LangChain

Streamlit document Q&A using LangChain, Deep Agents, and OpenAI. Supports PDF, Markdown, and text files.

## Setup

Requires Python 3.12+, [uv](https://docs.astral.sh/uv/), and an OpenAI API key.

```bash
uv sync
echo "OPENAI_API_KEY=your_key" > .env
uv run streamlit run main.py
```

Upload documents, process them, and ask questions in the browser.

## Example

Run the fixed PDF corpus in `pdfs/`:

```bash
uv run python agent.py
```
