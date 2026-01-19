from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{private_confession_revealed}"

@app.route("/")
def home():
    return """
    <style>
        body {
            background-color: #ffe6f2;
            font-family: Arial, sans-serif;
        }
    </style>

    <h2>HeartLink 💕</h2>
    <p>This site lets you view different messages.</p>
    <p>Example: <code>/profile?type=public</code></p>
    """

@app.route("/profile")
def profile():
    profile_type = request.args.get("type", "public")

    # probably not a great idea to trust URL parameters
    if profile_type == "public":
        return """
        <style>
            body {
                background-color: #ffe6f2;
                font-family: Arial, sans-serif;
            }
        </style>

        <h3>Public Message</h3>
        <p>This message is visible to everyone.</p>
        """

    elif profile_type == "private":
        return f"""
        <style>
            body {{
                background-color: #ffe6f2;
                font-family: Arial, sans-serif;
            }}
        </style>

        <h3>Private Confession ❤️</h3>
        <p>This message was never meant to be shared.</p>
        <p><b>{FLAG}</b></p>
        """

    else:
        return """
        <style>
            body {
                background-color: #ffe6f2;
                font-family: Arial, sans-serif;
            }
        </style>

        <p>Message not found.</p>
        """

if __name__ == "__main__":
    app.run(debug=True)


