from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self,name):
        with open("/app/user", 'r') as f:
            for line in f:
                if name in line:
                    return {'user': name}
            return {'user': None}

    def post(self,name):
        with open("/app/user", 'a') as f:
            f.write(f"{name} \n")
            return {'user': name}

    def delete(self,name):
        with open("/app/user", 'r+') as f:
            for line in f:
                if line != name:
                    f.write(line)

api.add_resource(Users,'/user/<string:name>')

app.run(debug=True, host='0.0.0.0', port=8080)
