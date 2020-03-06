# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.111
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401

from onshape_client.oas.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)
try:
    from onshape_client.oas.models import btm_parameter_reference2434
except ImportError:
    btm_parameter_reference2434 = sys.modules[
        'onshape_client.oas.models.btm_parameter_reference2434']
try:
    from onshape_client.oas.models import btm_parameter_reference_cad_import2016
except ImportError:
    btm_parameter_reference_cad_import2016 = sys.modules[
        'onshape_client.oas.models.btm_parameter_reference_cad_import2016']
try:
    from onshape_client.oas.models import btm_parameter_reference_image2014
except ImportError:
    btm_parameter_reference_image2014 = sys.modules[
        'onshape_client.oas.models.btm_parameter_reference_image2014']
try:
    from onshape_client.oas.models import btm_parameter_reference_json790
except ImportError:
    btm_parameter_reference_json790 = sys.modules[
        'onshape_client.oas.models.btm_parameter_reference_json790']
try:
    from onshape_client.oas.models import btm_parameter_reference_table917
except ImportError:
    btm_parameter_reference_table917 = sys.modules[
        'onshape_client.oas.models.btm_parameter_reference_table917']


class BTMParameterReferenceBlob3281(ModelComposed):
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
    }

    validations = {
    }

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
            'bt_type': (str,),  # noqa: E501
            'import_microversion': (str,),  # noqa: E501
            'node_id': (str,),  # noqa: E501
            'parameter_id': (str,),  # noqa: E501
            'element_id': (str,),  # noqa: E501
            'feature_script_type': (str,),  # noqa: E501
            'namespace': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return {
            'bt_type': {
                'BTMParameterReferenceJSON-790': btm_parameter_reference_json790.BTMParameterReferenceJSON790,
                'BTMParameterReferenceTable-917': btm_parameter_reference_table917.BTMParameterReferenceTable917,
                'BTMParameterReferenceCADImport-2016': btm_parameter_reference_cad_import2016.BTMParameterReferenceCADImport2016,
                'BTMParameterReferenceImage-2014': btm_parameter_reference_image2014.BTMParameterReferenceImage2014,
            },
        }

    attribute_map = {
        'bt_type': 'btType',  # noqa: E501
        'import_microversion': 'importMicroversion',  # noqa: E501
        'node_id': 'nodeId',  # noqa: E501
        'parameter_id': 'parameterId',  # noqa: E501
        'element_id': 'elementId',  # noqa: E501
        'feature_script_type': 'featureScriptType',  # noqa: E501
        'namespace': 'namespace',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """btm_parameter_reference_blob3281.BTMParameterReferenceBlob3281 - a model defined in OpenAPI


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
            bt_type (str): [optional]  # noqa: E501
            import_microversion (str): [optional]  # noqa: E501
            node_id (str): [optional]  # noqa: E501
            parameter_id (str): [optional]  # noqa: E501
            element_id (str): [optional]  # noqa: E501
            feature_script_type (str): [optional]  # noqa: E501
            namespace (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_from_server': _from_server,
            '_configuration': _configuration,
        }
        model_args = {
        }
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)

    @staticmethod
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
          'anyOf': [
          ],
          'allOf': [
              btm_parameter_reference2434.BTMParameterReference2434,
          ],
          'oneOf': [
          ],
        }

    @classmethod
    def get_discriminator_class(cls, from_server, data):
        """Returns the child class specified by the discriminator"""
        discriminator = cls.discriminator()
        discr_propertyname_py = list(discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if from_server:
            class_name = data[discr_propertyname_js]
        else:
            class_name = data[discr_propertyname_py]
        class_name_to_discr_class = discriminator[discr_propertyname_py]
        return class_name_to_discr_class.get(class_name)