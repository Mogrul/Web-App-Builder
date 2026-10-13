from argparse import ArgumentParser, Namespace
from pathlib import Path
import re


def get_args() -> Namespace:
    parser = ArgumentParser()
    
    parser.add_argument(
        "url",
        help="Website URL"
    )
    
    parser.add_argument(
        "--name",
        required=True,
        help="Application Name"
    )
    
    parser.add_argument(
        "--icon",
        type=Path,
        help="Path to windows .ico file"
    )
    
    return parser.parse_args()

class Options:
    def __init__(self) -> None:
        args = get_args()
        
        self.url: str = args.url
        self.name: str = args.name
        self.icon: Path = args.icon
        
        self.verify()
    
    def verify(self):
        slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", self.name).strip("-")
                    
        if not slug:
            raise ValueError("App name must contain letters or numbers.")
    
        if not re.match(r"^https?://", self.url, re.IGNORECASE):
            raise ValueError("URL must start with http:// or https://")

        self.name = slug
        
        if self.icon:
            icon = self.icon.resolve()
            
            if not icon.is_file():
                raise FileNotFoundError(f"Icon not found: {icon}")
            
            if icon.suffix.lower() != ".ico":
                raise ValueError("Use a .ico file for the Windows app icon.")
            
