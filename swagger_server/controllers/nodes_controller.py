import connexion
import six

from swagger_server.models.node import Node  # noqa: E501
from swagger_server import util


def get_nodes():  # noqa: E501
    """Retrieve a list of nodes representing instances of the models of the system

     # noqa: E501


    :rtype: List[Node]
    """
    return 'do some magic!'
