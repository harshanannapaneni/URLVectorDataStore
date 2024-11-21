import chromadb

client = chromadb.PersistentClient(".chromadb")
collection = client.get_collection('education_links')
results = collection.query(
    query_texts=["Java Generics"],
    # where={"category": "Computer Science", "ref_type": "youtube"},
    n_results=1
)
print(results)
