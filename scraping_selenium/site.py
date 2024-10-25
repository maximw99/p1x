from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/do_something/<action>', methods=['GET'])
def do_something(action):
    result = my_python_function()
    return jsonify({"message": f"Action completed: {result}"})

def my_python_function():
    # Your function logic here
    return "Python function executed!"

if __name__ == '__main__':
    app.run(debug=True)