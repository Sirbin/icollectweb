__author__ = 'Alessio'



import unittest
import os
from project import app, db
from project.config_ import path_testing
from project.model_ import user_

TEST_DB = "testing\database_tester.db"

class Test_API(unittest.TestCase):

    #esegui prio per ogni test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLE'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(path_testing,TEST_DB)
        self.app = app.test_client()
        db.create_all()

        self.assertEqual(app.debug,False)


    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()


    def add_user(self):
        db.session.add(user_("massimo",'binocchio19q778',"aleqssio.bino@gmail.com","alessio","bino","Admin"))
        db.session.commit()

    def test_add_user_collection_return_correct_data(self):
        #self.add_user()
        responce = self.app.get('api/v1/user',follow_redirects=True)
        self.assertEquals(responce.status_code,200)
        self.assertEquals(responce.mimetype, 'application/json')
        self.assertIn(b'administrator',responce.data)

    def test_edituser_resouce_endpoint_correct_data(self):
        responce = self.app.get('api/v1/user/administrator',follow_redirects=True)
        self.assertEquals(responce.status_code,200)
        self.assertEquals(responce.mimetype,'application/json')
        self.assertIn(b'administrator',responce.data)
        self.assertNotIn(b'errore',responce.data)

if __name__ == '__main__':
    unittest.main()




