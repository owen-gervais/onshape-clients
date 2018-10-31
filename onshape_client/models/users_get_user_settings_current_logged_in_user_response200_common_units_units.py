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


class UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits(object):
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
        'abbreviation': 'object',
        'unit_type': 'str',
        'value_in_base_units': 'float',
        'unit': 'str',
        'unit_name': 'str'
    }

    attribute_map = {
        'abbreviation': 'abbreviation',
        'unit_type': 'unitType',
        'value_in_base_units': 'valueInBaseUnits',
        'unit': 'unit',
        'unit_name': 'unitName'
    }

    def __init__(self, abbreviation=None, unit_type=None, value_in_base_units=None, unit=None, unit_name=None):  # noqa: E501
        """UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits - a model defined in Swagger"""  # noqa: E501

        self._abbreviation = None
        self._unit_type = None
        self._value_in_base_units = None
        self._unit = None
        self._unit_name = None
        self.discriminator = None

        if abbreviation is not None:
            self.abbreviation = abbreviation
        if unit_type is not None:
            self.unit_type = unit_type
        if value_in_base_units is not None:
            self.value_in_base_units = value_in_base_units
        if unit is not None:
            self.unit = unit
        if unit_name is not None:
            self.unit_name = unit_name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501

        Unit abbreviation  # noqa: E501

        :return: The abbreviation of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :rtype: object
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.

        Unit abbreviation  # noqa: E501

        :param abbreviation: The abbreviation of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :type: object
        """

        self._abbreviation = abbreviation

    @property
    def unit_type(self):
        """Gets the unit_type of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501

        Type of unit, currently LENGTH, ANGLE or MASS  # noqa: E501

        :return: The unit_type of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.

        Type of unit, currently LENGTH, ANGLE or MASS  # noqa: E501

        :param unit_type: The unit_type of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :type: str
        """

        self._unit_type = unit_type

    @property
    def value_in_base_units(self):
        """Gets the value_in_base_units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501

        Conversion factor  # noqa: E501

        :return: The value_in_base_units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :rtype: float
        """
        return self._value_in_base_units

    @value_in_base_units.setter
    def value_in_base_units(self, value_in_base_units):
        """Sets the value_in_base_units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.

        Conversion factor  # noqa: E501

        :param value_in_base_units: The value_in_base_units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :type: float
        """

        self._value_in_base_units = value_in_base_units

    @property
    def unit(self):
        """Gets the unit of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501

        Unit identifier  # noqa: E501

        :return: The unit of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.

        Unit identifier  # noqa: E501

        :param unit: The unit of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def unit_name(self):
        """Gets the unit_name of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501

        Unit name  # noqa: E501

        :return: The unit_name of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.

        Unit name  # noqa: E501

        :param unit_name: The unit_name of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

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
        if not isinstance(other, UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
