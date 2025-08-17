# WAMYA - Smart Python Package Manager

A better way to manage Python dependencies that actually figures out what you need.

## What is WAMYA?

WAMYA automatically discovers what packages your Python project uses by scanning your code for imports. No more manually maintaining requirements.txt files or trying to remember what you installed.

```bash
wamya                    # Auto-discovers and installs what you need
wamya --dry-run          # See what it would install first
wamya --uninstall        # Remove packages you don't use anymore
```

## Why I built this

I got tired of:
- Manually updating requirements.txt files
- Forgetting what packages I actually need
- Installing everything when I only need a few packages
- Requirements files getting out of sync with actual code

ZAP solves this by looking at your actual Python imports and managing packages based on what you're really using.

## Installation

```bash
git clone https://github.com/jassem-manita/wamya.git
cd wamya
pip install .
```

That's it. WAMYA is now available globally.

## How to use it

### Auto-discovery (the main feature)
```bash
wamya                    # Install missing packages
wamya --dry-run          # Preview what would be installed
wamya --uninstall        # Remove unused packages
wamya --verbose          # See what it's doing
```

### Traditional mode (if you have requirements files)
```bash
wamya requirements.txt
wamya requirements.txt --dry-run
```

## How it works

1. **Looks for requirements files first** - requirements.txt, pyproject.toml, setup.py, etc.
2. **If none found, scans your .py files** for import statements
3. **Filters out standard library stuff** - only suggests real packages
4. **Shows you what it found** and what needs to be installed
5. **Does the installation** (or uninstallation) if you want

## Example output

```bash
$ zap --dry-run
Auto-discovering requirements...
Found 4 packages (import analysis)

Already installed (1):
  + requests

Missing packages (3):
  - click
  - numpy  
  - pandas

DRY RUN: Would install the following packages:
  - click
  - numpy
  - pandas
```

## Commands

```
zap [requirements_file] [options]

Options:
  --uninstall, -u    Remove packages instead of installing
  --dry-run, -n      Show what would happen without doing it
  --verbose, -v      More detailed output
  --version          Show version
  --help, -h         This help message
```

## Smart features

- **Only installs what's missing** - won't reinstall stuff you already have
- **Ignores standard library** - won't try to install `os` or `sys`
- **Skips common directories** - ignores `.git`, `__pycache__`, `.venv`, etc.
- **Handles multiple file types** - requirements.txt, pyproject.toml, Pipfile
- **Safe dry-run mode** - always check first
- **Proper error handling** - won't crash on weird files

## Use cases

**New project setup:**
```bash
git clone some-repo
cd some-repo
zap  # installs exactly what the code needs
```

**Clean up your environment:**
```bash
zap --uninstall --dry-run  # see what can be removed
zap --uninstall            # actually remove it
```

**Check what your project uses:**
```bash
zap --dry-run --verbose  # detailed analysis
```

## Project structure

```
src/
├── core.py          # Main CLI logic
├── discovery.py     # Auto-discovery engine  
├── parser.py        # Requirements file parsing
├── installer.py     # Package installation
├── uninstaller.py   # Package removal
├── checker.py       # Check what's installed
└── logger.py        # Logging
```

## Requirements

- Python 3.8 or newer
- pip (comes with Python)
- That's it - no external dependencies

## Contributing

Found a bug or want to add a feature? 

1. Fork it
2. Create a branch: `git checkout -b my-feature`
3. Install dev dependencies: `pip install -e ".[dev]"`
4. Run tests: `pytest tests/`
5. Submit a PR

## License

Apache 2.0 - see LICENSE file

## Author

Jassem Manita  
GitHub: [@jassem-manita](https://github.com/jassem-manita)  
Email: jasemmanita00@gmail.com