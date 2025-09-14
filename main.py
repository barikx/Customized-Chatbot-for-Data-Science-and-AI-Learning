import os
from chatbot.app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render injects PORT
    print(f"Running on : http://0.0.0.0:{port}/")
    app.run(host="0.0.0.0", port=port, debug=False)  # debug=False in production
