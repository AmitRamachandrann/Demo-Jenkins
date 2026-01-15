"""Setup configuration for py-gha package."""

from setuptools import setup, find_packages

setup(
    name="py-gha",
    version="1.0.0",
    description="Enterprise Hello World Flask Application for CloudBees Unify Demo",
    author="CloudBees",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.11",
    install_requires=[
        "flask>=3.0.0",
        "werkzeug>=3.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "black>=23.12.1",
            "flake8>=7.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "py-gha=app.main:app.run",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
