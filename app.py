from flask import Flask
from flask_restful import Api, Resource
import scrap

app = Flask(__name__)
api = Api(app)


class cpAPI(Resource):
    @staticmethod
    def get():
        return scrap.fetchContests()


api.add_resource(cpAPI, "/")

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
