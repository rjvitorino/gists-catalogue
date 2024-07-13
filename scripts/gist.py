from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import Optional


@dataclass
class GistFile:
    """
    Represents a file within a Github Gist.
    """

    filename: str = ""
    type: str = ""
    language: Optional[str] = None
    raw_url: str = ""
    size: int = 0


@dataclass
class Gist:
    """
    Represents a Github Gist.
    """

    url: str = ""
    forks_url: str = ""
    commits_url: str = ""
    id: str = ""
    node_id: str = ""
    git_pull_url: str = ""
    git_push_url: str = ""
    html_url: str = ""
    files: Dict[str, GistFile] = field(default_factory=dict)
    public: bool = False
    created_at: str = ""
    updated_at: str = ""
    description: str = ""
    comments: int = 0
    comments_url: str = ""
    owner: Dict[str, str] = field(default_factory=dict)
    truncated: bool = False

    @staticmethod
    def from_dict(gist: Dict) -> "Gist":
        """
        Creates a Gist instance from a dictionary.

        Args:
            gist (Dict): A dictionary containing information provided from Github API.

        Returns:
            Gist: A Gist object created from the provided dictionary.
        """
        files = {
            file_name: GistFile(**file_content)
            for file_name, file_content in gist.get("files", {}).items()
        }
        return Gist(
            url=gist.get("url", ""),
            forks_url=gist.get("forks_url", ""),
            commits_url=gist.get("commits_url", ""),
            id=gist.get("id", ""),
            node_id=gist.get("node_id", ""),
            git_pull_url=gist.get("git_pull_url", ""),
            git_push_url=gist.get("git_push_url", ""),
            html_url=gist.get("html_url", ""),
            files=files,
            public=gist.get("public", False),
            created_at=gist.get("created_at", ""),
            updated_at=gist.get("updated_at", ""),
            description=gist.get("description", ""),
            comments=gist.get("comments", 0),
            comments_url=gist.get("comments_url", ""),
            owner=gist.get("owner", {}),
            truncated=gist.get("truncated", False),
        )
