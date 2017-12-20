# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.graph import Graph  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGraphsController(BaseTestCase):
    """GraphsController integration test stubs"""

    def test_post_graphs(self):
        """Test case for post_graphs

        Formats and returns a YAML file for running the Graph in cisrun
        """
        body = Graph()
        response = self.client.open(
            '/api/v1/graphs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
