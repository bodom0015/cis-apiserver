# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.node import Node  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNodesController(BaseTestCase):
    """NodesController integration test stubs"""

    def test_get_nodes(self):
        """Test case for get_nodes

        Retrieve a list of nodes representing instances of the models of the system
        """
        response = self.client.open(
            '/api/v1/nodes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
