# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from thingsboard_client.api_client import ApiClient


class ComponentDescriptorControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_component_descriptor_by_clazz_using_get(self, component_descriptor_clazz, **kwargs):  # noqa: E501
        """getComponentDescriptorByClazz  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptor_by_clazz_using_get(component_descriptor_clazz, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_descriptor_clazz: componentDescriptorClazz (required)
        :return: ComponentDescriptor
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_descriptor_by_clazz_using_get_with_http_info(component_descriptor_clazz, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_descriptor_by_clazz_using_get_with_http_info(component_descriptor_clazz, **kwargs)  # noqa: E501
            return data

    def get_component_descriptor_by_clazz_using_get_with_http_info(self, component_descriptor_clazz, **kwargs):  # noqa: E501
        """getComponentDescriptorByClazz  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptor_by_clazz_using_get_with_http_info(component_descriptor_clazz, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_descriptor_clazz: componentDescriptorClazz (required)
        :return: ComponentDescriptor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_descriptor_clazz']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_descriptor_by_clazz_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_descriptor_clazz' is set
        if ('component_descriptor_clazz' not in params or
                params['component_descriptor_clazz'] is None):
            raise ValueError("Missing the required parameter `component_descriptor_clazz` when calling `get_component_descriptor_by_clazz_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_descriptor_clazz' in params:
            path_params['componentDescriptorClazz'] = params['component_descriptor_clazz']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/component/{componentDescriptorClazz}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComponentDescriptor',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_component_descriptors_by_type_using_get(self, component_type, **kwargs):  # noqa: E501
        """getComponentDescriptorsByType  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_type_using_get(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: componentType (required)
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_descriptors_by_type_using_get_with_http_info(component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_descriptors_by_type_using_get_with_http_info(component_type, **kwargs)  # noqa: E501
            return data

    def get_component_descriptors_by_type_using_get_with_http_info(self, component_type, **kwargs):  # noqa: E501
        """getComponentDescriptorsByType  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_type_using_get_with_http_info(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: componentType (required)
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_descriptors_by_type_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `get_component_descriptors_by_type_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_type' in params:
            path_params['componentType'] = params['component_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/components/{componentType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ComponentDescriptor]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_component_descriptors_by_types_using_get(self, component_types, **kwargs):  # noqa: E501
        """getComponentDescriptorsByTypes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_types_using_get(component_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_types: componentTypes (required)
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_descriptors_by_types_using_get_with_http_info(component_types, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_descriptors_by_types_using_get_with_http_info(component_types, **kwargs)  # noqa: E501
            return data

    def get_component_descriptors_by_types_using_get_with_http_info(self, component_types, **kwargs):  # noqa: E501
        """getComponentDescriptorsByTypes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_types_using_get_with_http_info(component_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_types: componentTypes (required)
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_types']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_descriptors_by_types_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_types' is set
        if ('component_types' not in params or
                params['component_types'] is None):
            raise ValueError("Missing the required parameter `component_types` when calling `get_component_descriptors_by_types_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'component_types' in params:
            query_params.append(('componentTypes', params['component_types']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/components', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ComponentDescriptor]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
