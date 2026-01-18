from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{private_confession_revealed}"

@app.route("/")
def home():
    return """
    <h2>HeartLink 💕</h2>
    <p>This site lets you view different profiles.</p>
    <p>Example: <code>/profile?type=public</code></p>
    """

@app.route("/profile")
def profile():
    profile_type = request.args.get("type", "public")

    # probably not a great idea to trust URL parameters
    if profile_type == "public":
        return """
        <h3>Public Profile</h3>
        <p>This profile is visible to everyone.</p>
        """
    elif profile_type == "private":
        return f"""
        <h3>Private Profile ❤️</h3>
        <p>This profile was never meant to be shared.</p>
        <p><b>{FLAG}</b></p>
        """
    else:
        return "<p>Profile not found.</p>"

if __name__ == "__main__":
    app.run(debug=True)
