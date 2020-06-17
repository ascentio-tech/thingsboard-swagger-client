# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AssetSearchQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'asset_types': 'list[str]',
        'parameters': 'RelationsSearchParameters',
        'relation_type': 'str'
    }

    attribute_map = {
        'asset_types': 'assetTypes',
        'parameters': 'parameters',
        'relation_type': 'relationType'
    }

    def __init__(self, asset_types=None, parameters=None, relation_type=None):  # noqa: E501
        """AssetSearchQuery - a model defined in Swagger"""  # noqa: E501
        self._asset_types = None
        self._parameters = None
        self._relation_type = None
        self.discriminator = None
        if asset_types is not None:
            self.asset_types = asset_types
        if parameters is not None:
            self.parameters = parameters
        if relation_type is not None:
            self.relation_type = relation_type

    @property
    def asset_types(self):
        """Gets the asset_types of this AssetSearchQuery.  # noqa: E501


        :return: The asset_types of this AssetSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._asset_types

    @asset_types.setter
    def asset_types(self, asset_types):
        """Sets the asset_types of this AssetSearchQuery.


        :param asset_types: The asset_types of this AssetSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._asset_types = asset_types

    @property
    def parameters(self):
        """Gets the parameters of this AssetSearchQuery.  # noqa: E501


        :return: The parameters of this AssetSearchQuery.  # noqa: E501
        :rtype: RelationsSearchParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this AssetSearchQuery.


        :param parameters: The parameters of this AssetSearchQuery.  # noqa: E501
        :type: RelationsSearchParameters
        """

        self._parameters = parameters

    @property
    def relation_type(self):
        """Gets the relation_type of this AssetSearchQuery.  # noqa: E501


        :return: The relation_type of this AssetSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this AssetSearchQuery.


        :param relation_type: The relation_type of this AssetSearchQuery.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AssetSearchQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetSearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
