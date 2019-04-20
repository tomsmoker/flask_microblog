from app import app 

# Set the main page decorators 
@app.route('/')
@app.route('/index')
def index():
    return ("Hello, World!") 

