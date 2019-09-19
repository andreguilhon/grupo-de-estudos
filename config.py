class CarrosConfig:
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:12345@devtests.powers.com.br:5432/guilhon'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
