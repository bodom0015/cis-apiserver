import connexion
import six

from swagger_server.models.model import Model  # noqa: E501
from swagger_server import util

from .. import endpoints

def get_models():  # noqa: E501
    """Retrieve a list of all available models in the system

     # noqa: E501


    :rtype: List[Model]
    """
    return endpoints.GET_models_handler()
