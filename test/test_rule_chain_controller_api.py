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
from thingsboard_client.api.rule_chain_controller_api import RuleChainControllerApi  # noqa: E501
from thingsboard_client.rest import ApiException


class TestRuleChainControllerApi(unittest.TestCase):
    """RuleChainControllerApi unit test stubs"""

    def setUp(self):
        self.api = RuleChainControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_rule_chain_using_delete(self):
        """Test case for delete_rule_chain_using_delete

        deleteRuleChain  # noqa: E501
        """
        pass

    def test_get_latest_rule_node_debug_input_using_get(self):
        """Test case for get_latest_rule_node_debug_input_using_get

        getLatestRuleNodeDebugInput  # noqa: E501
        """
        pass

    def test_get_rule_chain_by_id_using_get(self):
        """Test case for get_rule_chain_by_id_using_get

        getRuleChainById  # noqa: E501
        """
        pass

    def test_get_rule_chain_meta_data_using_get(self):
        """Test case for get_rule_chain_meta_data_using_get

        getRuleChainMetaData  # noqa: E501
        """
        pass

    def test_get_rule_chains_using_get(self):
        """Test case for get_rule_chains_using_get

        getRuleChains  # noqa: E501
        """
        pass

    def test_save_rule_chain_meta_data_using_post(self):
        """Test case for save_rule_chain_meta_data_using_post

        saveRuleChainMetaData  # noqa: E501
        """
        pass

    def test_save_rule_chain_using_post(self):
        """Test case for save_rule_chain_using_post

        saveRuleChain  # noqa: E501
        """
        pass

    def test_set_root_rule_chain_using_post(self):
        """Test case for set_root_rule_chain_using_post

        setRootRuleChain  # noqa: E501
        """
        pass

    def test_test_script_using_post(self):
        """Test case for test_script_using_post

        testScript  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
