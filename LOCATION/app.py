from flask import Flask, render_template, request, redirect, url_for
import uuid
import os

app = Flask(__name__)

import os

@app.route('/')
def index():
    # Generate a unique link for each request
    unique_id = str(uuid.uuid4())
    link = url_for('locate', unique_id=unique_id, _external=True)
    # Get the last location saved in locations.txt
    file_path = os.path.join(os.path.dirname(__file__), "locations.txt")
    last_location = None
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip()
                parts = last_line.split(',')
                if len(parts) == 3:
                    last_location = {'lat': parts[1], 'lon': parts[2]}
    return render_template('index.html', link=link, unique_id=unique_id, last_location=last_location)

@app.route('/locate/<unique_id>')
def locate(unique_id):
    return render_template('locate.html', unique_id=unique_id)

@app.route('/submit_location', methods=['POST'])
def submit_location():
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    unique_id = data.get('unique_id')
    if lat is not None and lon is not None:
        # Save location to a text file
        location_line = f"{unique_id},{lat},{lon}\n"
        file_path = os.path.join(os.path.dirname(__file__), "locations.txt")
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(location_line)
        print(f"Location received for {unique_id}: {lat}, {lon}")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
