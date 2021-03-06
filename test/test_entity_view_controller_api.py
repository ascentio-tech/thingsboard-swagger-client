# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import thingsboard_client
from thingsboard_client.api.entity_view_controller_api import EntityViewControllerApi  # noqa: E501
from thingsboard_client.rest import ApiException


class TestEntityViewControllerApi(unittest.TestCase):
    """EntityViewControllerApi unit test stubs"""

    def setUp(self):
        self.api = EntityViewControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_entity_view_to_customer_using_post(self):
        """Test case for assign_entity_view_to_customer_using_post

        assignEntityViewToCustomer  # noqa: E501
        """
        pass

    def test_assign_entity_view_to_public_customer_using_post(self):
        """Test case for assign_entity_view_to_public_customer_using_post

        assignEntityViewToPublicCustomer  # noqa: E501
        """
        pass

    def test_delete_entity_view_using_delete(self):
        """Test case for delete_entity_view_using_delete

        deleteEntityView  # noqa: E501
        """
        pass

    def test_find_by_query_using_post3(self):
        """Test case for find_by_query_using_post3

        findByQuery  # noqa: E501
        """
        pass

    def test_get_customer_entity_views_using_get(self):
        """Test case for get_customer_entity_views_using_get

        getCustomerEntityViews  # noqa: E501
        """
        pass

    def test_get_entity_view_by_id_using_get(self):
        """Test case for get_entity_view_by_id_using_get

        getEntityViewById  # noqa: E501
        """
        pass

    def test_get_entity_view_types_using_get(self):
        """Test case for get_entity_view_types_using_get

        getEntityViewTypes  # noqa: E501
        """
        pass

    def test_get_tenant_entity_view_using_get(self):
        """Test case for get_tenant_entity_view_using_get

        getTenantEntityView  # noqa: E501
        """
        pass

    def test_get_tenant_entity_views_using_get(self):
        """Test case for get_tenant_entity_views_using_get

        getTenantEntityViews  # noqa: E501
        """
        pass

    def test_save_entity_view_using_post(self):
        """Test case for save_entity_view_using_post

        saveEntityView  # noqa: E501
        """
        pass

    def test_unassign_entity_view_from_customer_using_delete(self):
        """Test case for unassign_entity_view_from_customer_using_delete

        unassignEntityViewFromCustomer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
