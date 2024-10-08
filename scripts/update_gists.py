import json
import logging

from requests import HTTPError

try:
    # Import for normal execution
    from utils import create_gist_index, fetch_gists, save_gist_files, update_readme
except ImportError:
    # Import for testing context
    from scripts.utils import (
        create_gist_index,
        fetch_gists,
        save_gist_files,
        update_readme,
    )

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename="gist_catalogue.log",
    format="%(asctime)s:%(levelname)s:%(message)s",
)


# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)


def main() -> None:
    """
    Main function to fetch the Gists from Github API, update the local files, and update the README.
    """
    try:
        logging.info("Fetching gists...")
        gists = fetch_gists()

        logging.info("Sorting gists by creation date...")
        sorted_gists = sorted(gists, key=lambda gist: gist.created_at)

        logging.info("Creating gists directories and files...")
        for gist in sorted_gists:
            folder_name = create_gist_index(gist)
            if config["fetch_gist_code"] is True:
                save_gist_files(gist, folder_name)
            logging.info(f"Processed gist: {folder_name}")

        logging.info("Updating README...")
        update_readme(sorted_gists, config["display_format"] == "table")

        logging.info("Gists update complete.")

    except HTTPError as http_error:
        logging.error(f"HTTP error occurred: {http_error}")
    except Exception as error:
        # TODO remove Pokemon exception
        logging.error(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
