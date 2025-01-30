from langchain_core.embeddings import Embeddings
from hdbcli import dbapi

class HanaEmbeddings(Embeddings):
    def __init__(
        self,
        connection: dbapi.Connection
    ):
        self.connection = connection

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text: str) -> list[float]:
        mycur = self.connection.cursor()
        # print(type(text))
        select_sql=f"""SELECT TO_NVARCHAR(VECTOR_EMBEDDING(?, 'DOCUMENT', 'SAP_NEB.20240715')) FROM DUMMY;"""
        # print(select_sql)
        mycur.execute(
            select_sql, text
        )
        rows = mycur.fetchone()
        return eval(rows[0])