from flask import Flask
# from imdb_api_service.sql_management.query_manager import IMDBQueryManager
# from imdb_api_service.json_management.json_encoding import IMDBJsonEncoder
from imdb_api_service.imdb_factory.imdb_factory_manager import IMDBFactory
#creating api

#hi

#entry point into our product
imdb_api = Flask(__name__)

# data_manager = IMDBQueryManager()
# json_encoder = IMDBJsonEncoder()

@imdb_api.route('/')
def home_page():
    return "Welcome to the IMDB api"

@imdb_api.route('/all-movie-data')
def all_movie_data():
    return IMDBFactory().get_all_movie_data_json()

@imdb_api.route('/all-films-over-half-a-billion')
def films_over_half_a_billion():
    return IMDBFactory().get_all_films_over_half_a_billion_json()

@imdb_api.route('/top-5-uk-films')
def top_five_uk_films():
    return IMDBFactory().get_top_five_uk_json()



if __name__ == '__main__':
    imdb_api.run()

