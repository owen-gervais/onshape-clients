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

from onshape_client.models.part_studios_eval_feature_script_response200_notices import PartStudiosEvalFeatureScriptResponse200Notices  # noqa: F401,E501


class PartStudiosEvalFeatureScriptResponse200(object):
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
        'notices': 'list[PartStudiosEvalFeatureScriptResponse200Notices]',
        'serialization_version': 'str',
        'console': 'str',
        'result': 'object',
        'source_microversion': 'str'
    }

    attribute_map = {
        'notices': 'notices',
        'serialization_version': 'serializationVersion',
        'console': 'console',
        'result': 'result',
        'source_microversion': 'sourceMicroversion'
    }

    def __init__(self, notices=None, serialization_version=None, console=None, result=None, source_microversion=None):  # noqa: E501
        """PartStudiosEvalFeatureScriptResponse200 - a model defined in Swagger"""  # noqa: E501

        self._notices = None
        self._serialization_version = None
        self._console = None
        self._result = None
        self._source_microversion = None
        self.discriminator = None

        if notices is not None:
            self.notices = notices
        if serialization_version is not None:
            self.serialization_version = serialization_version
        if console is not None:
            self.console = console
        if result is not None:
            self.result = result
        if source_microversion is not None:
            self.source_microversion = source_microversion

    @property
    def notices(self):
        """Gets the notices of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501

        A list of notices regarding the execution  # noqa: E501

        :return: The notices of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :rtype: list[PartStudiosEvalFeatureScriptResponse200Notices]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this PartStudiosEvalFeatureScriptResponse200.

        A list of notices regarding the execution  # noqa: E501

        :param notices: The notices of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :type: list[PartStudiosEvalFeatureScriptResponse200Notices]
        """

        self._notices = notices

    @property
    def serialization_version(self):
        """Gets the serialization_version of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501

        The version of the serialization protocol for the response  # noqa: E501

        :return: The serialization_version of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this PartStudiosEvalFeatureScriptResponse200.

        The version of the serialization protocol for the response  # noqa: E501

        :param serialization_version: The serialization_version of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def console(self):
        """Gets the console of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501

        An informational message  # noqa: E501

        :return: The console of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :rtype: str
        """
        return self._console

    @console.setter
    def console(self, console):
        """Sets the console of this PartStudiosEvalFeatureScriptResponse200.

        An informational message  # noqa: E501

        :param console: The console of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :type: str
        """

        self._console = console

    @property
    def result(self):
        """Gets the result of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501

        the result of the function execution  # noqa: E501

        :return: The result of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PartStudiosEvalFeatureScriptResponse200.

        the result of the function execution  # noqa: E501

        :param result: The result of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def source_microversion(self):
        """Gets the source_microversion of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501

        The document microversion from which the feature was extracted  # noqa: E501

        :return: The source_microversion of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this PartStudiosEvalFeatureScriptResponse200.

        The document microversion from which the feature was extracted  # noqa: E501

        :param source_microversion: The source_microversion of this PartStudiosEvalFeatureScriptResponse200.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

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
        if not isinstance(other, PartStudiosEvalFeatureScriptResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
