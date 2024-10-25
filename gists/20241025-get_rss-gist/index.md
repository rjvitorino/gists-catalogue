# 20241025-get_rss-gist

**Gist file**: [https://gist.github.com/rjvitorino/f751b3e5ee689bc3bda721802dcf6dda](https://gist.github.com/rjvitorino/f751b3e5ee689bc3bda721802dcf6dda)

**Description**: Cassidoo's interview question of the week: a function that takes in an RSS feed URL, and returns the title of and link to the the original feed source

## get_rss.py

```Python
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
from urllib.error import URLError
from typing import Optional

# Attempt to import feedparser; set flag based on availability
try:
    import feedparser

    USE_FEEDPARSER = True
except ImportError:
    USE_FEEDPARSER = False
    print("Warning: feedparser is not installed. Falling back to standard libraries.")


def get_rss(url: str) -> Optional[str]:
    """
    Fetches attributes like title, link, and description from an RSS feed URL.

    Args:
        url (str): The URL of the RSS feed.

    Returns:
        Optional[str]: A string with the title, link, and description of the feed, or None if failed.

    Note:
        To use the feedparser functionality, you need to install the feedparser library.
        You can install it using pip:
        ```
        pip install feedparser
        ```
    """
    # Default values in case any attribute is missing from the feed
    default_values = {
        "title": "No title available",
        "link": "No link available",
        "description": "No description available",
    }

    if USE_FEEDPARSER:
        # If feedparser is available, use it for parsing RSS feeds
        feed = feedparser.parse(url)
        if feed.bozo:
            # The 'bozo' flag indicates any issues with the feed's structure
            print("Failed to parse RSS feed.")
            return None
        title = feed.feed.get("title", default_values["title"])
        link = feed.feed.get("link", default_values["link"])
        description = feed.feed.get("description", default_values["description"])

    else:
        # If feedparser is unavailable, fall back on using standard libraries
        try:
            # Create a request with a User-Agent header to bypass possible access restrictions
            request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(request) as response:
                root = ET.parse(response).getroot()

                # Explicitly check for the presence of 'channel' or 'feed' without triggering the deprecation warning
                channel = (
                    root.find("channel")
                    if root.find("channel") is not None
                    else root.find("feed")
                )

                # Check if channel is found and extract data
                if channel is not None:
                    title = (
                        channel.findtext("title")
                        or channel.findtext("{*}title")
                        or default_values["title"]
                    )
                    link = (
                        channel.findtext("link")
                        or channel.findtext("{*}link")
                        or default_values["link"]
                    )
                    description = (
                        channel.findtext("description")
                        or channel.findtext("{*}description")
                        or default_values["description"]
                    )
                else:
                    # If no channel or feed is found, use default values
                    title, link, description = (
                        default_values["title"],
                        default_values["link"],
                        default_values["description"],
                    )

        except (URLError, ET.ParseError) as e:
            # Handle URL errors and XML parsing errors
            print(f"Failed to fetch or parse RSS feed: {e}")
            return None

    return f">>> {title} ({link}) - {description}"


# Test with sample RSS feed URLs
print(get_rss("https://cassidoo.co/rss.xml"))
print(get_rss("https://feed.syntax.fm/"))
print(get_rss("https://techcrunch.com/feed/"))
print(
    get_rss("https://www.theverge.com/rss/index.xml")
)  # Should fail with standard lib
print(
    get_rss("https://feeds.feedburner.com/PythonSoftwareFoundationNews")
)  # Should fail with standard lib
print(get_rss("https://github.blog/feed/"))
print(get_rss("https://stackoverflow.blog/feed/"))
print(get_rss("https://lifehacker.com/rss"))
print(get_rss("https://zenhabits.net/feed/"))
print(get_rss("https://seths.blog/feed/"))

```