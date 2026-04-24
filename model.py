#!/usr/bin/env python3
import os

from langchain_community.document_loaders import UnstructuredMarkdownLoader, TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))

def call_rag_system(question: str) -> str:
    
    if os.path.exists("db"):
        db = Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"))
    
    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3})
    
    relevant_docs = retriever.invoke(question)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    messages = [
        ("system", "You are an AI assistant that can answer questions about Ignasi Aliguer-Piferrer. You are given a question and a list of documents and need to answer the question. Answer the question only based on these documents. These documents can help you answer the question: {context}. Plase assume that if the question refers to pronouns he or him or you, you should answer as if the question is referring to Ignasi Aliguer-Piferrer. If you are not sure about the answer, you can say 'I don't know' or 'I don't know the answer to that question.' If the question is not about Ignasi Aliguer-Piferrer, you can say 'I am only able to answer questions about Ignasi Aliguer-Piferrer.'"),
        ("human", "{query}"),
]
    prompt = ChatPromptTemplate.from_messages(messages=messages)
    model = ChatOpenAI(model="gpt-5.2-chat-latest")
    chain = prompt | model | StrOutputParser()
    answer = chain.invoke({"context": context, "query": question})
    return answer



if __name__ == "__main__":
    file = "assets/resume_CV_IAliguer_2026.md"
    #loader = UnstructuredMarkdownLoader(file, mode="single")
    loader = TextLoader(file, encoding="utf-8")
    docs = loader.load()
    print(f"Loaded {len(docs)} document(s) from {file}")
    print (docs[0].page_content)

    splitter = RecursiveCharacterTextSplitter(chunk_size=250,
                                              chunk_overlap=40,
                                              separators=["\n\n", "\n"," ", ".", ","])



    chunks = splitter.split_documents(docs)

    for chunk in chunks[:5]:
        print(chunk)
        print("---")

    # %% Create instance of embedding model
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

    
    #%%
    persist_directory = "db"
    if os.path.exists(persist_directory):
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings_model)
    else: 
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings_model)
        db.add_documents(chunks)
    # %%
    
    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3})
    


    query = "how many years of experience does Ignasi have in technology commercialization?"
    relevant_docs = retriever.invoke(query)

    #%% combined relevant docs to context
    context = "\n".join([doc.page_content for doc in relevant_docs])

    #%% create prompt
    messages = [
        ("system", "You are an AI assistant that can answer questions about Ignasi Aliguer-Piferrer. You are given a question and a list of documents and need to answer the question. Answer the question only based on these documents. These documents can help you answer the question: {context}. Plase assume that if the question refers to he or him, you should answer as if the question is referring to Ignasi Aliguer-Piferrer. If you are not sure about the answer, you can say 'I don't know' or 'I don't know the answer to that question.' If the question is not about Ignasi Aliguer-Piferrer, you can say 'I am only able to answer questions about Ignasi Aliguer-Piferrer.'"),
        ("human", "{query}"),
]
    prompt = ChatPromptTemplate.from_messages(messages=messages)

    model = ChatOpenAI(model="gpt-5.2-chat-latest")

    chain = prompt | model | StrOutputParser()

    answer = chain.invoke({"context": context, "query": query})

    print(f"Question: {query}")
    print(f"Answer: {answer}")

    # %% extract the texts from "page_content" attribute of each chunk
    #texts = [chunk.page_content for chunk in chunks]
    # %% create embeddings
    #embeddings = embeddings_model.embed_documents(texts=texts)
    #print(f"Created {len(embeddings)} embeddings for {len(texts)} chunks")
    #print(f"Embedding dimension: {len(embeddings[0])}")
    #print("End ...")