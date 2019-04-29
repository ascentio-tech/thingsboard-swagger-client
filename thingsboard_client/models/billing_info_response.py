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
from thingsboard_client.models.tenant_id import TenantId  # noqa: F401,E501


class BillingInfoResponse(object):
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
        'message': 'str',
        'name': 'str',
        'quantity_of_meters': 'int',
        'tenant_id': 'TenantId'
    }

    attribute_map = {
        'message': 'message',
        'name': 'name',
        'quantity_of_meters': 'quantityOfMeters',
        'tenant_id': 'tenantId'
    }

    def __init__(self, message=None, name=None, quantity_of_meters=None, tenant_id=None):  # noqa: E501
        """BillingInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._name = None
        self._quantity_of_meters = None
        self._tenant_id = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if quantity_of_meters is not None:
            self.quantity_of_meters = quantity_of_meters
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def message(self):
        """Gets the message of this BillingInfoResponse.  # noqa: E501


        :return: The message of this BillingInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BillingInfoResponse.


        :param message: The message of this BillingInfoResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this BillingInfoResponse.  # noqa: E501


        :return: The name of this BillingInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingInfoResponse.


        :param name: The name of this BillingInfoResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def quantity_of_meters(self):
        """Gets the quantity_of_meters of this BillingInfoResponse.  # noqa: E501


        :return: The quantity_of_meters of this BillingInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._quantity_of_meters

    @quantity_of_meters.setter
    def quantity_of_meters(self, quantity_of_meters):
        """Sets the quantity_of_meters of this BillingInfoResponse.


        :param quantity_of_meters: The quantity_of_meters of this BillingInfoResponse.  # noqa: E501
        :type: int
        """

        self._quantity_of_meters = quantity_of_meters

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BillingInfoResponse.  # noqa: E501


        :return: The tenant_id of this BillingInfoResponse.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BillingInfoResponse.


        :param tenant_id: The tenant_id of this BillingInfoResponse.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

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
        if issubclass(BillingInfoResponse, dict):
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
        if not isinstance(other, BillingInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
