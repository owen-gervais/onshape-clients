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


class BTMSketch(object):
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
        'namespace': 'str',
        'node_id': 'str',
        'import_microversion': 'str',
        'name': 'str',
        'suppressed': 'bool',
        'parameters': 'list[BTMParameter]',
        'feature_id': 'str',
        'feature_type': 'str',
        'sub_features': 'list[BTMFeature]',
        'return_after_subfeatures': 'bool',
        'entities': 'list[BTMSketchGeomEntity]',
        'constraints': 'list[BTMSketchConstraint]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'node_id': 'nodeId',
        'import_microversion': 'importMicroversion',
        'name': 'name',
        'suppressed': 'suppressed',
        'parameters': 'parameters',
        'feature_id': 'featureId',
        'feature_type': 'featureType',
        'sub_features': 'subFeatures',
        'return_after_subfeatures': 'returnAfterSubfeatures',
        'entities': 'entities',
        'constraints': 'constraints'
    }

    def __init__(self, namespace=None, node_id=None, import_microversion=None, name=None, suppressed=None, parameters=None, feature_id=None, feature_type=None, sub_features=None, return_after_subfeatures=None, entities=None, constraints=None):  # noqa: E501
        """BTMSketch - a model defined in OpenAPI"""  # noqa: E501

        self._namespace = None
        self._node_id = None
        self._import_microversion = None
        self._name = None
        self._suppressed = None
        self._parameters = None
        self._feature_id = None
        self._feature_type = None
        self._sub_features = None
        self._return_after_subfeatures = None
        self._entities = None
        self._constraints = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if node_id is not None:
            self.node_id = node_id
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if name is not None:
            self.name = name
        if suppressed is not None:
            self.suppressed = suppressed
        if parameters is not None:
            self.parameters = parameters
        if feature_id is not None:
            self.feature_id = feature_id
        if feature_type is not None:
            self.feature_type = feature_type
        if sub_features is not None:
            self.sub_features = sub_features
        if return_after_subfeatures is not None:
            self.return_after_subfeatures = return_after_subfeatures
        if entities is not None:
            self.entities = entities
        if constraints is not None:
            self.constraints = constraints

    @property
    def namespace(self):
        """Gets the namespace of this BTMSketch.  # noqa: E501


        :return: The namespace of this BTMSketch.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMSketch.


        :param namespace: The namespace of this BTMSketch.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def node_id(self):
        """Gets the node_id of this BTMSketch.  # noqa: E501


        :return: The node_id of this BTMSketch.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTMSketch.


        :param node_id: The node_id of this BTMSketch.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def import_microversion(self):
        """Gets the import_microversion of this BTMSketch.  # noqa: E501


        :return: The import_microversion of this BTMSketch.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this BTMSketch.


        :param import_microversion: The import_microversion of this BTMSketch.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def name(self):
        """Gets the name of this BTMSketch.  # noqa: E501


        :return: The name of this BTMSketch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTMSketch.


        :param name: The name of this BTMSketch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def suppressed(self):
        """Gets the suppressed of this BTMSketch.  # noqa: E501


        :return: The suppressed of this BTMSketch.  # noqa: E501
        :rtype: bool
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """Sets the suppressed of this BTMSketch.


        :param suppressed: The suppressed of this BTMSketch.  # noqa: E501
        :type: bool
        """

        self._suppressed = suppressed

    @property
    def parameters(self):
        """Gets the parameters of this BTMSketch.  # noqa: E501


        :return: The parameters of this BTMSketch.  # noqa: E501
        :rtype: list[BTMParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BTMSketch.


        :param parameters: The parameters of this BTMSketch.  # noqa: E501
        :type: list[BTMParameter]
        """

        self._parameters = parameters

    @property
    def feature_id(self):
        """Gets the feature_id of this BTMSketch.  # noqa: E501


        :return: The feature_id of this BTMSketch.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this BTMSketch.


        :param feature_id: The feature_id of this BTMSketch.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def feature_type(self):
        """Gets the feature_type of this BTMSketch.  # noqa: E501


        :return: The feature_type of this BTMSketch.  # noqa: E501
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this BTMSketch.


        :param feature_type: The feature_type of this BTMSketch.  # noqa: E501
        :type: str
        """

        self._feature_type = feature_type

    @property
    def sub_features(self):
        """Gets the sub_features of this BTMSketch.  # noqa: E501


        :return: The sub_features of this BTMSketch.  # noqa: E501
        :rtype: list[BTMFeature]
        """
        return self._sub_features

    @sub_features.setter
    def sub_features(self, sub_features):
        """Sets the sub_features of this BTMSketch.


        :param sub_features: The sub_features of this BTMSketch.  # noqa: E501
        :type: list[BTMFeature]
        """

        self._sub_features = sub_features

    @property
    def return_after_subfeatures(self):
        """Gets the return_after_subfeatures of this BTMSketch.  # noqa: E501


        :return: The return_after_subfeatures of this BTMSketch.  # noqa: E501
        :rtype: bool
        """
        return self._return_after_subfeatures

    @return_after_subfeatures.setter
    def return_after_subfeatures(self, return_after_subfeatures):
        """Sets the return_after_subfeatures of this BTMSketch.


        :param return_after_subfeatures: The return_after_subfeatures of this BTMSketch.  # noqa: E501
        :type: bool
        """

        self._return_after_subfeatures = return_after_subfeatures

    @property
    def entities(self):
        """Gets the entities of this BTMSketch.  # noqa: E501


        :return: The entities of this BTMSketch.  # noqa: E501
        :rtype: list[BTMSketchGeomEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this BTMSketch.


        :param entities: The entities of this BTMSketch.  # noqa: E501
        :type: list[BTMSketchGeomEntity]
        """

        self._entities = entities

    @property
    def constraints(self):
        """Gets the constraints of this BTMSketch.  # noqa: E501


        :return: The constraints of this BTMSketch.  # noqa: E501
        :rtype: list[BTMSketchConstraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this BTMSketch.


        :param constraints: The constraints of this BTMSketch.  # noqa: E501
        :type: list[BTMSketchConstraint]
        """

        self._constraints = constraints

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
        if not isinstance(other, BTMSketch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other