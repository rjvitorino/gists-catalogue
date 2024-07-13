from pathlib import Path
from unittest.mock import patch
from unittest.mock import mock_open
from unittest.mock import MagicMock

from scripts.utils import fetch_gists
from scripts.utils import fetch_gist_content
from scripts.utils import format_date
from scripts.utils import generate_folder_name
from scripts.utils import save_gist_files
from scripts.utils import create_gist_index
from scripts.utils import update_readme
from scripts.gist import Gist

# Example data
example_gist_data = {
    "id": "1",
    "created_at": "2024-06-17T09:30:09Z",
    "updated_at": "2024-06-17T09:30:09Z",
    "description": "Test gist",
    "files": {
        "file1.py": {
            "filename": "file1.py",
            "raw_url": "https://gist.githubusercontent.com/rjvitorino/dfef5433066c061954d29d1b15202290/raw/54a0207aaf64e70e57a2063795b0a1c88a6b046c/file1.py",
            "language": "Python",
        }
    },
    "owner": {"login": "rjvitorino", "html_url": "https://github.com/rjvitorino"},
}

example_gist = Gist.from_dict(example_gist_data)


@patch("requests.get")
def test_fetch_gists(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [example_gist_data]
    mock_get.return_value = mock_response
    gists = fetch_gists()
    assert len(gists) == 1
    assert gists[0].id == "1"


@patch("requests.get")
def test_fetch_gist_content(mock_get):
    mock_response = MagicMock()
    mock_response.text = "print('Hello, world!')"
    mock_get.return_value = mock_response
    content = fetch_gist_content(
        "https://gist.githubusercontent.com/rjvitorino/dfef5433066c061954d29d1b15202290/raw/54a0207aaf64e70e57a2063795b0a1c88a6b046c/file1.py"
    )
    assert content == "print('Hello, world!')"


def test_format_date():
    assert format_date("2024-06-17T09:30:09Z") == "2024-06-17"
    assert format_date("2024-06-17T09:30:09Z", "YYYYMMDD") == "20240617"


def test_generate_folder_name():
    folder_name = generate_folder_name(example_gist)
    assert folder_name == "20240617-file1-gist"


@patch("builtins.open", new_callable=mock_open)
@patch("scripts.utils.fetch_gist_content")
def test_save_gist_files(mock_fetch_content, mock_file):
    mock_fetch_content.return_value = "print('Hello, world!')"
    save_gist_files(example_gist)
    mock_file.assert_called_with(Path("gists/20240617-file1-gist/files/file1.py"), "w")
    mock_file().write.assert_called_with("print('Hello, world!')")


@patch("builtins.open", new_callable=mock_open)
def test_create_gist_index(mock_file):
    create_gist_index(example_gist)
    mock_file.assert_called_with(Path("gists/20240617-file1-gist/index.md"), "w")
    # Adjust the assertion to match the actual content
    calls = mock_file().write.call_args_list
    assert any(call[0][0].startswith("# 20240617-file1-gist") for call in calls)


@patch("builtins.open", new_callable=mock_open)
def test_update_readme(mock_file):
    update_readme([example_gist])
    mock_file.assert_called_with(Path("README.md"), "w")
    # Adjust the assertion to match the actual content
    calls = mock_file().write.call_args_list
    assert any("## Gists" in call[0][0] for call in calls)
