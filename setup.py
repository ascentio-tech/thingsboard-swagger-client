# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "thingsboard-client"
VERSION = "2.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Thingsboard REST API",
    author_email="info@thingsboard.io",
    url="",
    keywords=["Swagger", "Thingsboard REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    For instructions how to authorize requests please visit &lt;a href&#x3D;&#x27;http://thingsboard.io/docs/reference/rest-api/&#x27;&gt;REST API documentation page&lt;/a&gt;.  # noqa: E501
    """
)
