__author__ = 'Alessio'


#!/usr/bin/python
# -*- coding: ascii -*-

import unittest
import os
from project import app, db
from project.config_ import path_testing
from project.model_ import user_

TEST_DB = "testing\database_tester.db"

class AllTest(unittest.TestCase):

    #esegui prio per ogni test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['WTF_CSRF_ENABLE'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(path_testing,TEST_DB)
        self.app = app.test_client()
        db.create_all()

    #def tearDown(self):
        #db.drop_all()
     #   pass

    # esegue dopo ogni test
    def test_uset_setup(self):
        new_user = user_("alessio","solamente","alexs@hotmail.com","alesssoi","binos","admin")
        db.session.add(new_user)
        db.session.commit
        test = db.session.query(user_).all()
        for t in test:
            t.user
        assert t.user == "alessio"

    def test_form_present_on_login_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code,200)
        self.assertIn('ho',response.data)

    def login(self,name,password):
        return self.app.post('/', data=dict(name=name,password=password),follow_redirects=True)

    def test_un_register_usert_cannot_login_unless_register(self):
        responce = self.login('foooooooo','barrrrrrrr')
        self.assertIn('Invalid User or Password',responce.data)

    def register(self,username,password,confirm,email,first_name,laste_name,type):
        return self.app.post('dashboard/users/new_user/', data=dict(username=username,password=password,
                            confirm=confirm,email=email,first_name=first_name,laste_name=laste_name,type=type),
                             follow_redirects=True)

    def test_user_can_login(self):
        self.register("massimo","colantoni","colantoni","masimo@gmail.it","max","cazz","admin")
        responce = self.login("massimo","colantoni")
        self.assertIn('you are login',responce.data)

    def test_invalid_user_form_data(self):
         self.register("massimo","colantoni","colantoni","masimo@gmail.it","max","cazz","admin")
         responce = self.login("alet","foor")
         self.assertIn('invalid username and paswword',responce.data)

    def test_form_is_present_on_register_page(self):
        responce = self.app.get('/dashboard/users/new_user')
        self.assertEqual(responce.status_code,200)
        self.assertIn('please register to access the register ',responce.data)

    def test_user_registration(self):
        self.app.get('dashboard/users/new_user/',follow_redirects=True)
        self.register("massimo","colantoni","colantoni","masimo@gmail.it","max","cazz","admin")
        self.app.get('/dashboard/users/new_user',follow_redirects=True)
        responce =  self.register("massimo","colantoni","colantoni","masimo@gmail.it","max","cazz","admin")
        self.assertIn("username and/or email exist",responce.data)

    def logout(self):
        return self.app.get('logout/',follow_redirects=True)

    def test_logged_in_user_logout_can_logout(self):
        self.register("massimo1","colantoni1","colantoni1","masimoso@gmail.it","maxx","cazzz","admin")
        self.login("massimo1","colantono1")
        responce = self.logout()
        self.assertIn(b'Goodbye',responce.data)

    def test_not_logged_in_users_cannot_logout(self):
        respoce = self.logout()
        self.assertNotIn(b"Goodbye",respoce.data)

    def test_user_role_enter_in_setting_page(self):
         self.register("massimo1","colantoni1","colantoni1","masimoso@gmail.it","maxx","cazzz","user")
         self.login("massimo1","colantoni1")
         responce = self.app.get('dashboard/setting/',follow_redirects=True)
         self.assertIn("not permission",responce.data)

    def test_on_404_error(self):
        responce = self.app.get('/this_route_non_exist')
        self.assertEqual(responce.status_code, 404)
        self.assertIn(b'sorry',responce.data)

    def test_on_505(self):
        bad_user= user_(user="jeremy",password="corallo12",email="jeremy@hto.it",first_name="traco",last_name="sorra",profile_type="users")
        db.session.add(bad_user)
        db.session.commit()
        respoce = self.login('jeremy1', 'corallo')
        self.assertEqual(respoce.status_code,500)

    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()

