from mysql.connector import MySQLConnection, Error
from config import read_config
#whenever needed add database credentials

def read_file(filename):
    with open(filename, 'rb') as f:
        photo =f.read()
        return photo
    
def update_blob(author_id, filename):
    #read file data
    data=read_file(filename)
    
    #prepare update query and data
    query='UPDATE authors' \
                'SET photo = %s' \
                'WHERE id =%s'
                
    args=(data,author_id) 
    config=read_config()   
try:
    #establish a conn to mysql database
    with MySQLConnection(**config) as conn:
        #create a cursor to execute SQL queries
        with conn.cursor() as cursor:
            #execute the update query with the provided arguements
            cursor.execute(query.args)
            #commit the chnages to the database
            conn.commit()
            
            
except Error as e:
    print(e)
if __name__ == '__main__':

    try:
        author_id=3
        filename='D:/Program Files/Blob in python/MySQL-Logo.jpg'
        update_blob(author_id,filename)
    
    
    except Error as e:
        print(e)