import connexion
from swagger_server.models.simulation import Simulation
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from cis_interface.config import cis_cfg, cfg_environment
from cis_interface import runner
from cis_interface.runner import CisRunner

def add_sim_data(body):
    """
    Add a new simulation data point
    
    :param body: Simulation data that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Simulation.from_dict(connexion.request.get_json())

    example_dir='/usr/local/lib/python3.6/site-packages/cis_interface/examples/hello/'

    # List of paths to yaml files specifying the models that should be run
    # TODO: Pull this from POST body instead?
    files = body['files']

    for path in files:
        if not path.startswith('example_'):
            path = example_dir + '/' + path
        yaml_paths.append(path)

    cisRunner = runner.get_runner(yaml_paths)

    cisRunner.run()

    return 'did some magic!'
