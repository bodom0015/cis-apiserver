from swagger_server.models.simulation import Simulation

from cis_interface import runner

#
# This file holds the server implementation called 
# into by the generated Swagger REST API
#

# Handler for GET /simulations
def GET_simulations_handler(body):
    return 'a-yup'

# Handler for POST /simulations
def POST_simulations_handler(body):
    examples_dir='/usr/local/lib/python3.6/site-packages/cis_interface/examples'
    models_dir='./Models_AMQP'

    # List of paths to yaml files specifying the models that should be run
    # TODO: Pull this from POST body instead?
    # FIXME: temporary hack
    models = body.models
    yaml_paths = []
    
    print(models)

    for model in models:
        name = model.name
        path = model.path

        # Temporary handling for running the examples
        if name.startswith('example:'):
            path = examples_dir + '/' + path + '.yml'
        else:
            path = models_dir + '/' + path + '.yml'
        yaml_paths.append(path)
        
    # TODO: Set model parameters somehow
    # FIXME: Writing parameters to files on disk doesn't allow for 2+ users

    # Run "cisrun" with the given models
    runner.get_runner(yaml_paths).run()

    return 'did some magic!'
