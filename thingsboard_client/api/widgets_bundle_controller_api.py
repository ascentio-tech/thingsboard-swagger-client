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


class WidgetsBundleControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_widgets_bundle_using_delete(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """deleteWidgetsBundle  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_widgets_bundle_using_delete(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: widgetsBundleId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_widgets_bundle_using_delete_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_widgets_bundle_using_delete_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
            return data

    def delete_widgets_bundle_using_delete_with_http_info(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """deleteWidgetsBundle  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_widgets_bundle_using_delete_with_http_info(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: widgetsBundleId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['widgets_bundle_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_widgets_bundle_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'widgets_bundle_id' is set
        if ('widgets_bundle_id' not in params or
                params['widgets_bundle_id'] is None):
            raise ValueError("Missing the required parameter `widgets_bundle_id` when calling `delete_widgets_bundle_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'widgets_bundle_id' in params:
            path_params['widgetsBundleId'] = params['widgets_bundle_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetsBundle/{widgetsBundleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widgets_bundle_by_id_using_get(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """getWidgetsBundleById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundle_by_id_using_get(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: widgetsBundleId (required)
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widgets_bundle_by_id_using_get_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widgets_bundle_by_id_using_get_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
            return data

    def get_widgets_bundle_by_id_using_get_with_http_info(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """getWidgetsBundleById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundle_by_id_using_get_with_http_info(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: widgetsBundleId (required)
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['widgets_bundle_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widgets_bundle_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'widgets_bundle_id' is set
        if ('widgets_bundle_id' not in params or
                params['widgets_bundle_id'] is None):
            raise ValueError("Missing the required parameter `widgets_bundle_id` when calling `get_widgets_bundle_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'widgets_bundle_id' in params:
            path_params['widgetsBundleId'] = params['widgets_bundle_id']  # noqa: E501

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
            '/api/widgetsBundle/{widgetsBundleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetsBundle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widgets_bundles_using_get1(self, limit, **kwargs):  # noqa: E501
        """getWidgetsBundles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundles_using_get1(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataWidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widgets_bundles_using_get1_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widgets_bundles_using_get1_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def get_widgets_bundles_using_get1_with_http_info(self, limit, **kwargs):  # noqa: E501
        """getWidgetsBundles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundles_using_get1_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataWidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'text_search', 'id_offset', 'text_offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widgets_bundles_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_widgets_bundles_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'id_offset' in params:
            query_params.append(('idOffset', params['id_offset']))  # noqa: E501
        if 'text_offset' in params:
            query_params.append(('textOffset', params['text_offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/api/widgetsBundles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextPageDataWidgetsBundle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_widgets_bundle_using_post(self, body, **kwargs):  # noqa: E501
        """saveWidgetsBundle  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_widgets_bundle_using_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidgetsBundle body: widgetsBundle (required)
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_widgets_bundle_using_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.save_widgets_bundle_using_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def save_widgets_bundle_using_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """saveWidgetsBundle  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_widgets_bundle_using_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidgetsBundle body: widgetsBundle (required)
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_widgets_bundle_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_widgets_bundle_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetsBundle', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetsBundle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
