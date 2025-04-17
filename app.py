from flask import Flask, send_file, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

# This will serve anything inside the 'assets' directory
@app.route('/assets/<path:filename>')
def custom_static(filename):
    return send_from_directory("assets", filename)

if __name__ == "__main__":
    app.run(debug=True)
