import logging
from requests import HTTPError


try:
    # Import for normal execution
    from utils import fetch_gists
    from utils import create_gist_index
    from utils import save_gist_files
    from utils import update_readme
except ImportError:
    # Import for testing context
    from scripts.utils import fetch_gists
    from scripts.utils import create_gist_index
    from scripts.utils import save_gist_files
    from scripts.utils import update_readme

# Configure logging
logging.basicConfig(level=logging.INFO, filename='gist_catalogue.log', 
                    format='%(asctime)s:%(levelname)s:%(message)s')

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
            save_gist_files(gist, folder_name)
            logging.info(f"Processed gist: {folder_name}")
        
        logging.info("Updating README...")    
        update_readme(sorted_gists)
        
        logging.info("Gists update complete.")

    except HTTPError as http_error:
        logging.error(f"HTTP error occurred: {http_error}")
    except Exception as error:
        # TODO remove Pokemon exception
        logging.error(f"An error occurred: {error}")

if __name__ == '__main__':
    main()