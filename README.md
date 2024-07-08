# Text2SQL
As the name suggests this is a Text-to-SQL chatbot which users can now clone and operate on their own local systems, utilizing MySQL Server and Gogle Gemini API Key.




   <img width="614" align = "center" alt="text2sql logo" src="https://github.com/karantha-kur/Text2SQL/assets/80699988/01ab0d4a-e3c5-45d5-bbdd-4516b2b80f9b">


The project allows users to ask questions in natural language, which are then converted into SQL queries using Google GenerativeAI model and LangChain. 
This bot then further executes the queries on the MySQL database to generate accurate responses.

In my demo I have made use of an Uber Dataset with the given ER Diagram shown below.

![uber data analysis ERD](https://github.com/karantha-kur/Text2SQL/assets/80699988/f07ed9fc-78f9-4ed8-90be-9bf20190b90c)


When configured and deployed this is what it finally produces:

<img width="1437" alt="Screenshot 2024-07-08 at 10 08 39 PM" src="https://github.com/karantha-kur/Text2SQL/assets/80699988/3ff13506-632f-4d1d-8551-1dc0ead4a1f7">

Techstack used:

Google GenerativeAI LLM: For natural language processing and query generation.
LangChain's SQLDatabaseChain: To integrate the model with the MySQL database.
Hugging Face Embeddings: For enhanced semantic understanding.
Chromadb: As a vector store for efficient data retrieval.
Few-Shot Learning: Implemented to fine-tune the model for more precise results.
Streamlit: For building a user-friendly interface.
