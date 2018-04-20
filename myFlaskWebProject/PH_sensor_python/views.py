"""
Routes and views for the flask application.
"""

from forms import VoteForm
import config_cosmos
import pydocumentdb.document_client as document_client
from datetime import datetime
from flask import render_template
from myFlaskWebProject import app


def home():
    client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'masterKey': config_cosmos.COSMOSDB_KEY})
    # Read databases and take first since id should not be duplicated.
    db = next((data for data in client.ReadDatabases() if data['id'] == config_cosmos.COSMOSDB_DATABASE))

    # Read collections and take first since id should not be duplicated.
    coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config_cosmos.COSMOSDB_COLLECTION))

    # Read documents and take first since id should not be duplicated.
    doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == config_cosmos.COSMOSDB_DOCUMENT))

    # Create a model to pass to results.html
    class VoteObject:
        choices = dict()
        total_votes = 0

    vote_object = VoteObject()
    vote_object.choices = {
        "Web Site" : doc['Web Site'],
        "Cloud Service" : doc['Cloud Service'],
        "Virtual Machine" : doc['Virtual Machine']
    }
    vote_object.total_votes = sum(vote_object.choices.values())
    # Hack to avoid zero detection in empty database
    if vote_object.total_votes == 0:
        vote_object.total_votes = 1

    return render_template(
        'results.html',
        title='Home page',
        year=datetime.now().year,
        vote_object = vote_object
    )

def create(): 
    form = VoteForm()
    replaced_document ={}
    if form.validate_on_submit(): # is user submitted vote  
        client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'masterKey': config_cosmos.COSMOSDB_KEY})

        # Read databases and take first since id should not be duplicated.
        db = next((data for data in client.ReadDatabases() if data['id'] == config_cosmos.COSMOSDB_DATABASE))

        # Read collections and take first since id should not be duplicated.
        coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config_cosmos.COSMOSDB_COLLECTION))

        # Read documents and take first since id should not be duplicated.
        doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == config_cosmos.COSMOSDB_DOCUMENT))

        # Take the data from the deploy_preference and increment our database
        doc[form.deploy_preference.data] = doc[form.deploy_preference.data] + 1
        replaced_document = client.ReplaceDocument(doc['_self'], doc)

        # Create a model to pass to results.html
        class VoteObject:
            choices = dict()
            total_votes = 0

        vote_object = VoteObject()
        vote_object.choices = {
            "Web Site" : doc['Web Site'],
            "Cloud Service" : doc['Cloud Service'],
            "Virtual Machine" : doc['Virtual Machine']
        }
        vote_object.total_votes = sum(vote_object.choices.values())

        return render_template(
            'results.html', 
            year=datetime.now().year, 
            vote_object = vote_object
        )

caca = create()
