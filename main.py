import chromadb
import uuid
import datetime

client = chromadb.PersistentClient(".chromadb")
collection = client.get_or_create_collection('education_links')

#Data to insert/add:
id = uuid.uuid4()
title = input("Title")
url = input("URL")
description = input("Description")
category = input("Category")
created = datetime.datetime.now().isoformat()
author = input('Suthor')
ref_type = input("Ref_type: youtube/article/book")
access_level = input("free/paid")

collection.add(
    ids=[str(uuid.uuid4())],  # Unique ID
    documents=[
        f"{title}\n{description}"
    ],  # Full content to be used for similarity search
    metadatas=[{
        "url": url,
        "category": category,
        "author": author,
        "created": created,
        "ref_type": ref_type,
        "access_level": access_level
    }]
)

