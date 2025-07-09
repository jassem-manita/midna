from setuptools import setup

if __name__ == "__main__":
    setup(
        name="zap",
        version="0.1.0",
        description="A simple and friendly pip requirements installer with pre-install checks",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        author="Jassem",
        author_email="jasemmanita00@gmail.com",
        url="https://github.com/jassem-manita/zap",
        py_modules=["zap"],
        install_requires=[],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
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
            "Bug Reports": "https://github.com/jassem-manita/zap/issues",
            "Source": "https://github.com/jassem-manita/zap",
        },
    )
