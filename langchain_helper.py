from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# from langchain_community.llms import OpenAI, SQLDatabase
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate
from sentence_transformers import SentenceTransformer
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from typing import List
from few_shots import few_shots

import os
#connecting to the MySQL server, you can make use of [SELECT CURRENT_USER() FROM <TABLE_NAME>;] to find the db_user and db_host 
db_user = '<USER_NAME>'
db_password = '<PASSWORD>'
db_host = 'localhost'
db_name = '<DB_NAME>'

class CustomHuggingFaceEmbeddings(HuggingFaceEmbeddings):
    def _init_(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def _call_(self, texts: str | List[str], **kwargs):
        return self.embed_texts(texts, **kwargs)

    def embed_texts(self, texts: str | List[str], **kwargs):
        if isinstance(texts, str):
            texts = [texts]
        return self.model.encode(texts, convert_to_tensor=True)

    @property
    def embedding_size(self) -> int:
        return self.model.get_sentence_embedding_dimension()

def get_few_shot_db_chain():

    db = SQLDatabase.from_uri(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}',
                              sample_rows_in_table_info=3)
    #the google_api_key is the api key from your gemini web app
    llm = GoogleGenerativeAI(model = 'models/text-bison-001', 
                         google_api_key = '<GOOGLE_API_KEY>', 
                         temperature = 0)

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [' '.join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas = few_shots)
    example_selector = SemanticSimilarityExampleSelector(vectorstore = vectorstore, k=2)

    mysql_prompt = '''You are a MySQL expert. Given an input question, first create a syntactically correct 
    MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most 
    {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative 
    data in the database. Never query for all columns from a table. You must query only the columns that 
    are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns 
    that do not exist. Also, pay attention to which column is in which table. Pay attention to use CURDATE() function 
    to get the current date, if the question involves 'today'.
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    '''

    example_prompt = PromptTemplate(
        input_variables=['Question', 'SQLQuery', 'SQLResult','Answer'],
        template='\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}',
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt = example_prompt,
        prefix = mysql_prompt,
        suffix = PROMPT_SUFFIX,
        input_variables = ['input', 'table_info', 'top_k']
    )
    chain = SQLDatabaseChain.from_llm(llm, db, verbose = True, prompt = few_shot_prompt)
    return chain
