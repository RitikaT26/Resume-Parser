import PyPDF2
import docx


def extract_text_from_pdf(file):

    pdf_reader = PyPDF2.PdfReader(file)

    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


def extract_text_from_docx(file):

    document = docx.Document(file)

    text = ""

    for para in document.paragraphs:

        text += para.text + "\n"

    return text