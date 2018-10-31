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

from onshape_client.models.documents_share_document_body_entries import DocumentsShareDocumentBodyEntries  # noqa: F401,E501


class FoldersShareFolderBody(object):
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
        'permission_set': 'list[str]',
        'folder_id': 'str',
        'message': 'str',
        'update': 'bool',
        'entries': 'list[DocumentsShareDocumentBodyEntries]'
    }

    attribute_map = {
        'permission_set': 'permissionSet',
        'folder_id': 'folderId',
        'message': 'message',
        'update': 'update',
        'entries': 'entries'
    }

    def __init__(self, permission_set=None, folder_id=None, message=None, update=None, entries=None):  # noqa: E501
        """FoldersShareFolderBody - a model defined in Swagger"""  # noqa: E501

        self._permission_set = None
        self._folder_id = None
        self._message = None
        self._update = None
        self._entries = None
        self.discriminator = None

        if permission_set is not None:
            self.permission_set = permission_set
        if folder_id is not None:
            self.folder_id = folder_id
        if message is not None:
            self.message = message
        if update is not None:
            self.update = update
        if entries is not None:
            self.entries = entries

    @property
    def permission_set(self):
        """Gets the permission_set of this FoldersShareFolderBody.  # noqa: E501

        The permissions to grant to the entities. Must not be empty. The      valid permissions are READ, WRITE, DELETE, RESHARE, COMMENT, LINK, COPY, OWNER. It is an error for a      permission set to be specified that is identical to the current permissions for an entity in the entries      list.  # noqa: E501

        :return: The permission_set of this FoldersShareFolderBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this FoldersShareFolderBody.

        The permissions to grant to the entities. Must not be empty. The      valid permissions are READ, WRITE, DELETE, RESHARE, COMMENT, LINK, COPY, OWNER. It is an error for a      permission set to be specified that is identical to the current permissions for an entity in the entries      list.  # noqa: E501

        :param permission_set: The permission_set of this FoldersShareFolderBody.  # noqa: E501
        :type: list[str]
        """

        self._permission_set = permission_set

    @property
    def folder_id(self):
        """Gets the folder_id of this FoldersShareFolderBody.  # noqa: E501

        The ID of the folder to be shared. Must match the folder ID specified in the           URL.  # noqa: E501

        :return: The folder_id of this FoldersShareFolderBody.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FoldersShareFolderBody.

        The ID of the folder to be shared. Must match the folder ID specified in the           URL.  # noqa: E501

        :param folder_id: The folder_id of this FoldersShareFolderBody.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def message(self):
        """Gets the message of this FoldersShareFolderBody.  # noqa: E501

        An optional message to include in the share email.      This message has a maximum allowed size.  # noqa: E501

        :return: The message of this FoldersShareFolderBody.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FoldersShareFolderBody.

        An optional message to include in the share email.      This message has a maximum allowed size.  # noqa: E501

        :param message: The message of this FoldersShareFolderBody.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def update(self):
        """Gets the update of this FoldersShareFolderBody.  # noqa: E501

        If true, indicates that the request is intended to be an update of existing      share permissions for the entities in the entries list.  # noqa: E501

        :return: The update of this FoldersShareFolderBody.  # noqa: E501
        :rtype: bool
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this FoldersShareFolderBody.

        If true, indicates that the request is intended to be an update of existing      share permissions for the entities in the entries list.  # noqa: E501

        :param update: The update of this FoldersShareFolderBody.  # noqa: E501
        :type: bool
        """

        self._update = update

    @property
    def entries(self):
        """Gets the entries of this FoldersShareFolderBody.  # noqa: E501

        List of target entities to share with. Must not be empty.  # noqa: E501

        :return: The entries of this FoldersShareFolderBody.  # noqa: E501
        :rtype: list[DocumentsShareDocumentBodyEntries]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this FoldersShareFolderBody.

        List of target entities to share with. Must not be empty.  # noqa: E501

        :param entries: The entries of this FoldersShareFolderBody.  # noqa: E501
        :type: list[DocumentsShareDocumentBodyEntries]
        """

        self._entries = entries

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
        if not isinstance(other, FoldersShareFolderBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
