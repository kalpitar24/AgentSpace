# Agenstpace: RAG Agent with Vertex AI + Evaluation

This repo contains:
- A document-grounded agent using Vertex AI and LangChain
- In-memory FAISS vector search
- Golden dataset evaluation using [`golden_dataset_gen`](https://github.com/hselbie/golden_dataset_gen)

## Setup

```bash
pip install -r requirements.txt
```

## Generate Golden Set

```bash
bash generate_golden_dataset.sh
```

## Run Agent

```bash
python rag_agent.py
```

## Evaluate

```bash
python evaluate_agent.py
```

Or open `rag_agent_colab.ipynb` in Colab for a full demo.
