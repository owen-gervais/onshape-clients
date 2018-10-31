# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from onshape_client.models.parts_get_edges_response200_parts import PartsGetEdgesResponse200Parts  # noqa: F401,E501


class PartsGetEdgesResponse200(object):
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
        'parts': 'list[PartsGetEdgesResponse200Parts]'
    }

    attribute_map = {
        'parts': 'parts'
    }

    def __init__(self, parts=None):  # noqa: E501
        """PartsGetEdgesResponse200 - a model defined in Swagger"""  # noqa: E501

        self._parts = None
        self.discriminator = None

        if parts is not None:
            self.parts = parts

    @property
    def parts(self):
        """Gets the parts of this PartsGetEdgesResponse200.  # noqa: E501

        Array containing response info for each part  # noqa: E501

        :return: The parts of this PartsGetEdgesResponse200.  # noqa: E501
        :rtype: list[PartsGetEdgesResponse200Parts]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this PartsGetEdgesResponse200.

        Array containing response info for each part  # noqa: E501

        :param parts: The parts of this PartsGetEdgesResponse200.  # noqa: E501
        :type: list[PartsGetEdgesResponse200Parts]
        """

        self._parts = parts

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PartsGetEdgesResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
