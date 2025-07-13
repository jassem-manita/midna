[1mdiff --git a/.gitignore b/.gitignore[m
[1mindex 4526226..589177d 100644[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@ -3,9 +3,6 @@[m [m__pycache__/[m
 *.py[cod][m
 *$py.class[m
 [m
[31m-# C extensions[m
[31m-*.so[m
[31m-[m
 # Distribution / packaging[m
 .Python[m
 build/[m
[36m@@ -20,87 +17,25 @@[m [mparts/[m
 sdist/[m
 var/[m
 wheels/[m
[31m-share/python-wheels/[m
 *.egg-info/[m
 .installed.cfg[m
 *.egg[m
[31m-MANIFEST[m
 [m
 # PyInstaller[m
 *.manifest[m
 *.spec[m
 [m
[31m-# Installer logs[m
[31m-pip-log.txt[m
[31m-pip-delete-this-directory.txt[m
[31m-[m
 # Unit test / coverage reports[m
 htmlcov/[m
 .tox/[m
[31m-.nox/[m
 .coverage[m
 .coverage.*[m
 .cache[m
 nosetests.xml[m
 coverage.xml[m
 *.cover[m
[31m-*.py,cover[m
 .hypothesis/[m
 .pytest_cache/[m
[31m-cover/[m
[31m-[m
[31m-# Translations[m
[31m-*.mo[m
[31m-*.pot[m
[31m-[m
[31m-# Django stuff:[m
[31m-*.log[m
[31m-local_settings.py[m
[31m-db.sqlite3[m
[31m-db.sqlite3-journal[m
[31m-[m
[31m-# Flask stuff:[m
[31m-instance/[m
[31m-.webassets-cache[m
[31m-[m
[31m-# Scrapy stuff:[m
[31m-.scrapy[m
[31m-[m
[31m-# Sphinx documentation[m
[31m-docs/_build/[m
[31m-[m
[31m-# PyBuilder[m
[31m-.pybuilder/[m
[31m-target/[m
[31m-[m
[31m-# Jupyter Notebook[m
[31m-.ipynb_checkpoints[m
[31m-[m
[31m-# IPython[m
[31m-profile_default/[m
[31m-ipython_config.py[m
[31m-[m
[31m-# pyenv[m
[31m-.python-version[m
[31m-[m
[31m-# pipenv[m
[31m-Pipfile.lock[m
[31m-[m
[31m-# poetry[m
[31m-poetry.lock[m
[31m-[m
[31m-# pdm[m
[31m-.pdm.toml[m
[31m-[m
[31m-# PEP 582[m
[31m-__pypackages__/[m
[31m-[m
[31m-# Celery stuff[m
[31m-celerybeat-schedule[m
[31m-celerybeat.pid[m
[31m-[m
[31m-# SageMath parsed files[m
[31m-*.sage.py[m
 [m
 # Environments[m
 .env[m
[36m@@ -111,37 +46,20 @@[m [mENV/[m
 env.bak/[m
 venv.bak/[m
 [m
[31m-# Spyder project settings[m
[31m-.spyderproject[m
[31m-.spyproject[m
[31m-[m
[31m-# Rope project settings[m
[31m-.ropeproject[m
[31m-[m
[31m-# mkdocs documentation[m
[31m-/site[m
[31m-[m
[31m-# mypy[m
[31m-.mypy_cache/[m
[31m-.dmypy.json[m
[31m-dmypy.json[m
[31m-[m
[31m-# Pyre type checker[m
[31m-.pyre/[m
[31m-[m
[31m-# pytype static type analyzer[m
[31m-.pytype/[m
[31m-[m
[31m-# Codeql databases[m
[31m-.codeql[m
[31m-[m
[31m-# PyCharm[m
[32m+[m[32m# IDE[m
[32m+[m[32m.vscode/[m
 .idea/[m
[32m+[m[32m*.swp[m
[32m+[m[32m*.swo[m
[32m+[m[32m*~[m
 [m
[31m-# VS Code[m
[31m-.vscode/[m
[32m+[m[32m# OS[m
[32m+[m[32m.DS_Store[m
[32m+[m[32mThumbs.db[m
 [m
[31m-# ZAP specific[m
[31m-test_req.txt[m
[31m-test_requirements.txt[m
[32m+[m[32m# Logs[m
 *.log[m
[32m+[m
[32m+[m[32m# Temporary files[m
[32m+[m[32m*.tmp[m
[32m+[m[32m*.bak[m
\ No newline at end of file[m
