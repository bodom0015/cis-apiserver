from swagger_server.models.simulation import Simulation
from contextlib import redirect_stdout
import io
import os
# import subprocess
import json

from flask import jsonify

from cis_interface import runner

# from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
# config.load_incluster_config()

#
# This file holds the server implementation called 
# into by the generated Swagger REST API
#

# Handler for GET /models
def GET_models_handler():
    basepath = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    datapath = os.path.join(basepath, 'data')
    f = open(os.path.join(datapath, 'models.json'), encoding='utf-8');
    data = json.load(f)
    return jsonify(data)

# Handler for GET /simulations
def GET_simulations_handler():
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
        

    # Run "cisrun" with the given models and capture stdout/stderr
    f = io.StringIO()
    try: 
        with redirect_stdout(f):
            runner.get_runner(yaml_paths).run()
    except e:
        print('error: ' + e)
    return f.getvalue()
        
    # TODO: Set model parameters somehow
    # FIXME: Writing parameters to files on disk doesn't allow for 2+ users
    
    
    # Experiment: Kubernetes Python Client
    #v1 = client.CoreV1Api()
    #print("Listing pods with their IPs:")
    #ret = v1.list_pod_for_all_namespaces(watch=False)
    #for i in ret.items:
    #    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    
    # Experiment: Raw Docker
    # subprocess.check_output(['docker', 'run', '-it', '--rm', '-e', 'RABBIT_NAMESPACE=apiserver', '-e', 'RABBIT_HOST=10.0.0.214', '-e', 'YAML_FILES=' + str(yaml_paths), 'bodom0015/cis_interface'])

    #return 'did some magic!'
