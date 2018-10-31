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

from onshape_client.models.part_studios_get_edges_response200_edges import PartStudiosGetEdgesResponse200Edges  # noqa: F401,E501


class PartStudiosGetEdgesResponse200Parts(object):
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
        'edges': 'list[PartStudiosGetEdgesResponse200Edges]',
        'id': 'str'
    }

    attribute_map = {
        'edges': 'edges',
        'id': 'id'
    }

    def __init__(self, edges=None, id=None):  # noqa: E501
        """PartStudiosGetEdgesResponse200Parts - a model defined in Swagger"""  # noqa: E501

        self._edges = None
        self._id = None
        self.discriminator = None

        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id

    @property
    def edges(self):
        """Gets the edges of this PartStudiosGetEdgesResponse200Parts.  # noqa: E501

        Edges of a part  # noqa: E501

        :return: The edges of this PartStudiosGetEdgesResponse200Parts.  # noqa: E501
        :rtype: list[PartStudiosGetEdgesResponse200Edges]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this PartStudiosGetEdgesResponse200Parts.

        Edges of a part  # noqa: E501

        :param edges: The edges of this PartStudiosGetEdgesResponse200Parts.  # noqa: E501
        :type: list[PartStudiosGetEdgesResponse200Edges]
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this PartStudiosGetEdgesResponse200Parts.  # noqa: E501

        ID of a part  # noqa: E501

        :return: The id of this PartStudiosGetEdgesResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartStudiosGetEdgesResponse200Parts.

        ID of a part  # noqa: E501

        :param id: The id of this PartStudiosGetEdgesResponse200Parts.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, PartStudiosGetEdgesResponse200Parts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
