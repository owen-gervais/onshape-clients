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


class AssembliesGetOrCreateBillOfMaterialsElementResponse200(object):
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
        'name': 'str',
        'an': 'object',
        'microversion_id': 'str',
        'element_type': 'str',
        'type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'an': 'An',
        'microversion_id': 'microversionId',
        'element_type': 'elementType',
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, name=None, an=None, microversion_id=None, element_type=None, type=None, id=None):  # noqa: E501
        """AssembliesGetOrCreateBillOfMaterialsElementResponse200 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._an = None
        self._microversion_id = None
        self._element_type = None
        self._type = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if an is not None:
            self.an = an
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if element_type is not None:
            self.element_type = element_type
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501

        Element name  # noqa: E501

        :return: The name of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.

        Element name  # noqa: E501

        :param name: The name of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def an(self):
        """Gets the an of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501

        object containing information about the retrieved Bill Of Materials element  # noqa: E501

        :return: The an of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :rtype: object
        """
        return self._an

    @an.setter
    def an(self, an):
        """Sets the an of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.

        object containing information about the retrieved Bill Of Materials element  # noqa: E501

        :param an: The an of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :type: object
        """

        self._an = an

    @property
    def microversion_id(self):
        """Gets the microversion_id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501

        The current element microversion id  # noqa: E501

        :return: The microversion_id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.

        The current element microversion id  # noqa: E501

        :param microversion_id: The microversion_id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def element_type(self):
        """Gets the element_type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501

        Element type (will always be \"BILLOFMATERIALS\")  # noqa: E501

        :return: The element_type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.

        Element type (will always be \"BILLOFMATERIALS\")  # noqa: E501

        :param element_type: The element_type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

    @property
    def type(self):
        """Gets the type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.

        Onshape internal use  # noqa: E501

        :param type: The type of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501

        Element ID  # noqa: E501

        :return: The id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.

        Element ID  # noqa: E501

        :param id: The id of this AssembliesGetOrCreateBillOfMaterialsElementResponse200.  # noqa: E501
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
        if not isinstance(other, AssembliesGetOrCreateBillOfMaterialsElementResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
