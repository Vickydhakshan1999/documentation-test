from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import User, UserDetails

@registry.register_document
class UserDocument(Document):
    # Include related fields using nested fields
    details = fields.ObjectField(properties={
        'address': fields.TextField(),
        'date_of_birth': fields.DateField(),
    })


    class Index:
        name = 'users'  
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = User  # The model to be indexed
        fields = [
            'name',
            'email',      
            'phone_no',
            'id'
              
        ]


