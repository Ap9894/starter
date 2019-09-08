
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup 
import requests


# In[10]:


import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


# In[11]:


def get_link(link_url,max_count):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    arr = []
    for link in soup.findAll('a'):
        
        if max_count == 0 :
            break
        if link.get('href') == None:
            continue
        max_count -= 1
#         print(max_count)
        href = link_url+link.get('href')
#         get_link(href)
        arr.append(href)
    return arr
        

url = 'https://dmoz-odp.org/'
a = get_link(url,50)


# In[12]:


val = []
for i in range(len(a)):
     val.append([i+1, a[i]])


# In[13]:


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='ABHI',
                                         user='root',
                                         password='atgworld')
    mySql_insert_query = """INSERT INTO links (SI_NO, LINKS) 
                           VALUES (%s, %s) """
    records_to_insert = val
    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, val)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into links table")
except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

