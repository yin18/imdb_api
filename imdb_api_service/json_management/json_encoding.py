from imdb_api_service.sql_management.query_manager import IMDBQueryManager
from flask import jsonify

class IMDBJsonEncoder():

    def __init__(self):
        self.field_names = ['movie_id', 'movie_title', 'duration', 'color', 'director_name', 'actor_1_name',
                                'actor_2_name', 'actor_3_name', 'gross', 'genres', 'plot_keywords', 'language',
                                'country', 'content_rating', 'budget', 'title_year', 'imdb_score']

#     def create_imdb_dict_arr(self):
#         list_of_results = []
#         example_tuple_list = []
#
#         if len(example_tuple_list) >= 1:
#             for result in example_tuple_list:
#                 list_of_results.append(dict(zip(self.field_names, result)))
#             return jsonify(list_of_results)
#         else:
#             return 'No movie data available'
#
# if __name__ == '__main__':
#     print(IMDBJsonEncoder().create_imdb_dict_arr())

    def create_imdb_dict_arr(self, list_of_db_tuple_results):
        list_of_results = []
        if len(list_of_db_tuple_results) >= 1:
            for tuple in list_of_db_tuple_results:
                list_of_results.append(dict(zip(self.field_names, tuple)))
            return jsonify(list_of_results)
        else:
            return 'No movie data available'

