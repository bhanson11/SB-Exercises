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
    
    def test_homepage(self):
        """test the home page, check if homepage loads correctly, 
        initializes session with game board and has right HTML and setup on page, 
        resets board"""
        
        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('num_plays'))
            # b'word' is a bytes literal used to represent a sequency of bytes rather than sequence of characters
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_words(self):
        """Test if submitted word is valid by modifying the board in current session"""

        with self.client as client:
            with client.session_transaction() as session:
                session['board'] = [["C", "A", "T", "T", "T"],
                                    ["C", "A", "T", "T", "T"],
                                    ["C", "A", "T", "T", "T"],
                                    ["C", "A", "T", "T", "T"],
                                    ["C", "A", "T", "T", "T"]]
                response = self.client.get('/submit-word?word=cat')
                print(response.data)
                self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if word is in the dictionary"""

        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            # self.client.get('/')
            response = self.client.get('/submit-word?word=impossible')
            self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on the board"""

        with self.client:
            self.client.get('/')
            response = self.client.get('/submit-word?word=fsjdakfkldsfjdslkfjdlksf')
            self.assertEqual(response.json['result'], 'not-word')