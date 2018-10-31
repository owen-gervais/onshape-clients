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

from onshape_client.models.release_management_get_release_package_response200_workflow_state import ReleaseManagementGetReleasePackageResponse200WorkflowState  # noqa: F401,E501


class ReleaseManagementGetReleasePackageResponse200Workflow(object):
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
        'state': 'ReleaseManagementGetReleasePackageResponse200WorkflowState'
    }

    attribute_map = {
        'state': 'state'
    }

    def __init__(self, state=None):  # noqa: E501
        """ReleaseManagementGetReleasePackageResponse200Workflow - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self.discriminator = None

        if state is not None:
            self.state = state

    @property
    def state(self):
        """Gets the state of this ReleaseManagementGetReleasePackageResponse200Workflow.  # noqa: E501


        :return: The state of this ReleaseManagementGetReleasePackageResponse200Workflow.  # noqa: E501
        :rtype: ReleaseManagementGetReleasePackageResponse200WorkflowState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ReleaseManagementGetReleasePackageResponse200Workflow.


        :param state: The state of this ReleaseManagementGetReleasePackageResponse200Workflow.  # noqa: E501
        :type: ReleaseManagementGetReleasePackageResponse200WorkflowState
        """

        self._state = state

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
        if not isinstance(other, ReleaseManagementGetReleasePackageResponse200Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
