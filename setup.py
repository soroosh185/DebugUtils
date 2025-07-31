from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name="devwraps",
	version="0.1.0",
	author="Soroosh Fathi",
	author_email="your@email.com",
	description="Powerful decorators for debugging, confirmation, and logging",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/yourusername/devwraps",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	install_requires=[
		"colorama>=0.4.0"
	],
)