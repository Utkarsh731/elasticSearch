from elasticsearch import Elasticsearch

def get_connection():
    con=Elasticsearch(HOST="localhost",PORT=9200)
    print(con)
    return con

