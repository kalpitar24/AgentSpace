rag-agent-vertex-eval/

├── your_docs/

│   └── product_guide.pdf                # Your source PDFs

├── golden_dataset/

│   └── golden_set.json                 # Generated Q&A (use golden_dataset_gen)

├── rag_agent.py                        # Script to create and run the RAG agent

├── evaluate_agent.py                   # Evaluate agent against golden dataset

├── generate_golden_dataset.sh          # Helper script to run golden_dataset_gen

├── requirements.txt                    # Dependencies

├── rag_agent_colab.ipynb               # End-to-end Colab notebook

└── README.md                           # Instructions & usage



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
