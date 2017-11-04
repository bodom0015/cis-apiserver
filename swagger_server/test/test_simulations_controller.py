# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.simulation import Simulation
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestSimulationsController(BaseTestCase):
    """ SimulationsController integration test stubs """

    def test_add_sim_data(self):
        """
        Test case for add_sim_data

        Add a new simulation data point
        """
        body = Simulation()
        response = self.client.open('/v2/simulations',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
