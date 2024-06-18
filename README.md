
# GistMaster

Welcome to **GistMaster**, my **Gists catalogue**!
This repository is automatically updated and organised, to provide a structured and visually appealing way to browse and understand them.

## About

I'm **[@rjvitorino](https://github.com/rjvitorino)**, and my open-source contributions are available on my **[Github profile](https://github.com/rjvitorino)**.
In this repository, you will find solutions to various interview questions, coding challenges, random snippets and scripts I've created.
These gists are automatically fetched and updated using **Github Actions** and can be set in your profile as well. 

👉 **[Check out my Gists below](#gists)** to see my work and explore the code samples.

## Installation and Setup

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
    pip install -r scripts/requirements.pip
    ```

4. **Set environment variables**:
    - `GITHUB_USERNAME`: Your GitHub username.
    - `GISTMASTER_TOKEN`: Your personal access token with access to your gists (you will need to set one up in Github).

5. **Run the tests, and if they are good, then the update script**:
    ```bash
    pytest
    # If the tests run succesfully you can then run the script
    python3 scripts/update_gists.py
    ```

6. **Set up GitHub Actions**:
    - Ensure you have a `.github/workflows/update_gists.yml` file.
    - Update the file to include your repository and branch details.


## Gists

### [Gist no. 1](gists/20240603-only_evens-gist/index.md)

* **Description**: Cassidoo's interview question of the week: a function that takes an array of integers and returns a new array containing only the even numbers, and sorted.
* **Language**: Python
* **Created at**: 2024-06-03
* **Last updated at**: 2024-06-07

### [Gist no. 2](gists/20240610-four_sum-gist/index.md)

* **Description**: Cassidoo's interview question of the week: a function that takes an array of integers and a target sum, and returns all unique quadruplets [a, b, c, d] in the array such that a + b + c + d = target
* **Language**: Python
* **Created at**: 2024-06-10
* **Last updated at**: 2024-06-10

### [Gist no. 3](gists/20240617-sort_vowels-gist/index.md)

* **Description**: Cassidoo's interview question of the week: a function that takes a list of names and returns the names sorted by the number of vowels in each name in descending order. If two names have the same number of vowels, sort them alphabetically.
* **Language**: Python
* **Created at**: 2024-06-17
* **Last updated at**: 2024-06-17