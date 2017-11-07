import connexion
from swagger_server.models.simulation import Simulation
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from .. import endpoints

def add_sim_data(body):
    """
    Add a new simulation data point
    
    :param body: Simulation data that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Simulation.from_dict(connexion.request.get_json())

    return endpoints.POST_simulation_handler(body);
