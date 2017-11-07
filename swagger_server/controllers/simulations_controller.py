import connexion
import six

from swagger_server.models.simulation import Simulation  # noqa: E501
from swagger_server import util

from .. import endpoints

def get_simulations():  # noqa: E501
    """Retrieve a list of all prior simulations

     # noqa: E501


    :rtype: List[Simulation]
    """
    return endpoints.GET_simulations_handler()


def post_simulations(body):  # noqa: E501
    """Create a new simulation

     # noqa: E501

    :param body: A new set of simulation models to run
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Simulation.from_dict(connexion.request.get_json())  # noqa: E501
    return endpoints.POST_simulations_handler(body)
