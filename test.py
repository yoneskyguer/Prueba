import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models.user import UserModel


class TestUser(unittest.TestCase):

    engine = create_engine('sqlite:///data.db')
    Session = sessionmaker(bind=engine)
    session = Session()



    def test_add_user(self):
        actual_users_before = self.session.query(UserModel).count()
        user_to_add = UserModel('testing', '123456')
        self.session.add(user_to_add)
        self.session.commit()


        total_now = self.session.query(UserModel).count()

        self.assertEqual(total_now, actual_users_before + 1)

    def test_delete_user(self):
        result = self.session.query(UserModel).all()
        if (not len(result)):
            self.session.add(UserModel('testing', '123456'))
            self.session.commit()
            result = self.session.query(UserModel).all()
        self.session.delete(result[0])
        after_result = self.session.query(UserModel).all()
        self.assertEqual(len(after_result), len(result) - 1)


if __name__ == '__main__':
    unittest.main()