import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom CSS for animations
st.markdown(
    """
    <style>
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .animated-header {
            animation: float 3s infinite, fadeIn 2s ease-in-out;
            color: #4CAF50;
            font-size: 2.5em;
            text-align: center;
        }
        .animated-sidebar {
            animation: float 3s infinite, fadeIn 2s ease-in-out;
            color: #2196F3;
            font-size: 1.5em;
        }
        .animated-footer {
            animation: float 3s infinite, fadeIn 2s ease-in-out;
            color: #FFFFFF;
            font-size: 1em;
            text-align: center;
        }
        .animated-name {
            animation: float 3s infinite, fadeIn 2s ease-in-out;
            color: #FF5722;
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain


def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    # Perform similarity search to find relevant documents
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True,
    )

    print(response)
    st.write("Reply: ", response["output_text"])


def main():
    st.set_page_config("ResearchBuddy AI")
    st.markdown('<h1 class="animated-header">ResearchBuddy AI</h1>', unsafe_allow_html=True)

    user_question = st.text_input("Ask a Question from the PDF Files uploaded.")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.markdown('<h2 class="animated-sidebar">PDF File\'s Section</h2>', unsafe_allow_html=True)
        pdf_docs = st.file_uploader("Upload your PDF Files & Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process", key="process_button"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

    st.markdown(
        """
        <div class="animated-footer" style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px;">
            © ResearchBuddy AI | Created by <span class="animated-name">S.M. Shahriar</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()