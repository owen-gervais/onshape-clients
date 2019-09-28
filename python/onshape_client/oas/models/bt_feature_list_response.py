# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.104
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTFeatureListResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'feature_states': 'dict(str, BTFeatureState)',
        'features': 'list[BTMFeature]',
        'imports': 'list[BTMImport]',
        'default_features': 'list[BTMFeature]',
        'is_complete': 'bool',
        'rollback_index': 'int',
        'source_microversion': 'str',
        'reject_microversion_skew': 'bool',
        'library_version': 'int',
        'microversion_skew': 'bool',
        'serialization_version': 'str'
    }

    attribute_map = {
        'feature_states': 'featureStates',
        'features': 'features',
        'imports': 'imports',
        'default_features': 'defaultFeatures',
        'is_complete': 'isComplete',
        'rollback_index': 'rollbackIndex',
        'source_microversion': 'sourceMicroversion',
        'reject_microversion_skew': 'rejectMicroversionSkew',
        'library_version': 'libraryVersion',
        'microversion_skew': 'microversionSkew',
        'serialization_version': 'serializationVersion'
    }

    def __init__(self, feature_states=None, features=None, imports=None, default_features=None, is_complete=None, rollback_index=None, source_microversion=None, reject_microversion_skew=None, library_version=None, microversion_skew=None, serialization_version=None):  # noqa: E501
        """BTFeatureListResponse - a model defined in OpenAPI"""  # noqa: E501

        self._feature_states = None
        self._features = None
        self._imports = None
        self._default_features = None
        self._is_complete = None
        self._rollback_index = None
        self._source_microversion = None
        self._reject_microversion_skew = None
        self._library_version = None
        self._microversion_skew = None
        self._serialization_version = None
        self.discriminator = None

        if feature_states is not None:
            self.feature_states = feature_states
        if features is not None:
            self.features = features
        if imports is not None:
            self.imports = imports
        if default_features is not None:
            self.default_features = default_features
        if is_complete is not None:
            self.is_complete = is_complete
        if rollback_index is not None:
            self.rollback_index = rollback_index
        if source_microversion is not None:
            self.source_microversion = source_microversion
        if reject_microversion_skew is not None:
            self.reject_microversion_skew = reject_microversion_skew
        if library_version is not None:
            self.library_version = library_version
        if microversion_skew is not None:
            self.microversion_skew = microversion_skew
        if serialization_version is not None:
            self.serialization_version = serialization_version

    @property
    def feature_states(self):
        """Gets the feature_states of this BTFeatureListResponse.  # noqa: E501


        :return: The feature_states of this BTFeatureListResponse.  # noqa: E501
        :rtype: dict(str, BTFeatureState)
        """
        return self._feature_states

    @feature_states.setter
    def feature_states(self, feature_states):
        """Sets the feature_states of this BTFeatureListResponse.


        :param feature_states: The feature_states of this BTFeatureListResponse.  # noqa: E501
        :type: dict(str, BTFeatureState)
        """

        self._feature_states = feature_states

    @property
    def features(self):
        """Gets the features of this BTFeatureListResponse.  # noqa: E501


        :return: The features of this BTFeatureListResponse.  # noqa: E501
        :rtype: list[BTMFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BTFeatureListResponse.


        :param features: The features of this BTFeatureListResponse.  # noqa: E501
        :type: list[BTMFeature]
        """

        self._features = features

    @property
    def imports(self):
        """Gets the imports of this BTFeatureListResponse.  # noqa: E501


        :return: The imports of this BTFeatureListResponse.  # noqa: E501
        :rtype: list[BTMImport]
        """
        return self._imports

    @imports.setter
    def imports(self, imports):
        """Sets the imports of this BTFeatureListResponse.


        :param imports: The imports of this BTFeatureListResponse.  # noqa: E501
        :type: list[BTMImport]
        """

        self._imports = imports

    @property
    def default_features(self):
        """Gets the default_features of this BTFeatureListResponse.  # noqa: E501


        :return: The default_features of this BTFeatureListResponse.  # noqa: E501
        :rtype: list[BTMFeature]
        """
        return self._default_features

    @default_features.setter
    def default_features(self, default_features):
        """Sets the default_features of this BTFeatureListResponse.


        :param default_features: The default_features of this BTFeatureListResponse.  # noqa: E501
        :type: list[BTMFeature]
        """

        self._default_features = default_features

    @property
    def is_complete(self):
        """Gets the is_complete of this BTFeatureListResponse.  # noqa: E501


        :return: The is_complete of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this BTFeatureListResponse.


        :param is_complete: The is_complete of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

    @property
    def rollback_index(self):
        """Gets the rollback_index of this BTFeatureListResponse.  # noqa: E501


        :return: The rollback_index of this BTFeatureListResponse.  # noqa: E501
        :rtype: int
        """
        return self._rollback_index

    @rollback_index.setter
    def rollback_index(self, rollback_index):
        """Sets the rollback_index of this BTFeatureListResponse.


        :param rollback_index: The rollback_index of this BTFeatureListResponse.  # noqa: E501
        :type: int
        """

        self._rollback_index = rollback_index

    @property
    def source_microversion(self):
        """Gets the source_microversion of this BTFeatureListResponse.  # noqa: E501


        :return: The source_microversion of this BTFeatureListResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this BTFeatureListResponse.


        :param source_microversion: The source_microversion of this BTFeatureListResponse.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

    @property
    def reject_microversion_skew(self):
        """Gets the reject_microversion_skew of this BTFeatureListResponse.  # noqa: E501


        :return: The reject_microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._reject_microversion_skew

    @reject_microversion_skew.setter
    def reject_microversion_skew(self, reject_microversion_skew):
        """Sets the reject_microversion_skew of this BTFeatureListResponse.


        :param reject_microversion_skew: The reject_microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._reject_microversion_skew = reject_microversion_skew

    @property
    def library_version(self):
        """Gets the library_version of this BTFeatureListResponse.  # noqa: E501


        :return: The library_version of this BTFeatureListResponse.  # noqa: E501
        :rtype: int
        """
        return self._library_version

    @library_version.setter
    def library_version(self, library_version):
        """Sets the library_version of this BTFeatureListResponse.


        :param library_version: The library_version of this BTFeatureListResponse.  # noqa: E501
        :type: int
        """

        self._library_version = library_version

    @property
    def microversion_skew(self):
        """Gets the microversion_skew of this BTFeatureListResponse.  # noqa: E501


        :return: The microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._microversion_skew

    @microversion_skew.setter
    def microversion_skew(self, microversion_skew):
        """Sets the microversion_skew of this BTFeatureListResponse.


        :param microversion_skew: The microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._microversion_skew = microversion_skew

    @property
    def serialization_version(self):
        """Gets the serialization_version of this BTFeatureListResponse.  # noqa: E501


        :return: The serialization_version of this BTFeatureListResponse.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this BTFeatureListResponse.


        :param serialization_version: The serialization_version of this BTFeatureListResponse.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, BTFeatureListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other