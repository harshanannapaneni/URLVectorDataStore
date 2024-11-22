import chromadb

class EduLinksManager:

    def __init__(self,db_path,collections_name):
        self.client = chromadb.PersistentClient(db_path)
        self.collection = self.client.get_or_create_collection(collections_name)
    
    def add_entry(self, id, ref_type, url, title, created, author, access_level):
        self.collection.add(
            ids=[str(id),],  # Unique ID
            documents=[
                title,
            ],  # Full content to be used for similarity search
            metadatas=[{
                "url": url,
                "author": author,
                "created": created,
                "ref_type": ref_type,
                "access_level": access_level
            }]
        )

    def get_collection(self):
        return self.collection.get()

    @staticmethod
    def fetch_youtube_title(url):
        #Imports
        from bs4 import BeautifulSoup
        import requests

        #Getting the titles.
        request = requests.get(url)
        soup = BeautifulSoup(request.text,'html.parser')
        title = soup.find('meta',property='og:title')
        return title['content'] if title else 'No title found'
    
    def similarity_search(self, query_params, top_k):
        return self.collection.query(query_texts=[query_params],
                              n_results=top_k)