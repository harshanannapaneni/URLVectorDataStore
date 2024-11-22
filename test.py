import json
import chromadb

client = chromadb.PersistentClient(".temp")
collection = client.get_collection('educationlinks')
results = collection.get()
print(json.dumps(results))
