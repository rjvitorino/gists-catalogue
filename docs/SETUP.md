# Installation and Setup

To run this repository on your own GitHub profile, please [fork it](https://github.com/rjvitorino/gists-catalogue/fork) and follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/YOUR-USERNAME/gists-catalogue.git
    cd gists-catalogue
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv gists-venv
    source gists-venv/bin/activate  # On Windows, use `gists-venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables**:

    - `GITHUB_USERNAME`: Your GitHub username.
    - `GISTMASTER_TOKEN`: Your personal access token with access to your gists.

5. **Run the tests, and if they are good, then the update script**:

    ```bash
    pytest
    # If the tests run successfully you can try to run the script
    python3 scripts/update_gists.py
    ```

6. **Set up GitHub Actions**:

    - Ensure you have a `.github/workflows/update_gists.yml` file.
    - Update the file to include your repository and branch details.


## Configuration

You can choose to display the gists in a table or list format and decide whether to fetch and store the gists code locally or not.
To configure these options, update the `config.json` file in the root of the repository.

```json
{
    "display_format": "table",  // or "list"
    "fetch_gist_code": true      // or false
}
```

## Additional Information

You can find more details about contributing in our [CONTRIBUTING.md](CONTRIBUTING.md) file and our code of conduct in the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.

For any issues or questions, please open an issue on GitHub or contact me directly via my [GitHub profile](https://github.com/rjvitorino).
