from analyzer.rag_engine import retrieve_knowledge


test_alert = {
    "threat": "Possible Brute Force Attack",
    "severity": "HIGH",
    "description": "Multiple failed login attempts detected.",
    "ip": "185.220.101.5"
}


results = retrieve_knowledge(test_alert)


print("\n===== SECURITY RAG TEST =====\n")

for result in results:
    print(f"Knowledge File: {result['file']}")
    print(f"Relevance Score: {result['score']}")
    print("-" * 50)
    print(result["content"][:500])
    print("=" * 60)