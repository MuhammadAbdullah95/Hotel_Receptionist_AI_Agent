from setuptools import find_packages, setup

setup(
    name="QAsystem with haystack",
    version="0.1",
    author="Abdullah",
    author_email="aideveloper453@gmail.com",
    packages=find_packages(),
    install_requires=["haystack-ai", "pinecone-haystack", "fastapi[standard]", "uvicorn", "pathlib", "python-dotenv"]
)