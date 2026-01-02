# PDFs can contain text, images and tables, for that we will try to extract all with unstructured, then use sementic chunking for the raw text

from unstructured.partition.pdf import partition_pdf
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

embed_model = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")


file = input("Enter file directory: ")

raw_data = partition_pdf(
    filename=file,
    strategy="hi_res",
    infer_table_structure=True,
    extract_images_in_pdf=True,
    chunking_strategy="by_title",
    extract_image_block_output_dir="./temp_images"
)

text_elements = []
table_elements = []
image_elements = []

for element in raw_data:
    el_type = str(type(element))

    if "Table" in el_type:
        table_elements.append(element)
    elif "Image" in el_type:
        image_elements.append(element)
    elif "CompositeElement" in el_type or "Text" in el_type:
        text_elements.append(element)



raw_text = "\n\n".join(str(el) for el in text_elements)
semantic_chunker = SemanticChunker(embeddings=embed_model)
text_chunks = semantic_chunker.create_documents([raw_text])

print(text_chunks)