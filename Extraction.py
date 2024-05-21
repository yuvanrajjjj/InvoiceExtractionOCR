from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import create_extraction_chain
from langchain_experimental.llms.ollama_functions import OllamaFunctions
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Define file names
files = [r'D:\InvoiceExtractionWithLLM\Invoice.pdf']
documents = []

# Load documents
for file in files:
    loader = PyPDFLoader(file)
    documents.extend(loader.load())

# Define schema for extraction
schema = {
    "properties": {
        "invoice no": {"type": "integer"},
        "Total": {"type": "integer"},
        "Address": {"type": "string"},
        "Account No": {"type": "integer"},
    }
}

# Initialize LLM and create extraction chain
llm = OllamaFunctions(model="llama2", temperature=0)
chain = create_extraction_chain(schema, llm)

# Run extraction chain on documents
input = documents
output = chain.run(input)

# Print output
print(output)

# Save output to a text file
output_file = r'D:\InvoiceExtractionWithLLM\extracted_output.txt'
with open(output_file, 'w') as f:
    f.write(str(output))
