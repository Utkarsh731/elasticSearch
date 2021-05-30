import utils
import pandas as pd
from elasticsearch import helpers

def create_index():
    index_name=input("Enter name of index")
    es=utils.get_connection()
    try:
        es.indices.create(index=index_name)
        print("index created successfully")
    except Exception as e:
        print(e)

def get_all_indexes():
    es = utils.get_connection()
    try:
        res=es.indices.get_alias("*")
        for i in res:
            print(i)
        print(res)
    except Exception as e:
        print(e)

def check_index():
    index_name=input("Enter name of index")
    es=utils.get_connection()
    try:
        response=es.indices.exists(index=index_name)    #It returns true and false
        print(response)
    except Exception as e:
        print(e)

def delete_index():
    index_name=input("Enter name of index")
    es=utils.get_connection()
    try:
        response=es.indices.delete(index=index_name)    #It returnsjson response {"acknowledged":True}
        print(response)
    except Exception as e:
        print(e)

def insert_single_record():
    doc={"name":"Pratt","email":"pratt@gmail.com","age":"22"}
    es = utils.get_connection()
    try:
        response = es.index(index="student",doc_type="information",id=2,body=doc)  # It returnsjson response {'_index': 'student', '_type': 'information', '_id': '1', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
        print(response)
    except Exception as e:
        print(e)

def get_single_record():
    es = utils.get_connection()
    try:
        response = es.get(index="student", doc_type="information", id=1, filter_path=['_source'])  # It returnsjson response {'_index': 'student', '_type': 'information', '_id': '1', '_version': 3, '_seq_no': 2, '_primary_term': 1, 'found': True, '_source': {'name': 'Utkars', 'email': 'AAAutkarsh@gmail.com', 'age': '22'}}
        print(response)
    except Exception as e:
        print(e)

def get_from_query():
    es = utils.get_connection()
    try:
        body={"from":0,"size":10,"query":{"match":{"email":"pratt@gmail.com"}}}
        response = es.search(index="student",body=body, filter_path=['hits.hits._source'])  # It returnsjson response {'_index': 'student', '_type': 'information', '_id': '1', '_version': 3, '_seq_no': 2, '_primary_term': 1, 'found': True, '_source': {'name': 'Utkars', 'email': 'AAAutkarsh@gmail.com', 'age': '22'}}
        print(response["hits"]["hits"])
    except Exception as e:
        print(e)

def read_and_upload_from_csv():
    es=utils.get_connection()
    df=pd.read_csv("/home/ubuntu/Desktop/pycharm-community-2020.3.3/bin/archive/IPL Matches 2008-2020.csv")
    df.drop('method',axis='columns', inplace=True)
    print(df.columns)# for checking columns
    print(df.shape)# for printing number of columns
    print(len(df["id"].unique()))#for checking that all the ids are unique or not
    #before uploading lets do some data cleaning
    print(df.isna().sum())#this will return the total null values in all the columns
    df=df.dropna()#this will remove all the rows having null value
    print(df.isna().sum())
    print("len==============="+str(len(df)))
    #Now we will convert the data to appropiate format that elastic can understand
    df_elastic=df.to_dict("records")
    new_converted_data=[]
    for doc in df_elastic:
        dic={"_id":doc["id"],"_index":"ipl","_type":"_doc","_source":doc}
        new_converted_data.append(dic)
    print(len(new_converted_data))#elastic understand this format of data
    try:
        helpers.bulk(es,new_converted_data)
    except Exception as e:
        print(e)

read_and_upload_from_csv()

