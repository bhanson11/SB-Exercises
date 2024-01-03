from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """Stuff to do before every test in test.py for boggle"""

        self.client = app.test_client()
        app.config['TESTING'] = True
    
    # test the home page, check if homepage loads correctly, initializes session with game board and has right HTML and setup on page
    