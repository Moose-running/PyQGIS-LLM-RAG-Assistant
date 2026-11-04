import importlib

libraries = {
    "requests": "Requests",
    "bs4": "BeautifulSoup",
    "chromadb": "ChromaDB",
    "sentence_transformers": "Sentence Transformers",
    "dotenv": "Dotenv",
    "openai": "OpenAI SDK",
}

for module, name in libraries.items():
    try:
        importlib.import_module(module)
        print(f"{name}: OK")

    except ImportError:
        print(f"{name}: Failed")