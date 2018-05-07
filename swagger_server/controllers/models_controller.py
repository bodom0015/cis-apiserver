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


def post_models(body):  # noqa: E501
    """Creates a new model in the system catalog

     # noqa: E501

    :param body: A new model to add to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return endpoints.POST_models_handler(body)
