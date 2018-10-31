# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from onshape_client.api_client import ApiClient


class DrawingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_translation(self, wv_char, did, wv, eid, **kwargs):  # noqa: E501
        """Create Drawing Translation  # noqa: E501

        Create an element translation. The translation may be incomplete at the time that the call                 completes. If the requestState is ACTIVE, the translation can be polled until the state becomes                 either DONE or FAILED. Alternatively, a webhook callback can be registered for notification of                 translation completion. (Requires Write scope if storeInDocument is true)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_translation(wv_char, did, wv, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wv_char: One of w or v corresponding to whether a workspace or version was entered. (required)
        :param str did: Document ID (required)
        :param str wv: Workspace (w) or Version (v) ID (required)
        :param str eid: Element ID (required)
        :param DrawingsCreateTranslationBody body: The JSON request body.
        :return: DrawingsCreateTranslationResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_translation_with_http_info(wv_char, did, wv, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.create_translation_with_http_info(wv_char, did, wv, eid, **kwargs)  # noqa: E501
            return data

    def create_translation_with_http_info(self, wv_char, did, wv, eid, **kwargs):  # noqa: E501
        """Create Drawing Translation  # noqa: E501

        Create an element translation. The translation may be incomplete at the time that the call                 completes. If the requestState is ACTIVE, the translation can be polled until the state becomes                 either DONE or FAILED. Alternatively, a webhook callback can be registered for notification of                 translation completion. (Requires Write scope if storeInDocument is true)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_translation_with_http_info(wv_char, did, wv, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wv_char: One of w or v corresponding to whether a workspace or version was entered. (required)
        :param str did: Document ID (required)
        :param str wv: Workspace (w) or Version (v) ID (required)
        :param str eid: Element ID (required)
        :param DrawingsCreateTranslationBody body: The JSON request body.
        :return: DrawingsCreateTranslationResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wv_char', 'did', 'wv', 'eid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_translation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wv_char' is set
        if ('wv_char' not in params or
                params['wv_char'] is None):
            raise ValueError("Missing the required parameter `wv_char` when calling `create_translation`")  # noqa: E501
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `create_translation`")  # noqa: E501
        # verify the required parameter 'wv' is set
        if ('wv' not in params or
                params['wv'] is None):
            raise ValueError("Missing the required parameter `wv` when calling `create_translation`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `create_translation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wv_char' in params:
            path_params['wv_char'] = params['wv_char']  # noqa: E501
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'wv' in params:
            path_params['wv'] = params['wv']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/drawings/d/{did}/{wv_char}/{wv}/e/{eid}/translations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingsCreateTranslationResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_translation_formats(self, did, wid, eid, **kwargs):  # noqa: E501
        """Get Translation Formats  # noqa: E501

        Returns a list of the available formats to which this Drawing can be translated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_translation_formats(did, wid, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str did: Document ID (required)
        :param str wid: Workspace ID (required)
        :param str eid: Element ID (required)
        :return: DrawingsGetTranslationFormatsResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_translation_formats_with_http_info(did, wid, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_translation_formats_with_http_info(did, wid, eid, **kwargs)  # noqa: E501
            return data

    def get_translation_formats_with_http_info(self, did, wid, eid, **kwargs):  # noqa: E501
        """Get Translation Formats  # noqa: E501

        Returns a list of the available formats to which this Drawing can be translated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_translation_formats_with_http_info(did, wid, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str did: Document ID (required)
        :param str wid: Workspace ID (required)
        :param str eid: Element ID (required)
        :return: DrawingsGetTranslationFormatsResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'wid', 'eid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_translation_formats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `get_translation_formats`")  # noqa: E501
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `get_translation_formats`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `get_translation_formats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/drawings/d/{did}/w/{wid}/e/{eid}/translationformats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingsGetTranslationFormatsResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
