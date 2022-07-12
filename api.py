#!/usr/bin/env python3

from flask import Flask, Response
from flask_restful import Resource, Api, reqparse

class App():
    def __init__(self):
        self.__app = Flask("FileAPI")
        self.__api = Api(self.__app)
        self.__api.add_resource(File, "/file")
    
    def run(self):
        self.__app.run()
    
    def get_api(self):
        return self.__api


class File(Resource):
    """Class to represent the /file endpoint"""

    def __init__(self):

        self.__data_file = "./data-file"
        self.__chunk_size = 1024
        super(File, self).__init__()

    def get(self):
        """GET request method"""
        with open(self.__data_file) as file:
            contents = file.read()
            return {"contents": contents}

    def post(self):
        """POST request method"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "data", type=str, required=True, help="data cannot be blank."
        )
        args = parser.parse_args()
        data = str.encode(args["data"])

        self.__push_chunks(data)

        return {}

    def __push_chunks(self, data):
        """Pushes `data` in chunks"""
        with open(self.__data_file, "ab") as file:
            for chunk in [
                data[i : i + self.__chunk_size]
                for i in range(0, len(data) - 1, self.__chunk_size)
            ]:
                file.write(chunk)
            return True

if __name__ == "__main__":
    App().run()
