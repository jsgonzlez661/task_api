

class BaseConfig:
	SECRET_KEY = "b'\xf4WGJ<\xb1\x17\xec\xd0\x81'"
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://sql10353791:Uvfgc76WFM@sql10.freesqldatabase.com:3306/sql10353791'
	SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopementConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False