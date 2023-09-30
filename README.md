Certainly! Here's an enhanced README for your GitHub project with emojis and a more visually appealing format:

---

# 🤖 Blank - A Scalable Chatbot


## 💬 Description

Blank is a chatbot with both short-term and long-term memory, designed with a focus on scalability and data safety, while ensuring lightning-fast responses. 🚀

## ⚙️ Installation

To set up Blank, follow these steps:

1. Use `pip` to install all the required packages mentioned in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

2. Create a separate file named `constants.py` and define the following variables with your values in uppercase using underscores:

    ```python
    OPENAI_API_KEY = ""
    PINECONE_API_KEY = ""
    PINECONE_ENVIRONMENT = ""
    PINECONE_INDEX_NAME = ""
    UNSTRUCTURED_IO_API_KEY = ""
    ```

## 🚀 Usage

### Retrieval

To use the retrieval capabilities of Blank, follow these steps:

1. Run the `chatbot.py` file with Python.

    ```bash
    python chatbot.py
    ```

2. 🗨️ Enter your query when prompted.

### Embedding

To embed data into Pinecone vector storage, follow these steps:

1. Run the `embeddingUtils.py` file with Python.

    ```bash
    python embeddingUtils.py
    ```

2. Create a folder named 'data' and place all the files containing the data to be embedded inside this folder.


## ✉️ Contact Information

[Your Email Address (optional)](mailto:itsguneetsingh@gmail.com)
