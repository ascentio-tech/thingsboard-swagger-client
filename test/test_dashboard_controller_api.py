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
from api.dashboard_controller_api import DashboardControllerApi  # noqa: E501
from thingsboard_client.rest import ApiException


class TestDashboardControllerApi(unittest.TestCase):
    """DashboardControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.dashboard_controller_api.DashboardControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_dashboard_customers_using_post(self):
        """Test case for add_dashboard_customers_using_post

        addDashboardCustomers  # noqa: E501
        """
        pass

    def test_assign_dashboard_to_customer_using_post(self):
        """Test case for assign_dashboard_to_customer_using_post

        assignDashboardToCustomer  # noqa: E501
        """
        pass

    def test_assign_dashboard_to_public_customer_using_post(self):
        """Test case for assign_dashboard_to_public_customer_using_post

        assignDashboardToPublicCustomer  # noqa: E501
        """
        pass

    def test_delete_dashboard_using_delete(self):
        """Test case for delete_dashboard_using_delete

        deleteDashboard  # noqa: E501
        """
        pass

    def test_get_customer_dashboards_using_get(self):
        """Test case for get_customer_dashboards_using_get

        getCustomerDashboards  # noqa: E501
        """
        pass

    def test_get_dashboard_by_id_using_get(self):
        """Test case for get_dashboard_by_id_using_get

        getDashboardById  # noqa: E501
        """
        pass

    def test_get_dashboard_info_by_id_using_get(self):
        """Test case for get_dashboard_info_by_id_using_get

        getDashboardInfoById  # noqa: E501
        """
        pass

    def test_get_server_time_using_get(self):
        """Test case for get_server_time_using_get

        getServerTime  # noqa: E501
        """
        pass

    def test_get_tenant_dashboards_using_get(self):
        """Test case for get_tenant_dashboards_using_get

        getTenantDashboards  # noqa: E501
        """
        pass

    def test_get_tenant_dashboards_using_get1(self):
        """Test case for get_tenant_dashboards_using_get1

        getTenantDashboards  # noqa: E501
        """
        pass

    def test_remove_dashboard_customers_using_post(self):
        """Test case for remove_dashboard_customers_using_post

        removeDashboardCustomers  # noqa: E501
        """
        pass

    def test_save_dashboard_using_post(self):
        """Test case for save_dashboard_using_post

        saveDashboard  # noqa: E501
        """
        pass

    def test_unassign_dashboard_from_customer_using_delete(self):
        """Test case for unassign_dashboard_from_customer_using_delete

        unassignDashboardFromCustomer  # noqa: E501
        """
        pass

    def test_unassign_dashboard_from_public_customer_using_delete(self):
        """Test case for unassign_dashboard_from_public_customer_using_delete

        unassignDashboardFromPublicCustomer  # noqa: E501
        """
        pass

    def test_update_dashboard_customers_using_post(self):
        """Test case for update_dashboard_customers_using_post

        updateDashboardCustomers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
