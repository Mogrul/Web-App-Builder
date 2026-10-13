# Web-App-Builder

Turn any website into a standalone Windows desktop application.

Web-App-Builder takes a website URL and generates a Windows `.exe` that opens the website in its own application window using Python and `pywebview` with Microsoft Edge WebView2.

## Features

- **Website to desktop app** — wrap any HTTP or HTTPS website in a standalone application.
- **Custom application names** — set the window title and executable name.
- **Custom icons** — provide a Windows `.ico` file for the generated executable.
- **Persistent browser storage** — retain cookies, login sessions, and local storage between launches when persistent storage is configured.
- **Standalone executable** — package the application using PyInstaller.
- **No browser interface** — display the website without the usual browser address bar, tabs, or toolbars.

## Requirements

- Windows
- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)
- Microsoft Edge WebView2 Runtime
- A website accessible from your computer

## Installation

Clone the repository:

```bash
git clone https://github.com/Mogrul/Web-App-Builder.git
cd Web-App-Builder
```

Install the project dependencies:

```bash
uv sync
```

## Usage

Run Web-App-Builder with a website URL and application name:

```bash
uv run python -m webapp_builder "https://example.com" --name Example
```

Replace the URL with the website you want to turn into an application.

### Command-line options

| Argument | Required | Description |
|---|---|---|
| `url` | Yes | Website URL. Must start with `http://` or `https://`. |
| `--name` | Yes | Application name, used for the generated executable and window title. |
| `--icon` | No | Path to a Windows `.ico` file. |

### Examples

**Create an application without a custom icon:**

```bash
uv run python -m webapp_builder "https://example.com" --name Example
```

**Create a Plex application:**

```bash
uv run python -m webapp_builder "http://192.168.0.103:32400/" --name Plex
```

**Create an application with a custom icon:**

```bash
uv run python -m webapp_builder "https://example.com" --name Example --icon icons/example.ico
```

Icon paths can be absolute or relative to the current working directory.

## Output

Generated applications are saved under the `generated` directory.

```text
generated/
└── Example/
    ├── main.py
    ├── Example.spec
    ├── build/
    └── dist/
        └── Example.exe
```

The executable is located in `dist/`. You can copy it elsewhere and run it like a normal Windows application.

## Browser storage and login sessions

Generated applications can use persistent WebView2 storage to retain cookies, authentication sessions, and local storage between launches.

Browser data should be stored separately from the executable, in the user's application data directory. This means rebuilding or updating the executable does not inherently erase the saved login session.

Websites can still expire or revoke sessions, and some authentication mechanisms may require signing in again.

## How it works

1. Parses and validates the command-line arguments.
2. Generates a Python application from the project template.
3. Configures the website URL, application name, and optional icon.
4. Runs PyInstaller to package the generated application.
5. Outputs the finished Windows executable.

## Limitations

- **Windows-focused:** the build process targets Windows executables.
- **WebView2 required:** the target computer needs the Microsoft Edge WebView2 Runtime.
- **Internet or network access:** the website must be reachable from the target computer.
- **Website compatibility:** browser-dependent features, DRM-protected media, and certain authentication flows may not work on every website.
- **Icon format:** custom icons must use the `.ico` format.

## Dependencies

- [pywebview](https://github.com/r0x0r/pywebview) — native desktop windows for web applications.
- [PyInstaller](https://pyinstaller.org/) — packages Python applications into executables.
- [uv](https://docs.astral.sh/uv/) — Python project and dependency management.

## License

See [LICENSE](LICENSE) for licensing information.
