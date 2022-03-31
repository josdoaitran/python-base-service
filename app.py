from flask import Flask
app = Flask(__name__)

@app.route('/check', methods=['GET'])
def hello():
    return "checked!!!!"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')

# Why you should run it at 0.0.0.0
# https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues
