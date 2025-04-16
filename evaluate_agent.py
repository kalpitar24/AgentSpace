import json
from rag_agent import qa

with open("golden_dataset/golden_set.json") as f:
    golden_data = json.load(f)

print("\nEvaluating agent with golden dataset...\n")

for i, item in enumerate(golden_data):
    q = item['question']
    expected = item['answer']
    actual = qa.run(q)
    print(f"\n[{i+1}] Q: {q}\nExpected: {expected}\nGenerated: {actual}")
