class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql:///blogly_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TESTING = True
    SECRET_KEY = "utahjazz12"
