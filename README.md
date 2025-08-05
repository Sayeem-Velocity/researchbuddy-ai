# ResearchBuddy AI

Meet ResearchBuddy AI! Your ultimate multi-PDF chatbot application powered by cutting-edge AI technologies like Google Generative AI and FAISS. Extract, query, and interact with multiple PDF files seamlessly. Transform your research experience today!

## Description

ResearchBuddy AI is a Streamlit-based web application designed to assist users in extracting and querying information from multiple PDF files. With advanced AI capabilities, it provides accurate and detailed answers to user queries, making research faster and more efficient.

## Demo App

[Launch ResearchBuddy AI](https://sayeem-velocity-researchbuddy-ai-app-vmst8m.streamlit.app/)

## Demo:
<video controls>
  <source src="img/ResearchBuddy%20AI.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## How It Works:

![ResearchBuddy AI Architecture](img/Architecture.jpg)

The application follows these steps to provide responses to your questions:

1. **PDF Loading**: Upload multiple PDF documents, and the app extracts their text content.
2. **Text Chunking**: The extracted text is divided into smaller chunks for efficient processing.
3. **Embedding Generation**: Text chunks are converted into vector representations using AI models.
4. **Similarity Matching**: Your query is compared with text chunks to find the most relevant ones.
5. **Response Generation**: The selected chunks are used to generate detailed answers.

---

## Key Features

- **Multi-PDF Support**: Upload and query multiple PDF files simultaneously.
- **AI-Powered Responses**: Uses Google Generative AI for intelligent and accurate answers.
- **Customizable Prompt Templates**: Tailor responses to your needs.
- **FAISS Integration**: Efficient vector-based search for document retrieval.
- **Dynamic UI**: Interactive and animated user interface for an enhanced experience.
- **Real-Time Feedback**: Instant responses to user queries.
- **Secure Data Handling**: Ensures privacy and security of uploaded documents.

---

## Technologies Used

- **Python**: Core programming language for the application.
- **Streamlit**: Framework for building the web interface.
- **Google Generative AI**: Embedding and conversational AI model.
- **FAISS**: Vector search library for efficient document retrieval.
- **PyPDF2**: Library for extracting text from PDF files.
- **LangChain**: Framework for building AI-powered applications.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sayeem-Velocity/researchbuddy-ai.git
```

Navigate to the project directory:

```bash
cd researchbuddy-ai
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up your Google API key:

1. Create a `.env` file in the root directory.
2. Add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

Run the application:

```bash
streamlit run app.py
```

---

## Usage

1. **Upload PDFs**: Drag and drop multiple PDF files into the application.
2. **Query Documents**: Enter your query in the search bar, and the AI will retrieve relevant information.
3. **Interactive Responses**: View detailed answers with animations and dynamic UI elements.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

#### **If you like this project, drop a star on the repo!**
#### Follow me on [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/s-m-shahriar-26s/) &nbsp; [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sayeem-Velocity/)

---