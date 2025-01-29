
import PyPDF2
import g4f

def extract_text_from_pdf(pdf_path):
    full_text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text
    return full_text

if __name__ == "__main__":
    pdf_path = "path/to/filename.pdf"  
    chunk = extract_text_from_pdf(pdf_path)

    question = "What is the title of the document?"
    prompt = f"Context: {chunk}\n\nQuestion: {question}\nAnswer:"  

    response = g4f.ChatCompletion.create(  # giving a pdf file about 25000 words
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"Question: {question}")
    print(f"Answer: {response}")
