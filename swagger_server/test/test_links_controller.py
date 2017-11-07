# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model import Model  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLinksController(BaseTestCase):
    """LinksController integration test stubs"""

    def test_get_models(self):
        """Test case for get_models

        Retrieve a list of all available models in the system
        """
        response = self.client.open(
            '/api/v1/models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
