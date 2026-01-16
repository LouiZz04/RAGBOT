#!/usr/bin/env python
# coding: utf-8

# # Data Transformation
# receive a pdf, return a chroma data folder which is an embedding for the text, images and tables of the pdf.

# In[1]:


import unstructured
from unstructured.partition.pdf import partition_pdf
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

from dotenv import load_dotenv
import os

load_dotenv()  
import time


documents = []


# In[2]:


embed_model = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")


import warnings
warnings.filterwarnings(
    "ignore",
    message="The `max_size` parameter is deprecated*"
)

#####
def data_transform(file: str):
    raw_data = partition_pdf(
        filename=file,
        strategy="hi_res",
        infer_table_structure=True,
        extract_images_in_pdf=True,
        #chunking_strategy="by_title",
        extract_image_block_output_dir="./data/temp_images",
        languages=["eng", "fra"],
    )


    # In[3]:


    file = os.getcwd() + "/" + file


    # In[4]:

    # ## Divide text, images and tables

    # In[5]:


    text_elements = []
    table_elements = []
    image_elements = []

    text_metadata = []

    for element in raw_data:
        el_type = str(type(element))

        if "Table" in el_type:
            table_elements.append(element)
        elif "Image" in el_type:
            image_elements.append(element)
        elif "CompositeElement" in el_type or "Text" in el_type:
            text_elements.append(element)
            text_metadata.append({"page_number":element.metadata.page_number,
                                "source": file,
                                "file_name": element.metadata.filename,
                                "type": "text"})



    # In[6]:





    # In[7]:


    raw_text = "\n\n".join(str(el) for el in text_elements)

    # ## Text Chunking

    # In[8]:


    semantic_chunker = SemanticChunker(embeddings=embed_model, breakpoint_threshold_amount=82, breakpoint_threshold_type="percentile")


    # In[9]:


    text_chunks = semantic_chunker.create_documents([raw_text], metadatas=text_metadata)


    # In[10]:


    # In[11]:


    # In[12]:


    # In[13]:


    # In[14]:


    # In[15]:




    # In[16]:


    # ## Tables

    # In[17]:


    table_docs = []
    for table in table_elements:
        page_content = table.text
        metadata = {
            "page_number":table.metadata.page_number,
            "type":"table",
            "html_content":table.metadata.text_as_html
                    }

        document = Document(page_content=page_content, metadata=metadata)
        table_docs.append(document)


    # In[18]:


    # In[19]:



    # In[20]:



    # ## Images

    # In[21]:


    from langchain_groq import ChatGroq
    import base64
    from langchain_core.messages import HumanMessage

    llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",
                temperature=0.1,
                max_tokens=500) # for a small paragraph


    # In[22]:


    def describe_image_with_LLM(path: str)->str:
        """
        This function will return a description of the image as a string format using a multimodal LM

        Args
            path: str, path of file

        Return
            description: str
        """

        prompt = """
        You are an expert technical assistant, analyze this image from an engineering document.
        1. Identify the type (Diagram, Plot, Circuit, or Photo)
        2. Transcribe any visible text, lables, equations, or axis values
        3. Describe the structural relationships or trends shown
        output a concise, dense paragraph optimized for retrieval.    
        """

        with open(path, "rb") as f:
            image_bytes = f.read()

        b64_string = base64.b64encode(image_bytes).decode("utf-8")


        message = HumanMessage( content=[ {"type": "text", 
                                        "text": prompt},
                                            { "type": "image_url",
                                            "image_url": {"url": f"data:image/jpeg;base64,{b64_string}"} }, ] )

        return llm.invoke([message])


    # In[23]:


    # In[24]:


    image_docs = []
    for image in image_elements:
        desc = describe_image_with_LLM(image.metadata.image_path)

        page_content = str(desc)
        metadata = {
            "model":"meta-llama/llama-4-scout-17b-16e-instruct",
            "source": file,
            "type": "image",
            "page": image.metadata.page_number,
            "original_path":image.metadata.image_path
        }
        document = Document(metadata=metadata, page_content=page_content)
        image_docs.append(document)

        time.sleep(2)


    # In[25]:



    # In[26]:


    # # Implement RAG

    # add all documents into one list

    # In[27]:


    for i in text_chunks:
        documents.append(i)

    for i in image_docs:
        documents.append(i)

    for i in table_docs:
        documents.append(i)


    # In[28]:
    return documents


    # In[29]:




