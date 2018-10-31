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


class AppElementsStartTransactionResponse200(object):
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
        'parent_change_id': 'str',
        'transaction_id': 'str',
        'element_id': 'str',
        'change_id': 'str'
    }

    attribute_map = {
        'parent_change_id': 'parentChangeId',
        'transaction_id': 'transactionId',
        'element_id': 'elementId',
        'change_id': 'changeId'
    }

    def __init__(self, parent_change_id=None, transaction_id=None, element_id=None, change_id=None):  # noqa: E501
        """AppElementsStartTransactionResponse200 - a model defined in Swagger"""  # noqa: E501

        self._parent_change_id = None
        self._transaction_id = None
        self._element_id = None
        self._change_id = None
        self.discriminator = None

        if parent_change_id is not None:
            self.parent_change_id = parent_change_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if element_id is not None:
            self.element_id = element_id
        if change_id is not None:
            self.change_id = change_id

    @property
    def parent_change_id(self):
        """Gets the parent_change_id of this AppElementsStartTransactionResponse200.  # noqa: E501

        The changeId of the preceding operation, which is the same as changeId  # noqa: E501

        :return: The parent_change_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :rtype: str
        """
        return self._parent_change_id

    @parent_change_id.setter
    def parent_change_id(self, parent_change_id):
        """Sets the parent_change_id of this AppElementsStartTransactionResponse200.

        The changeId of the preceding operation, which is the same as changeId  # noqa: E501

        :param parent_change_id: The parent_change_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :type: str
        """

        self._parent_change_id = parent_change_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this AppElementsStartTransactionResponse200.  # noqa: E501

        The id of the transaction that was created  # noqa: E501

        :return: The transaction_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this AppElementsStartTransactionResponse200.

        The id of the transaction that was created  # noqa: E501

        :param transaction_id: The transaction_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def element_id(self):
        """Gets the element_id of this AppElementsStartTransactionResponse200.  # noqa: E501

        The elementId of the element  # noqa: E501

        :return: The element_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this AppElementsStartTransactionResponse200.

        The elementId of the element  # noqa: E501

        :param element_id: The element_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def change_id(self):
        """Gets the change_id of this AppElementsStartTransactionResponse200.  # noqa: E501

        The changeId upon which the transaction is based  # noqa: E501

        :return: The change_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :rtype: str
        """
        return self._change_id

    @change_id.setter
    def change_id(self, change_id):
        """Sets the change_id of this AppElementsStartTransactionResponse200.

        The changeId upon which the transaction is based  # noqa: E501

        :param change_id: The change_id of this AppElementsStartTransactionResponse200.  # noqa: E501
        :type: str
        """

        self._change_id = change_id

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
        if not isinstance(other, AppElementsStartTransactionResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
