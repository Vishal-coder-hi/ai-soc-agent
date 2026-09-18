import os
import re

KNOWLEDGE_DIR = "knowledge"


def tokenize(text):
    """
    Convert text into lowercase words for simple matching.
    """
    return set(re.findall(r"\b[a-zA-Z0-9_/.-]+\b", text.lower()))


def retrieve_knowledge(alert, top_k=2):
    """
    Retrieve the most relevant security knowledge
    for a given security alert.
    """

    alert_text = " ".join(
        str(value) for value in alert.values()
    )

    alert_words = tokenize(alert_text)

    documents = []

    for filename in os.listdir(KNOWLEDGE_DIR):

        if not filename.endswith(".md"):
            continue

        file_path = os.path.join(KNOWLEDGE_DIR, filename)

        with open(file_path, "r") as file:
            content = file.read()

        document_words = tokenize(content)

        score = len(alert_words.intersection(document_words))

        documents.append({
            "file": filename,
            "score": score,
            "content": content
        })

    documents.sort(
        key=lambda document: document["score"],
        reverse=True
    )

    relevant_documents = documents[:top_k]

    return relevant_documents