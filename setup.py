from setuptools import setup, Extension, find_packages
from pathlib import Path

long_description = Path("README.md").read_text(encoding="utf-8")

ext_modules = [
    Extension(
        "fastgraphFPMS._fastgraphFPMS",
        sources=["src/fastgraphFPMS/_fastgraphFPMS.c"],
    )
]

setup(
    name="fastgraphFPMS",
    version="0.1.1",
    description="Python library in C for graph and optimisation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Flavio D.",
    license="/",
    packages=find_packages("src"),
    package_dir={"": "src"},
    ext_modules=ext_modules,
    python_requires=">=3.8",
)
