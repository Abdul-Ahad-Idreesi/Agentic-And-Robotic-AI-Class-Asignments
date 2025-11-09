
import feedparser
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# The URL of the RSS feed
RSS_FEED_URL = "https://static.cricinfo.com/rss/livescores.xml"

@app.route("/")
def index():
    """
    Fetches and displays live cricket scores from an RSS feed.
    """
    # Parse the RSS feed
    feed = feedparser.parse(RSS_FEED_URL)
    
    # Extract match entries from the feed
    matches = feed.entries
    
    # Render the HTML template with the match data
    return render_template("index.html", matches=matches)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
