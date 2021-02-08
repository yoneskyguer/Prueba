from flask_restful import Resource, reqparse
from Models.user import UserModel
from seed import user


class User_register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user',
                        type=str,
                        required=True,
                        help="This space cannot be empty."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This space cannot be empty."
                        )

    def post(self):
        data = User_register.parser.parse_args()

        if UserModel.find_by_user(data['user']):
            return {"message": "This user already exists."}, 400

        user = UserModel(data['user'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201