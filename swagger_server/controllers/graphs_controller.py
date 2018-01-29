import connexion
import six

from swagger_server.models.graph import Graph  # noqa: E501
from swagger_server import util

from .. import endpoints

def post_graphs(body):  # noqa: E501
    """Formats and returns a YAML file for running the Graph in cisrun

     # noqa: E501

    :param body: A new graph of models to run
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Graph.from_dict(connexion.request.get_json())  # noqa: E501
    return endpoints.POST_graphs_handler(body)
