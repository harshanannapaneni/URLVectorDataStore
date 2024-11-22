import datetime
import uuid
from EduLinksManager import EduLinksManager

if __name__ == '__main__':
    choice = input("What operation you want to perform?\n\
                       1) Create a collection\n\
                       2) Add an entry to the existing collection\n\
                       3) Get all the documents inside an existing collection\n\
                       4) Similarity search on an existing collection\n\
                       5) Any other button to quit\n")
    
    def collect_details(new):
        collection_name = input(f"Enter the new collection name: ") if new else input(f"Enter the existing collection name: ")
        db_path = input("For default path: \".chromadb\" press enter....Else input here: ")
        ".chromadb" if db_path == "" else db_path
        return db_path,collection_name 
        
    
    if choice == "1":
        db_path, collection_name = collect_details(True)
        print(db_path,collection_name)
        edu = EduLinksManager(db_path, collection_name)
        
    elif choice == "2":
        db_path, collection_name = collect_details(False)

        edu = EduLinksManager(db_path,collection_name)

        id = uuid.uuid4()
        ref_type = input("Ref_type: youtube/article/book")
        url = input("URL")
        title = edu.fetch_youtube_title(url) if ref_type == 'youtube' else input("Title:")
        created = datetime.datetime.now().isoformat()
        author = input('Author')
        access_level = input("free/paid")
        
        edu.add_entry(
            id,ref_type,url,title,created,author,access_level)
    elif choice == "3":
        db_path, collection_name = collect_details(False)

        edu = EduLinksManager(db_path,collection_name)
        print(edu.get_collection())

    elif choice == "4":
        db_path, collection_name = collect_details(False)

        edu = EduLinksManager(db_path,collection_name)
        results = edu.similarity_search(query_params=input("\nEnter text to search for similar documents: "),
                              top_k=int(input("How many top results do you want? ")))
    
        for i,(doc,metadata,distance) in enumerate(zip(results["documents"],results["metadatas"],results['distances'])):
            print(f"\nResult {i + 1}:")
            print(f"Document: {doc}")
            print(f"Metadata: {metadata}")
            print(f"Similarity Score (Distance): {distance}")
    
    else:
        print("Exiting the function with status code 0.")
        quit(0)

    manager = EduLinksManager(db_path='.chromadb',collections_name='education_links')