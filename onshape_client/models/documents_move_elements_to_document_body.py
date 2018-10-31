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


class DocumentsMoveElementsToDocumentBody(object):
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
        'elements': 'list[str]',
        'name': 'str',
        'tags': 'list[str]',
        'is_public': 'bool',
        'owner_type': 'float',
        'target_document_id': 'str',
        'source_document_id': 'str',
        'is_generate_unknown_messages': 'bool',
        'beta_capability_ids': 'list[str]',
        'source_workspace_id': 'str',
        'owner_id': 'str',
        'target_workspace_id': 'str'
    }

    attribute_map = {
        'elements': 'elements',
        'name': 'name',
        'tags': 'tags',
        'is_public': 'isPublic',
        'owner_type': 'ownerType',
        'target_document_id': 'targetDocumentId',
        'source_document_id': 'sourceDocumentId',
        'is_generate_unknown_messages': 'isGenerateUnknownMessages',
        'beta_capability_ids': 'betaCapabilityIds',
        'source_workspace_id': 'sourceWorkspaceId',
        'owner_id': 'ownerId',
        'target_workspace_id': 'targetWorkspaceId'
    }

    def __init__(self, elements=None, name=None, tags=None, is_public=None, owner_type=None, target_document_id=None, source_document_id=None, is_generate_unknown_messages=None, beta_capability_ids=None, source_workspace_id=None, owner_id=None, target_workspace_id=None):  # noqa: E501
        """DocumentsMoveElementsToDocumentBody - a model defined in Swagger"""  # noqa: E501

        self._elements = None
        self._name = None
        self._tags = None
        self._is_public = None
        self._owner_type = None
        self._target_document_id = None
        self._source_document_id = None
        self._is_generate_unknown_messages = None
        self._beta_capability_ids = None
        self._source_workspace_id = None
        self._owner_id = None
        self._target_workspace_id = None
        self.discriminator = None

        if elements is not None:
            self.elements = elements
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if is_public is not None:
            self.is_public = is_public
        if owner_type is not None:
            self.owner_type = owner_type
        if target_document_id is not None:
            self.target_document_id = target_document_id
        if source_document_id is not None:
            self.source_document_id = source_document_id
        if is_generate_unknown_messages is not None:
            self.is_generate_unknown_messages = is_generate_unknown_messages
        if beta_capability_ids is not None:
            self.beta_capability_ids = beta_capability_ids
        if source_workspace_id is not None:
            self.source_workspace_id = source_workspace_id
        if owner_id is not None:
            self.owner_id = owner_id
        if target_workspace_id is not None:
            self.target_workspace_id = target_workspace_id

    @property
    def elements(self):
        """Gets the elements of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        elements to move  # noqa: E501

        :return: The elements of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this DocumentsMoveElementsToDocumentBody.

        elements to move  # noqa: E501

        :param elements: The elements of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: list[str]
        """

        self._elements = elements

    @property
    def name(self):
        """Gets the name of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Document name  # noqa: E501

        :return: The name of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentsMoveElementsToDocumentBody.

        Document name  # noqa: E501

        :param name: The name of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The tags of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DocumentsMoveElementsToDocumentBody.

        Onshape internal use  # noqa: E501

        :param tags: The tags of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def is_public(self):
        """Gets the is_public of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Whether document is public  # noqa: E501

        :return: The is_public of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this DocumentsMoveElementsToDocumentBody.

        Whether document is public  # noqa: E501

        :param is_public: The is_public of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def owner_type(self):
        """Gets the owner_type of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Owner's user type, which can be: 0: user 1: company 2: Team  # noqa: E501

        :return: The owner_type of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: float
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this DocumentsMoveElementsToDocumentBody.

        Owner's user type, which can be: 0: user 1: company 2: Team  # noqa: E501

        :param owner_type: The owner_type of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: float
        """

        self._owner_type = owner_type

    @property
    def target_document_id(self):
        """Gets the target_document_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        target document Id  # noqa: E501

        :return: The target_document_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._target_document_id

    @target_document_id.setter
    def target_document_id(self, target_document_id):
        """Sets the target_document_id of this DocumentsMoveElementsToDocumentBody.

        target document Id  # noqa: E501

        :param target_document_id: The target_document_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: str
        """

        self._target_document_id = target_document_id

    @property
    def source_document_id(self):
        """Gets the source_document_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        source document Id  # noqa: E501

        :return: The source_document_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._source_document_id

    @source_document_id.setter
    def source_document_id(self, source_document_id):
        """Sets the source_document_id of this DocumentsMoveElementsToDocumentBody.

        source document Id  # noqa: E501

        :param source_document_id: The source_document_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: str
        """

        self._source_document_id = source_document_id

    @property
    def is_generate_unknown_messages(self):
        """Gets the is_generate_unknown_messages of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The is_generate_unknown_messages of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_generate_unknown_messages

    @is_generate_unknown_messages.setter
    def is_generate_unknown_messages(self, is_generate_unknown_messages):
        """Sets the is_generate_unknown_messages of this DocumentsMoveElementsToDocumentBody.

        Onshape internal use  # noqa: E501

        :param is_generate_unknown_messages: The is_generate_unknown_messages of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: bool
        """

        self._is_generate_unknown_messages = is_generate_unknown_messages

    @property
    def beta_capability_ids(self):
        """Gets the beta_capability_ids of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The beta_capability_ids of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._beta_capability_ids

    @beta_capability_ids.setter
    def beta_capability_ids(self, beta_capability_ids):
        """Sets the beta_capability_ids of this DocumentsMoveElementsToDocumentBody.

        Onshape internal use  # noqa: E501

        :param beta_capability_ids: The beta_capability_ids of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: list[str]
        """

        self._beta_capability_ids = beta_capability_ids

    @property
    def source_workspace_id(self):
        """Gets the source_workspace_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        source workspace Id  # noqa: E501

        :return: The source_workspace_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._source_workspace_id

    @source_workspace_id.setter
    def source_workspace_id(self, source_workspace_id):
        """Sets the source_workspace_id of this DocumentsMoveElementsToDocumentBody.

        source workspace Id  # noqa: E501

        :param source_workspace_id: The source_workspace_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: str
        """

        self._source_workspace_id = source_workspace_id

    @property
    def owner_id(self):
        """Gets the owner_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        Owner's user ID (default: current user)  # noqa: E501

        :return: The owner_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this DocumentsMoveElementsToDocumentBody.

        Owner's user ID (default: current user)  # noqa: E501

        :param owner_id: The owner_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def target_workspace_id(self):
        """Gets the target_workspace_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501

        target workspace Id  # noqa: E501

        :return: The target_workspace_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._target_workspace_id

    @target_workspace_id.setter
    def target_workspace_id(self, target_workspace_id):
        """Sets the target_workspace_id of this DocumentsMoveElementsToDocumentBody.

        target workspace Id  # noqa: E501

        :param target_workspace_id: The target_workspace_id of this DocumentsMoveElementsToDocumentBody.  # noqa: E501
        :type: str
        """

        self._target_workspace_id = target_workspace_id

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
        if not isinstance(other, DocumentsMoveElementsToDocumentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
