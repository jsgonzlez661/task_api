

class BaseConfig:
	SECRET_KEY = "b'\xf4WGJ<\xb1\x17\xec\xd0\x81'"
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://user:password@host/database'
	SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopementConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False
