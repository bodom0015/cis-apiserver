# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.simulation import Simulation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSimulationsController(BaseTestCase):
    """SimulationsController integration test stubs"""

    def test_get_simulations(self):
        """Test case for get_simulations

        Retrieve a list of all prior simulations
        """
        response = self.client.open(
            '/api/v1/simulations',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_simulations(self):
        """Test case for post_simulations

        Create a new simulation
        """
        body = Simulation()
        response = self.client.open(
            '/api/v1/simulations',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
