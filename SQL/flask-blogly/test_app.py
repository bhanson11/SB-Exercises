# terminal ==> python -m unittest test_app.py

from app import app
from unittest import TestCase
from models import db, User, Post
from config import TestConfig

class TestApp(TestCase): 

    @classmethod
    def setUpClass(cls):
       app.config.from_object(TestConfig)
       cls.client = app.test_client()
       with app.app_context():
           db.create_all()

    # @classmethod
    # def tearDownClass(cls):
    #    with app.app_context():
    #        db.drop_all()

    # # from chatGPT for setup and tear down? try it
    # def setUp(self):
    #     with app.app_context():
    #         db.create_all()
    #         self.user = User(first_name="Test", last_name="User")
    #         db.session.add(self.user)
    #         db.session.commit()
    #         self.post = Post(title="Test Post", content="Test Content", user_id=self.user.id)
    #         db.session.add(self.post)
    #         db.session.commit()

    # def tearDown(self):
    #     with app.app_context():
    #         db.session.remove()
    #         db.drop_all()
    # # end of chatGPT setup and tear down

    def test_root_redirect(self):
        """test that root URL redirects to /users"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/users')

    def test_create_user(self):
        """test creating a new user"""
        response = self.client.post('/users/new', data={
            'first_name': 'John',
            'last_name': 'Doe',
            'image_url': ''
            }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        user = User.query.filter_by(first_name='John').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.last_name, 'Doe')

    def test_edit_user(self):
        """test editing a user"""
        data = {
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.post(f'/users/{self.user.id}/edit', data=data, follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        updated_user = User.query.get(self.user.id)
        self.assertEqual(updated_user.first_name, 'Updated')

    def test_delete_user(self):
        """test deleting a user from website and database"""
        response = self.client.post(f'/users/{self.user.id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        user = User.query.get(self.user.id)
        self.assertIsNone(user)

    def test_create_post(self):
        """test creating a new post for a user"""
        user = User(first_name="Jane", last_name="Doe")
        db.session.add(user)
        db.session.commit()

        response = self.client.post(f'/users/{user.id}/posts/new', data={
            'title': 'Test Post',
            'content': 'Test content'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        post = Post.query.filter_by(title='Test Post').first()
        self.assertIsNotNone(post)
        self.assertEqual(post.content, 'Test content')
        self.assertEqual(post.user_id, user.id)

    def test_edit_post(self):
        """ test editing a post"""
        data = {
            'title': 'Updated Post',
            'content': 'This is an updated post.'
        }
        response = self.client.post(f'/posts/{self.post.id}/edit', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        updated_post = Post.query.get(self.post.id)
        self.assertEqual(updated_post.title, 'Updated Post')

        