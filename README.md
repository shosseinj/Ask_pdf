# PDF Question-Answering Prototype

This is a small experimental prototype for asking a language model questions about the text extracted from a PDF document.

## Workflow

```text
PDF
  -> PyPDF2 text extraction
  -> document text inserted into a prompt
  -> question submitted to a language-model client
  -> generated answer
```

The current implementation reads the available page text with `PyPDF2` and sends the extracted text together with a question to the configured chat-completion client.

## Run

Edit the PDF path and question in `main.py`, install the required dependencies, and run:

```bash
python main.py
```

## Limitations

This is an early prototype, not a full retrieval-augmented generation (RAG) system. It currently has no vector database, semantic retrieval, citation grounding, document chunk ranking, or long-document context management. These would be natural extensions for larger document collections.


## Goal

The script demonstrates direct question answering over the text of one PDF and makes the limitations of a prompt-only approach visible before retrieval, chunking, and citation features are added.

## Installation

The repository has no dependency file. Create a small environment and install the two imported packages:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install PyPDF2 g4f
```

## Working with the Repository

Set the PDF path and question in `main.py`, then run `python main.py`. Use only documents you are permitted to send to the configured model provider. Scanned PDFs require OCR before this script can extract useful text, and long documents may exceed the provider's context limit.
