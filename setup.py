from setuptools import setup

if __name__ == "__main__":
    setup()
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
