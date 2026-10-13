from pathlib import Path
import shutil
import subprocess
import sys

from . import options

class Builder:
    def __init__(self):
        self.root = Path.cwd() / "generated" / options.name
        
        if self.root.exists():
            shutil.rmtree(self.root)
        
        source_template = Path("templates/main.txt").read_text("utf-8")
        self.source = source_template.format(
            name=repr(options.name),
            url=repr(options.url),
        )
        self.script = self.root / "main.py"
        
        self.command = [
            sys.executable, "-m", "PyInstaller",
            "--noconfirm",
            "--clean",
            "--onefile",
            "--windowed",
            "--name", options.name,
            "--distpath", str(self.root / "dist"),
            "--workpath", str(self.root / "build"),
            "--specpath", str(self.root)
        ]
        
        if options.icon:
            self.command.extend([
                "--icon", str(self.root / options.icon.name),
                "--add-data", f"{self.root / options.icon.name};."
            ])
        
    def build(self):
        self.root.mkdir(parents=True, exist_ok=True)
        self.script.write_text(self.source, "utf-8")
        
        if options.icon:
            icon = options.icon.resolve()
            shutil.copy2(icon, self.root / options.icon.name)
        
        subprocess.run([*self.command, str(self.script)], check=True)

        print(f"Built Web App: {self.root / 'dist'}")