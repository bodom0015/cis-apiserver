import connexion
import six

from swagger_server.models.yaml_graph import YamlGraph  # noqa: E501
from swagger_server import util

from .. import endpoints

def post_graphs(body):  # noqa: E501
    """Formats and returns a YAML file for running the Graph in cisrun

     # noqa: E501

    :param body: A new system of models to run with cis_interface
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = YamlGraph.from_dict(connexion.request.get_json())  # noqa: E501
    return endpoints.POST_graphs_handler_v2(body)
