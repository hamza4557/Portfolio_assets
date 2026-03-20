# Location Finder Flask App

This app generates a unique link. When someone clicks the link, it tries to get their location. If location access is denied or unavailable, it shows a fake loading screen and then a generic error message. If location is obtained, it is sent to the backend and printed in the VS Code terminal.

## How to Run

1. Make sure you have Python 3.7+ installed.
2. Install Flask:
   pip install flask
3. Run the app:
   python app.py
4. Open http://127.0.0.1:5000/ in your browser.

## How it Works
- The main page gives you a unique link to send to someone.
- When they open the link, their browser will request location access.
- If allowed, their coordinates are sent to the backend and printed in the terminal.
- If denied or unavailable, a fake loading screen is shown, then a generic error message.

## Note
- No email integration yet. Location is only shown in the terminal for now.
