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

from onshape_client.models.documents_share_document_response200_entries_1 import DocumentsShareDocumentResponse200Entries1  # noqa: F401,E501
from onshape_client.models.documents_share_document_response200_inherited_acls import DocumentsShareDocumentResponse200InheritedAcls  # noqa: F401,E501
from onshape_client.models.documents_share_document_response200_owner_1 import DocumentsShareDocumentResponse200Owner1  # noqa: F401,E501


class DocumentsShareDocumentResponse200(object):
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
        'object_id': 'str',
        'is_public': 'bool',
        'shared_with_support': 'bool',
        'visibility': 'str',
        'inherited_acls': 'list[DocumentsShareDocumentResponse200InheritedAcls]',
        'is_admin': 'bool',
        'href': 'str',
        'entries': 'list[DocumentsShareDocumentResponse200Entries1]',
        'owner': 'DocumentsShareDocumentResponse200Owner1',
        'id': 'str',
        'object_type': 'float'
    }

    attribute_map = {
        'name': 'name',
        'object_id': 'objectId',
        'is_public': 'isPublic',
        'shared_with_support': 'sharedWithSupport',
        'visibility': 'visibility',
        'inherited_acls': 'inheritedAcls',
        'is_admin': 'isAdmin',
        'href': 'href',
        'entries': 'entries',
        'owner': 'owner',
        'id': 'id',
        'object_type': 'objectType'
    }

    def __init__(self, name=None, object_id=None, is_public=None, shared_with_support=None, visibility=None, inherited_acls=None, is_admin=None, href=None, entries=None, owner=None, id=None, object_type=None):  # noqa: E501
        """DocumentsShareDocumentResponse200 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._object_id = None
        self._is_public = None
        self._shared_with_support = None
        self._visibility = None
        self._inherited_acls = None
        self._is_admin = None
        self._href = None
        self._entries = None
        self._owner = None
        self._id = None
        self._object_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if object_id is not None:
            self.object_id = object_id
        if is_public is not None:
            self.is_public = is_public
        if shared_with_support is not None:
            self.shared_with_support = shared_with_support
        if visibility is not None:
            self.visibility = visibility
        if inherited_acls is not None:
            self.inherited_acls = inherited_acls
        if is_admin is not None:
            self.is_admin = is_admin
        if href is not None:
            self.href = href
        if entries is not None:
            self.entries = entries
        if owner is not None:
            self.owner = owner
        if id is not None:
            self.id = id
        if object_type is not None:
            self.object_type = object_type

    @property
    def name(self):
        """Gets the name of this DocumentsShareDocumentResponse200.  # noqa: E501

        Not used  # noqa: E501

        :return: The name of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentsShareDocumentResponse200.

        Not used  # noqa: E501

        :param name: The name of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object_id(self):
        """Gets the object_id of this DocumentsShareDocumentResponse200.  # noqa: E501

        The ID of the object  # noqa: E501

        :return: The object_id of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this DocumentsShareDocumentResponse200.

        The ID of the object  # noqa: E501

        :param object_id: The object_id of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def is_public(self):
        """Gets the is_public of this DocumentsShareDocumentResponse200.  # noqa: E501

        True if the object is public  # noqa: E501

        :return: The is_public of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this DocumentsShareDocumentResponse200.

        True if the object is public  # noqa: E501

        :param is_public: The is_public of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def shared_with_support(self):
        """Gets the shared_with_support of this DocumentsShareDocumentResponse200.  # noqa: E501

        True if the object is shared with support  # noqa: E501

        :return: The shared_with_support of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._shared_with_support

    @shared_with_support.setter
    def shared_with_support(self, shared_with_support):
        """Sets the shared_with_support of this DocumentsShareDocumentResponse200.

        True if the object is shared with support  # noqa: E501

        :param shared_with_support: The shared_with_support of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: bool
        """

        self._shared_with_support = shared_with_support

    @property
    def visibility(self):
        """Gets the visibility of this DocumentsShareDocumentResponse200.  # noqa: E501

        A description string indicating whether the object is public or private  # noqa: E501

        :return: The visibility of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this DocumentsShareDocumentResponse200.

        A description string indicating whether the object is public or private  # noqa: E501

        :param visibility: The visibility of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def inherited_acls(self):
        """Gets the inherited_acls of this DocumentsShareDocumentResponse200.  # noqa: E501

        A list of parent objects from which this object inherits access       rights. Parent objects are currently always folders  # noqa: E501

        :return: The inherited_acls of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: list[DocumentsShareDocumentResponse200InheritedAcls]
        """
        return self._inherited_acls

    @inherited_acls.setter
    def inherited_acls(self, inherited_acls):
        """Sets the inherited_acls of this DocumentsShareDocumentResponse200.

        A list of parent objects from which this object inherits access       rights. Parent objects are currently always folders  # noqa: E501

        :param inherited_acls: The inherited_acls of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: list[DocumentsShareDocumentResponse200InheritedAcls]
        """

        self._inherited_acls = inherited_acls

    @property
    def is_admin(self):
        """Gets the is_admin of this DocumentsShareDocumentResponse200.  # noqa: E501

        True if the requesting user has RESHARE privileges on the object.      If set to false, entries that do not relate to the caller are removed from the output.  # noqa: E501

        :return: The is_admin of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this DocumentsShareDocumentResponse200.

        True if the requesting user has RESHARE privileges on the object.      If set to false, entries that do not relate to the caller are removed from the output.  # noqa: E501

        :param is_admin: The is_admin of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def href(self):
        """Gets the href of this DocumentsShareDocumentResponse200.  # noqa: E501

        A URL referencing the API to get this structure  # noqa: E501

        :return: The href of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DocumentsShareDocumentResponse200.

        A URL referencing the API to get this structure  # noqa: E501

        :param href: The href of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def entries(self):
        """Gets the entries of this DocumentsShareDocumentResponse200.  # noqa: E501

        The current share entries for the object. Each share entry indicates      an entity that the object is shared with and the permissions granted to the entity  # noqa: E501

        :return: The entries of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: list[DocumentsShareDocumentResponse200Entries1]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this DocumentsShareDocumentResponse200.

        The current share entries for the object. Each share entry indicates      an entity that the object is shared with and the permissions granted to the entity  # noqa: E501

        :param entries: The entries of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: list[DocumentsShareDocumentResponse200Entries1]
        """

        self._entries = entries

    @property
    def owner(self):
        """Gets the owner of this DocumentsShareDocumentResponse200.  # noqa: E501


        :return: The owner of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: DocumentsShareDocumentResponse200Owner1
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DocumentsShareDocumentResponse200.


        :param owner: The owner of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: DocumentsShareDocumentResponse200Owner1
        """

        self._owner = owner

    @property
    def id(self):
        """Gets the id of this DocumentsShareDocumentResponse200.  # noqa: E501

        Not used  # noqa: E501

        :return: The id of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsShareDocumentResponse200.

        Not used  # noqa: E501

        :param id: The id of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object_type(self):
        """Gets the object_type of this DocumentsShareDocumentResponse200.  # noqa: E501

        Set to the value 1, indicating the the objectId indicates a document,       or 4, indicating that the objectId indicates a folder  # noqa: E501

        :return: The object_type of this DocumentsShareDocumentResponse200.  # noqa: E501
        :rtype: float
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this DocumentsShareDocumentResponse200.

        Set to the value 1, indicating the the objectId indicates a document,       or 4, indicating that the objectId indicates a folder  # noqa: E501

        :param object_type: The object_type of this DocumentsShareDocumentResponse200.  # noqa: E501
        :type: float
        """

        self._object_type = object_type

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
        if not isinstance(other, DocumentsShareDocumentResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
