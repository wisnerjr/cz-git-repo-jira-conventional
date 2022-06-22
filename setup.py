from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cz_git_jira_conventional",
    version="1.0.0",
    py_modules=["cz_git_jira_conventional"],
    author="Wisner Júnior",
    author_email="wisner@gmail.com",
    license="MIT",
    url="https://github.com/wisnerjr/cz-git-jira-conventional/",
    install_requires=["commitizen"],
    description="Extend the commitizen tools to create conventional commits and README that link to Jira and Git repo.",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
