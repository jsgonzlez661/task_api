from flask_marshmallow import Marshmallow

ma = Marshmallow()

class TaskAPISchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'create_date')

