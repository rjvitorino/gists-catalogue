import logging
from requests import HTTPError
from utils import fetch_gists
from utils import create_gist_index
from utils import save_gist_files
from utils import update_readme

# Configure logging
logging.basicConfig(level=logging.INFO, filename='gist_catalogue.log', 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main() -> None:
    """
    Main function to fetch the Gists from Github API, update the local files, and update the README.
    """
    try:
        gists = fetch_gists()
        for gist in gists:
            folder_name = create_gist_index(gist)
            save_gist_files(gist, folder_name)
        update_readme(gists)
    except HTTPError as http_error:
        logging.error(f"HTTP error occurred: {http_error}")
    except Exception as error:
        # TODO remove Pokemon exception
        logging.error(f"An error occurred: {error}")

if __name__ == '__main__':
    main()