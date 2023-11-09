import time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def handle_request():
    text = str(request.args.get('input'))  # Request the ?input=a
    char_count = len(text)

    # Setup json to return output
    data = {
        'input': text,
        'timestamp': time.time(),
        'count': char_count
    }

    json_data = json.dumps(data)
    return json_data
