# Midna Improvements Tracker

## Core Functionality Issues

### Critical

- [ ] UTF-8 encoding issue when creating requirements files
- [ ] Unicode encoding errors in logging (BOM character handling)
- [ ] No validation of package existence before attempting installation
- [ ] Incorrect handling of malformed requirement specifications
- [ ] No proper handling of circular dependencies
- [ ] Comments incorrectly parsed as package names
- [ ] Incorrect parsing of complex version specifiers (e.g., !=, ~=)

### Package Management

- [ ] No support for package extras (e.g., pandas[excel])
- [ ] No handling of local path installations
- [ ] No support for editable installs (-e flag)
- [ ] No handling of meta-package dependencies
- [ ] No support for platform-specific requirements
- [ ] No handling of environment markers
- [ ] No support for constraints files (-c flag)
- [ ] Build tags not properly parsed (e.g., +mkl suffix)

## User Interface Improvements

### Visual Elements

- [ ] No progress bar/spinner during package installation
- [ ] No color coding in output (green for installed, yellow for updates)
- [ ] No visual indication of dependency relationships
- [ ] No clear differentiation between comments and package specifications
- [x] Help text still mentions "zap" instead of "midna" in examples

### Output Formatting

- [ ] Large requirements files show excessive output
- [ ] No smart output truncation or summarization
- [ ] No proper formatting for inline comments
- [ ] Environment variable references not clearly marked
- [ ] Character encoding issues with PowerShell output

## User Experience Enhancements

### Installation Process

- [ ] No indication of total installation size
- [ ] No feedback on installation progress
- [ ] No estimated installation time
- [ ] No warning for potentially malicious packages
- [ ] No cache management commands

### Dependency Management

- [ ] No bulk upgrade command for outdated packages
- [ ] No dependency resolution preview
- [ ] No handling of version conflicts
- [ ] No detection of conflicting dependencies
- [ ] No dependency tree visualization

## Security

- [ ] No hash verification support for secure installations
- [ ] No warning for potentially malicious packages
- [ ] No validation of package sources
- [ ] No support for private repository authentication
- [ ] No verification of package signatures

## Performance

- [ ] No parallel download support
- [ ] No caching of package metadata
- [ ] No optimization for repeated installations
- [ ] No lazy loading of package information
- [ ] No smart package download order

## Documentation

- [ ] Missing environment variables documentation
- [ ] No virtual environment usage examples
- [ ] No troubleshooting section
- [ ] Lack of API documentation
- [ ] Missing examples for common use cases
- [ ] No documentation for error codes
- [ ] No integration guides

## Environment Management Features

### Environment Detection & Info
- [ ] Detect current Python environment (venv, conda, system)
- [ ] Display Python version, environment type, and installed packages
- [ ] Add CLI command to show environment information
- [ ] Show environment path and activation status
- [ ] Display environment size and package count

### Automatic Environment Creation
- [ ] Auto-create virtual environment if none exists
- [ ] Auto-create conda environment if none exists
- [ ] Auto-install dependencies from requirements.txt after environment creation
- [ ] Support for different Python versions in environment creation
- [ ] Environment naming and configuration options

### Dependency Pinning & Lock File Support
- [ ] Resolve and freeze exact versions of all dependencies
- [ ] Generate requirements.lock with pinned versions
- [ ] Install dependencies from lock file for reproducibility
- [ ] Update existing lock files
- [ ] Support for different lock file formats

### Export/Import Environment
- [ ] Export current environment to requirements.txt
- [ ] Export environment to conda environment.yml
- [ ] Install environment from requirements file
- [ ] Install environment from conda YAML
- [ ] Cross-platform environment compatibility

### Environment Cleanup
- [ ] Clean unused packages not in requirements
- [ ] Reset environment to clean state
- [ ] Remove orphaned dependencies
- [ ] Environment health check and repair
- [ ] Backup and restore environment state

## Advanced Features

### Dependency Management Enhancements
- [ ] No detection of conflicting dependencies between meta-packages
- [ ] No warning about optional vs required dependencies
- [ ] No handling of environment markers (e.g., sys_platform conditions)
- [ ] No support for development vs production requirements separation
- [ ] No handling of dependency groups or requirement categories
- [ ] No support for build tags or binary distribution preferences
- [ ] No handling of Git repository references with specific branches/tags
- [ ] No support for constraints files (-c flag)
- [ ] No interactive mode for package selection
- [ ] No dependency tree visualization
- [ ] No way to see package download size before install
- [ ] No estimated installation time  
- [ ] No suggestions for commonly paired packages
- [ ] No conflict warnings before installation

### Additional Features
- [ ] No export current environment feature
- [ ] No cache management commands

## Completed Features ✅

- [x] Clear output formatting
- [x] Auto-discovery works well  
- [x] Dry-run feature is helpful
- [x] Verbose mode provides good debugging info
- [x] Requirements file validation works well
- [x] Version command functionality
- [x] Help command with examples
- [x] Package installation/uninstall core functionality
- [x] Logging support
- [x] Output to file functionality

## Documentation Gaps
- [ ] Missing environment variables documentation
- [ ] No virtual environment usage examples
- [ ] No troubleshooting section
- [ ] Update README with new CLI features
- [ ] Add comprehensive tests for new functionality
- [ ] Real-world usage scenarios and examples
