from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zap",
    version="1.0.0",
    author="Jassem Manita",
    description="ZAP - A package installer that actually makes sense. Shows you what's happening and doesn't reinstall stuff you already have.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jassem/zap",
    py_modules=["zap"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Installation/Setup",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "zap=zap:main",
        ],
    },
    keywords="pip, package, installer, requirements, dry-run",
    project_urls={
        "Bug Reports": "https://github.com/jassem/zap/issues",
        "Source": "https://github.com/jassem/zap",
    },
)
