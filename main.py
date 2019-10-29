### Required Modules ###
from server import app
#TODO set the Content-Type on tthe server side. current workaround is with a chrome extension to set response headers for the style sheet. otherwise chrome will always interpret the css as html
# TODO store game piece relations in a database

### Main ###

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=True)
