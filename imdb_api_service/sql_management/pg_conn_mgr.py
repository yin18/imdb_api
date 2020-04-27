from psycopg2 import connect


class IMDBConnManager:

    def __init__(self, dbname='imdb', user='postgres', password='postgres',host='81.102.129.142',port=5432):
        # config = connect(dbname='imdb', user='postgres', password='postgres',host='81.102.129.142',port=5432)
        self.connection = connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # cursor = config.cursor()
        self.cursor = self.connection.cursor()

    def query_execution(self, sql_query_string):
        return self.cursor.execute(sql_query_string)

    def all_data_from_query(self):
        #cursor.fetchall()
        return self.cursor.fetchall()

# if __name__ == '__main__':
#     api = IMDBConnManager()
#     api.query_execution('SELECT * FROM moviedata')
#     print(api.all_data_from_query())




# all_movie_data = cursor.execute('SELECT * FROM moviedata')
# print(all_movie_data)
# all_rows = cursor.fetchall()
#
# for row in all_rows:
#     print(row)