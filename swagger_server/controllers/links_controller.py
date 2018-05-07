import connexion
import six

from swagger_server.models.link import Link  # noqa: E501
from swagger_server import util


def get_links():  # noqa: E501
    """Retrieve a list of links between the nodes of the system

     # noqa: E501


    :rtype: List[Link]
    """
    return 'do some magic!'