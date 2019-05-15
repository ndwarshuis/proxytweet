import setuptools

with open("README.org", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ProxyFeed",
    version="0.0.1",
    author="Nathan Dwarhsuis",
    author_email="natedwarshuis@gmail.com",
    description="A lightweight Twitter to RSS feed generator",
    long_description=long_description,
    long_description_content_type="text/x-org",
    url="https://github.com/ndwarshuis/proxytweet",
    zip_safe=False,
    include_package_data=True,
    packages=["proxytweet"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
