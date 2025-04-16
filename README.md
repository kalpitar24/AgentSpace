rag-agent-vertex-eval/

├── your_docs/

│   └── product_guide.pdf               _ # Your source PDFs_

├── golden_dataset/

│   └── golden_set.json                _ # Generated Q&A (use golden_dataset_gen)_

├── rag_agent.py                       _ # Script to create and run the RAG agent_

├── evaluate_agent.py                 _  # Evaluate agent against golden dataset_

├── generate_golden_dataset.sh        _  # Helper script to run golden_dataset_gen_

├── requirements.txt                 _   # Dependencies_

├── rag_agent_colab.ipynb             _  # End-to-end Colab notebook_

└── README.md                         _  # Instructions & usage_



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
