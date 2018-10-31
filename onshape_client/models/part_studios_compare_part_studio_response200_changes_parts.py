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

from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_collection_changes import PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges  # noqa: F401,E501


class PartStudiosComparePartStudioResponse200ChangesParts(object):
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
        'type': 'str',
        'collection_changes': 'list[PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges]'
    }

    attribute_map = {
        'type': 'type',
        'collection_changes': 'collectionChanges'
    }

    def __init__(self, type=None, collection_changes=None):  # noqa: E501
        """PartStudiosComparePartStudioResponse200ChangesParts - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._collection_changes = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if collection_changes is not None:
            self.collection_changes = collection_changes

    @property
    def type(self):
        """Gets the type of this PartStudiosComparePartStudioResponse200ChangesParts.  # noqa: E501

        Type of the differences in Part collection in the Part             Studio (see API description for values)  # noqa: E501

        :return: The type of this PartStudiosComparePartStudioResponse200ChangesParts.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartStudiosComparePartStudioResponse200ChangesParts.

        Type of the differences in Part collection in the Part             Studio (see API description for values)  # noqa: E501

        :param type: The type of this PartStudiosComparePartStudioResponse200ChangesParts.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def collection_changes(self):
        """Gets the collection_changes of this PartStudiosComparePartStudioResponse200ChangesParts.  # noqa: E501

        List of changes in Part Studio Parts             collection  # noqa: E501

        :return: The collection_changes of this PartStudiosComparePartStudioResponse200ChangesParts.  # noqa: E501
        :rtype: list[PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges]
        """
        return self._collection_changes

    @collection_changes.setter
    def collection_changes(self, collection_changes):
        """Sets the collection_changes of this PartStudiosComparePartStudioResponse200ChangesParts.

        List of changes in Part Studio Parts             collection  # noqa: E501

        :param collection_changes: The collection_changes of this PartStudiosComparePartStudioResponse200ChangesParts.  # noqa: E501
        :type: list[PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges]
        """

        self._collection_changes = collection_changes

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
        if not isinstance(other, PartStudiosComparePartStudioResponse200ChangesParts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
