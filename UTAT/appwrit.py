from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.input_file import InputFile
import random

client = Client()

(client
 .set_endpoint('http://34.139.148.58/v1')  # Your API Endpoint
 .set_project('637009ba1cc4e478f2ac')  # Your project ID
 .set_key('f3c9e9b0ed0b3fb2b6029687884b332f7df170546104aff0f9ef0cb10829de1235e2bde03a7b2f1f97e0efa78426fa444da66fa8e750caa9a81a5dc107b68ed785bb7ef3d2149e5f162621a75d1a83749657ddfad7336f2b4aaed96d25ad2b59694d898b0ed9773f7ea1a7237cccc5d4916f4ae96c2fd730b16cc8fd69758a4b')  # Your secret API key
 )

storage = Storage(client)

result = storage.create_file('637009d1ea462ff0d224', 'unique()', InputFile.from_path("appwrit.py"))

# promise = storage.create_file('637009d1ea462ff0d224', str(random.randint), '/Users/shiveshprakash/Desktop/UofT/UTAT/JSON.py')
