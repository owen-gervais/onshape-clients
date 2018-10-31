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

from onshape_client.models.part_studios_get_translation_formats_response200_items import PartStudiosGetTranslationFormatsResponse200Items  # noqa: F401,E501


class AssembliesGetTranslationFormatsResponse200(object):
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
        'items': 'list[PartStudiosGetTranslationFormatsResponse200Items]'
    }

    attribute_map = {
        'items': 'items'
    }

    def __init__(self, items=None):  # noqa: E501
        """AssembliesGetTranslationFormatsResponse200 - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self.discriminator = None

        if items is not None:
            self.items = items

    @property
    def items(self):
        """Gets the items of this AssembliesGetTranslationFormatsResponse200.  # noqa: E501

        Array of translation formats  # noqa: E501

        :return: The items of this AssembliesGetTranslationFormatsResponse200.  # noqa: E501
        :rtype: list[PartStudiosGetTranslationFormatsResponse200Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AssembliesGetTranslationFormatsResponse200.

        Array of translation formats  # noqa: E501

        :param items: The items of this AssembliesGetTranslationFormatsResponse200.  # noqa: E501
        :type: list[PartStudiosGetTranslationFormatsResponse200Items]
        """

        self._items = items

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
        if not isinstance(other, AssembliesGetTranslationFormatsResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
