from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

# The preferred method is to use nginx or another web server 
# to serve static files; they'll be able to do it more efficiently
# than Flask. However, you can use send_from_directory to 
# send files from a directory, which can be pretty convenient 
# in some situations.
@app.route('/holy-static/')
def serve_static():
    return app.send_static_file('index.html')

@app.route('/api/cat')
def get_cat():
    return jsonify({"cat": {"name": "Millicent", "age": "8"}})

@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})   

if __name__ == "__main__":
    app.run(host='0.0.0.0')