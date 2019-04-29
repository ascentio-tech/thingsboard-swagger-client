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
from api.asset_controller_api import AssetControllerApi  # noqa: E501
from thingsboard_client.rest import ApiException


class TestAssetControllerApi(unittest.TestCase):
    """AssetControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.asset_controller_api.AssetControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_asset_to_customer_using_post(self):
        """Test case for assign_asset_to_customer_using_post

        assignAssetToCustomer  # noqa: E501
        """
        pass

    def test_assign_asset_to_public_customer_using_post(self):
        """Test case for assign_asset_to_public_customer_using_post

        assignAssetToPublicCustomer  # noqa: E501
        """
        pass

    def test_delete_asset_using_delete(self):
        """Test case for delete_asset_using_delete

        deleteAsset  # noqa: E501
        """
        pass

    def test_find_by_query_using_post(self):
        """Test case for find_by_query_using_post

        findByQuery  # noqa: E501
        """
        pass

    def test_get_asset_by_id_using_get(self):
        """Test case for get_asset_by_id_using_get

        getAssetById  # noqa: E501
        """
        pass

    def test_get_asset_types_using_get(self):
        """Test case for get_asset_types_using_get

        getAssetTypes  # noqa: E501
        """
        pass

    def test_get_assets_by_ids_using_get(self):
        """Test case for get_assets_by_ids_using_get

        getAssetsByIds  # noqa: E501
        """
        pass

    def test_get_customer_assets_using_get(self):
        """Test case for get_customer_assets_using_get

        getCustomerAssets  # noqa: E501
        """
        pass

    def test_get_tenant_asset_using_get(self):
        """Test case for get_tenant_asset_using_get

        getTenantAsset  # noqa: E501
        """
        pass

    def test_get_tenant_assets_using_get(self):
        """Test case for get_tenant_assets_using_get

        getTenantAssets  # noqa: E501
        """
        pass

    def test_save_asset_using_post(self):
        """Test case for save_asset_using_post

        saveAsset  # noqa: E501
        """
        pass

    def test_unassign_asset_from_customer_using_delete(self):
        """Test case for unassign_asset_from_customer_using_delete

        unassignAssetFromCustomer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
