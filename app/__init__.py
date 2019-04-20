from flask import Flask 

# Create the application object 
# The name variable is set to the name of the module in which it is used 
app = Flask(__name__) 

# Import the routes module
# Imported at the bottom as it relies on the app object 
from app import routes 