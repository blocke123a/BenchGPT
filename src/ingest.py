"""
Document ingestion for the Basketball RAG project.

Loads PDFs and Markdown files from the documents directory
and converts them into Document objects.
"""
import json
from pathlib import Path
import fitz

from src.models import Document
from src.config import DOCUMENTS_DIR
from src.file_tracking import file_hash

class DocumentLoader:

    def __init__(self, documents_dir=DOCUMENTS_DIR):

        self.documents_dir = Path(documents_dir)

    def load(self):

        documents = []

        for filepath in self.documents_dir.rglob("*"):

            if filepath.is_dir():

                continue

            if ".ipynb_checkpoints" in str(filepath):

                continue

            suffix = filepath.suffix.lower()

            if suffix == ".pdf":

                document = self._load_pdf(filepath)

            elif suffix in [".md", ".markdown"]:

                document = self._load_markdown(filepath)

            else:

                continue

            documents.append(document)

        return documents

    def _load_pdf(self, filepath):

        pdf = fitz.open(filepath)

        text = ""

        for page in pdf:

            text += page.get_text()

        pdf.close()

        category = filepath.parent.name

        return Document(
            text=text,
            metadata={
                "title": filepath.stem.replace("_", " ").title(),
                "filename": filepath.name,
                "filepath": str(filepath),
                "category": category,
                "source_type": "pdf"
            }
        )

    def _load_markdown(self, filepath):
    
        with open(filepath, encoding="utf8") as f:
            text = f.read()
    
        category = filepath.parent.name
    
        metadata_file = filepath.with_suffix(".json")
    
        extra_metadata = {}
    
        if metadata_file.exists():
    
            with open(metadata_file, encoding="utf8") as f:
    
                extra_metadata = json.load(f)
    
        title = extra_metadata.get(
            "title",
            filepath.stem.replace("_", " ").title()
        )
    
        url = extra_metadata.get("url")
    
        domain = extra_metadata.get("domain")
    
        if domain:
    
            domain = domain.lower()
    
            if "wikipedia" in domain:
    
                domain = "Wikipedia"
    
            else:
    
                domain = (
                    domain
                    .replace("www.", "")
                    .replace(".com", "")
                    .replace(".org", "")
                    .replace(".net", "")
                    .replace("-", " ")
                    .title()
                )
    
        return Document(
    
            text=text,
    
            metadata={
    
                "title": title,
    
                "url": url,
    
                "domain": domain,
    
                "filename": filepath.name,
    
                "filepath": str(filepath),
    
                "category": category,
    
                "source_type": "markdown"
    
            }
    
        )

    def document_paths(self):

        paths = []

        for filepath in self.documents_dir.rglob("*"):

            if filepath.is_dir():
                continue

            if ".ipynb_checkpoints" in str(filepath):
                continue

            suffix = filepath.suffix.lower()

            if suffix in [".pdf", ".md", ".markdown"]:

                paths.append(filepath)

        return paths

    def load_file(self, filepath):

        suffix = filepath.suffix.lower()

        if suffix == ".pdf":

            return [self._load_pdf(filepath)]

        elif suffix in [".md", ".markdown"]:

            return [self._load_markdown(filepath)]

        return []

    def load_new_documents(self, known_hashes):

        documents = []
    
        new_hashes = {}
    
        for filepath in self.document_paths():
    
            h = file_hash(filepath)
    
            new_hashes[str(filepath)] = h
    
            if known_hashes.get(str(filepath)) == h:
                continue
    
            documents.extend(self.load_file(filepath))
    
        return documents, new_hashes

# Convenience Function

def load_documents():

    loader = DocumentLoader()

    return loader.load()