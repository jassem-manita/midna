[![codecov](https://codecov.io/gh/jassem-manita/midna/branch/main/graph/badge.svg)](https://codecov.io/gh/jassem-manita/midna)
[![Security Scan](https://github.com/jassem-manita/midna/workflows/Security%20Scanning/badge.svg)](https://github.com/jassem-manita/midna/actions)

# Midna - The Smart Python Package Assistant

An intelligent tool that automatically manages your Python dependencies by analyzing your actual code usage.

## What is Midna?

Midna - The smart Python package assistant that automatically discovers what packages your Python project uses by scanning your code for imports. No more manually maintaining requirements.txt files or trying to remember what you installed.

```bash
midna                    # Auto-discovers and installs what you need
midna --dry-run          # See what it would install first
midna --uninstall        # Remove packages you don't use anymore
```

## Why Midna exists

Common Python package management challenges:

- Manual maintenance of requirements.txt files
- Difficulty tracking essential package dependencies
- Unnecessary installation of unused packages
- Inconsistencies between requirements and actual code usage

Midna addresses these challenges through intelligent code analysis and automated dependency management, ensuring your project only includes the packages it actually needs.

## Installation

Simply run:

```bash
pip install midna
```

Once installed, Midna is available system-wide and ready to optimize your Python package management.

## How to use it

### Auto-discovery (the main feature)

```bash
midna                    # Install missing packages
midna --dry-run          # Preview what would be installed
midna --uninstall        # Remove unused packages
midna --verbose          # See what it's doing
```

### Traditional mode (if you have requirements files)

```bash
midna requirements.txt
midna requirements.txt --dry-run
```

## How it works

1. **Looks for requirements files first** - requirements.txt, pyproject.toml, setup.py, etc.
2. **If none found, scans your .py files** for import statements
3. **Filters out standard library stuff** - only suggests real packages
4. **Shows you what it found** and what needs to be installed
5. **Does the installation** (or uninstallation) if you want

## Example output

```bash
$ midna --dry-run
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

```bash
midna [requirements_file] [options]

Options:
  --uninstall, -u    Remove packages instead of installing
  --dry-run, -n      Show what would happen without doing it
  --verbose, -v      More detailed output
  --version          Show version
  --help, -h         This help message
```

## Key Features

- **Intelligent Package Detection** - Installs only required dependencies
- **Standard Library Awareness** - Automatically excludes built-in Python modules
- **Smart Directory Filtering** - Ignores non-project directories (`.git`, `__pycache__`, `.venv`)
- **Multi-Format Support** - Compatible with requirements.txt, pyproject.toml, and Pipfile
- **Safe Execution** - Provides dry-run mode for verification
- **Robust Error Handling** - Ensures reliable operation across diverse codebases

## Security

Midna implements automated security scanning to ensure safe package management:

- **Dependency Vulnerability Scanning** - Weekly checks for known CVEs using pip-audit
- **Code Security Analysis** - Bandit security linting on every commit
- **Secure Subprocess Execution** - Explicit `shell=False` in all pip calls
- **Minimal Attack Surface** - Only `tomli` dependency for TOML parsing

Security reports are automatically generated and can be found in the [Actions tab](https://github.com/jassem-manita/midna/actions).

For security-related issues, please see [SECURITY.md](https://github.com/jassem-manita/midna/blob/main/SECURITY.md).

## Use cases

**New project setup:**

```bash
git clone some-repo
cd some-repo
midna  # installs exactly what the code needs
```

**Clean up your environment:**

```bash
midna --uninstall --dry-run  # see what can be removed
midna --uninstall            # actually remove it
```

**Check what your project uses:**

```bash
midna --dry-run --verbose  # detailed analysis
```

## Project structure

```text
midna/
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
5. Run security checks: `bandit -r midna/ -x tests,test`
6. Submit a PR

All contributions are automatically tested for security issues using Bandit and pip-audit.

## License

Apache 2.0 - see [LICENSE](https://github.com/jassem-manita/midna/blob/main/LICENSE)

## Author

Jassem Manita  
GitHub: [@jassem-manita](https://github.com/jassem-manita)  
Email: jasemmanita00 [at] gmail.com