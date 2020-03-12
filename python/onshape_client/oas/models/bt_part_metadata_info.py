# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.111
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import sys  # noqa: F401

import six  # noqa: F401
from onshape_client.oas.model_utils import (  # noqa: F401
    ModelNormal,
    int,
    str,
)

try:
    from onshape_client.oas.models import bt_custom_property_definition_info
except ImportError:
    bt_custom_property_definition_info = sys.modules[
        "onshape_client.oas.models.bt_custom_property_definition_info"
    ]
try:
    from onshape_client.oas.models import bt_part_appearance_info
except ImportError:
    bt_part_appearance_info = sys.modules[
        "onshape_client.oas.models.bt_part_appearance_info"
    ]
try:
    from onshape_client.oas.models import bt_part_material_info
except ImportError:
    bt_part_material_info = sys.modules[
        "onshape_client.oas.models.bt_part_material_info"
    ]
try:
    from onshape_client.oas.models import bt_thumbnail_info
except ImportError:
    bt_thumbnail_info = sys.modules["onshape_client.oas.models.bt_thumbnail_info"]


class BTPartMetadataInfo(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ("state",): {
            "IN_PROGRESS": "IN_PROGRESS",
            "PENDING": "PENDING",
            "RELEASED": "RELEASED",
            "OBSOLETE": "OBSOLETE",
            "REJECTED": "REJECTED",
            "DISCARDED": "DISCARDED",
        },
    }

    validations = {}

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "appearance": (bt_part_appearance_info.BTPartAppearanceInfo,),  # noqa: E501
            "body_type": (str,),  # noqa: E501
            "configuration_id": (str,),  # noqa: E501
            "custom_properties": ({str: (str,)},),  # noqa: E501
            "custom_property_definitions": (
                {
                    str: (
                        bt_custom_property_definition_info.BTCustomPropertyDefinitionInfo,
                    )
                },
            ),  # noqa: E501
            "description": (str,),  # noqa: E501
            "element_id": (str,),  # noqa: E501
            "href": (str,),  # noqa: E501
            "id": (str,),  # noqa: E501
            "is_flattened_body": (bool,),  # noqa: E501
            "is_hidden": (bool,),  # noqa: E501
            "is_mesh": (bool,),  # noqa: E501
            "material": (bt_part_material_info.BTPartMaterialInfo,),  # noqa: E501
            "microversion_id": (str,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "ordinal": (int,),  # noqa: E501
            "part_id": (str,),  # noqa: E501
            "part_number": (str,),  # noqa: E501
            "part_query": (str,),  # noqa: E501
            "product_line": (str,),  # noqa: E501
            "project": (str,),  # noqa: E501
            "property_source_types": ({str: (int,)},),  # noqa: E501
            "referencing_configured_part_node_ids": ([str],),  # noqa: E501
            "revision": (str,),  # noqa: E501
            "state": (str,),  # noqa: E501
            "thumbnail_configuration_id": (str,),  # noqa: E501
            "thumbnail_info": (bt_thumbnail_info.BTThumbnailInfo,),  # noqa: E501
            "title1": (str,),  # noqa: E501
            "title2": (str,),  # noqa: E501
            "title3": (str,),  # noqa: E501
            "unflattened_part_id": (str,),  # noqa: E501
            "vendor": (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "appearance": "appearance",  # noqa: E501
        "body_type": "bodyType",  # noqa: E501
        "configuration_id": "configurationId",  # noqa: E501
        "custom_properties": "customProperties",  # noqa: E501
        "custom_property_definitions": "customPropertyDefinitions",  # noqa: E501
        "description": "description",  # noqa: E501
        "element_id": "elementId",  # noqa: E501
        "href": "href",  # noqa: E501
        "id": "id",  # noqa: E501
        "is_flattened_body": "isFlattenedBody",  # noqa: E501
        "is_hidden": "isHidden",  # noqa: E501
        "is_mesh": "isMesh",  # noqa: E501
        "material": "material",  # noqa: E501
        "microversion_id": "microversionId",  # noqa: E501
        "name": "name",  # noqa: E501
        "ordinal": "ordinal",  # noqa: E501
        "part_id": "partId",  # noqa: E501
        "part_number": "partNumber",  # noqa: E501
        "part_query": "partQuery",  # noqa: E501
        "product_line": "productLine",  # noqa: E501
        "project": "project",  # noqa: E501
        "property_source_types": "propertySourceTypes",  # noqa: E501
        "referencing_configured_part_node_ids": "referencingConfiguredPartNodeIds",  # noqa: E501
        "revision": "revision",  # noqa: E501
        "state": "state",  # noqa: E501
        "thumbnail_configuration_id": "thumbnailConfigurationId",  # noqa: E501
        "thumbnail_info": "thumbnailInfo",  # noqa: E501
        "title1": "title1",  # noqa: E501
        "title2": "title2",  # noqa: E501
        "title3": "title3",  # noqa: E501
        "unflattened_part_id": "unflattenedPartId",  # noqa: E501
        "vendor": "vendor",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_from_server",
            "_path_to_item",
            "_configuration",
        ]
    )

    def __init__(
        self,
        _check_type=True,
        _from_server=False,
        _path_to_item=(),
        _configuration=None,
        **kwargs
    ):  # noqa: E501
        """bt_part_metadata_info.BTPartMetadataInfo - a model defined in OpenAPI


        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            appearance (bt_part_appearance_info.BTPartAppearanceInfo): [optional]  # noqa: E501
            body_type (str): [optional]  # noqa: E501
            configuration_id (str): [optional]  # noqa: E501
            custom_properties ({str: (str,)}): [optional]  # noqa: E501
            custom_property_definitions ({str: (bt_custom_property_definition_info.BTCustomPropertyDefinitionInfo,)}): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            element_id (str): [optional]  # noqa: E501
            href (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            is_flattened_body (bool): [optional]  # noqa: E501
            is_hidden (bool): [optional]  # noqa: E501
            is_mesh (bool): [optional]  # noqa: E501
            material (bt_part_material_info.BTPartMaterialInfo): [optional]  # noqa: E501
            microversion_id (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            ordinal (int): [optional]  # noqa: E501
            part_id (str): [optional]  # noqa: E501
            part_number (str): [optional]  # noqa: E501
            part_query (str): [optional]  # noqa: E501
            product_line (str): [optional]  # noqa: E501
            project (str): [optional]  # noqa: E501
            property_source_types ({str: (int,)}): [optional]  # noqa: E501
            referencing_configured_part_node_ids ([str]): [optional]  # noqa: E501
            revision (str): [optional]  # noqa: E501
            state (str): [optional]  # noqa: E501
            thumbnail_configuration_id (str): [optional]  # noqa: E501
            thumbnail_info (bt_thumbnail_info.BTThumbnailInfo): [optional]  # noqa: E501
            title1 (str): [optional]  # noqa: E501
            title2 (str): [optional]  # noqa: E501
            title3 (str): [optional]  # noqa: E501
            unflattened_part_id (str): [optional]  # noqa: E501
            vendor (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)
