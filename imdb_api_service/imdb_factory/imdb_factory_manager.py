from imdb_api_service.sql_management.query_manager import IMDBQueryManager
from imdb_api_service.json_management.json_encoding import IMDBJsonEncoder

class IMDBFactory():

    def __init__(self):
        self.json_encoder = IMDBJsonEncoder()
        self.imdb_query_manager = IMDBQueryManager()

    def get_all_movie_data_json(self):
        return self.json_encoder.create_imdb_dict_arr(self.imdb_query_manager.get_query_data("SELECT * FROM moviedata;"))

    def get_all_films_over_half_a_billion_json(self):
        return self.json_encoder.create_imdb_dict_arr(self.imdb_query_manager.get_query_data("SELECT * FROM moviedata WHERE gross > 500000000;"))

    def get_top_five_uk_json(self):
        return self.json_encoder.create_imdb_dict_arr(self.imdb_query_manager.get_query_data("SELECT * FROM moviedata WHERE country = 'UK' ORDER BY gross DESC LIMIT 5;"))

