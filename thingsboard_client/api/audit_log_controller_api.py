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


class AuditLogControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_audit_logs_by_customer_id_using_get(self, customer_id, limit, **kwargs):  # noqa: E501
        """getAuditLogsByCustomerId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_by_customer_id_using_get(customer_id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_logs_by_customer_id_using_get_with_http_info(customer_id, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_logs_by_customer_id_using_get_with_http_info(customer_id, limit, **kwargs)  # noqa: E501
            return data

    def get_audit_logs_by_customer_id_using_get_with_http_info(self, customer_id, limit, **kwargs):  # noqa: E501
        """getAuditLogsByCustomerId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_by_customer_id_using_get_with_http_info(customer_id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'limit', 'start_time', 'end_time', 'asc_order', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_logs_by_customer_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_audit_logs_by_customer_id_using_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_audit_logs_by_customer_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/api/audit/logs/customer/{customerId}{?startTime,endTime,ascOrder,offset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimePageDataAuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_logs_by_entity_id_using_get(self, entity_type, entity_id, limit, **kwargs):  # noqa: E501
        """getAuditLogsByEntityId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_by_entity_id_using_get(entity_type, entity_id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_logs_by_entity_id_using_get_with_http_info(entity_type, entity_id, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_logs_by_entity_id_using_get_with_http_info(entity_type, entity_id, limit, **kwargs)  # noqa: E501
            return data

    def get_audit_logs_by_entity_id_using_get_with_http_info(self, entity_type, entity_id, limit, **kwargs):  # noqa: E501
        """getAuditLogsByEntityId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_by_entity_id_using_get_with_http_info(entity_type, entity_id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'limit', 'start_time', 'end_time', 'asc_order', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_logs_by_entity_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_audit_logs_by_entity_id_using_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_audit_logs_by_entity_id_using_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_audit_logs_by_entity_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/api/audit/logs/entity/{entityType}/{entityId}{?startTime,endTime,ascOrder,offset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimePageDataAuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_logs_by_user_id_using_get(self, user_id, limit, **kwargs):  # noqa: E501
        """getAuditLogsByUserId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_by_user_id_using_get(user_id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: userId (required)
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_logs_by_user_id_using_get_with_http_info(user_id, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_logs_by_user_id_using_get_with_http_info(user_id, limit, **kwargs)  # noqa: E501
            return data

    def get_audit_logs_by_user_id_using_get_with_http_info(self, user_id, limit, **kwargs):  # noqa: E501
        """getAuditLogsByUserId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_by_user_id_using_get_with_http_info(user_id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: userId (required)
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'start_time', 'end_time', 'asc_order', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_logs_by_user_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_audit_logs_by_user_id_using_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_audit_logs_by_user_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/api/audit/logs/user/{userId}{?startTime,endTime,ascOrder,offset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimePageDataAuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_logs_using_get(self, limit, **kwargs):  # noqa: E501
        """getAuditLogs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_using_get(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_logs_using_get_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_logs_using_get_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def get_audit_logs_using_get_with_http_info(self, limit, **kwargs):  # noqa: E501
        """getAuditLogs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_logs_using_get_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'start_time', 'end_time', 'asc_order', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_logs_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_audit_logs_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/api/audit/logs{?startTime,endTime,ascOrder,offset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimePageDataAuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
