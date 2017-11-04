#!/bin/bash

# Build up a local config file from the passed-in environment variables
cat /usr/local/lib/python3.6/site-packages/cis_interface/defaults.cfg | sed -e "s#host:.*#host: ${RABBIT_HOST:-localhost}#" \
    -e "s#namespace:.*#namespace: ${RABBIT_NAMESPACE:-apiserver}#" \
    -e "s#user:.*#user: ${RABBIT_USER:-guest}#" \
    -e "s#password:.*#password: ${RABBIT_PASS:-guest}#" \
    -e "s#vhost:.*#vhost: ${RABBIT_VHOST}#" > ./.cis_interface.cfg

# Start our swagger API server
python -m swagger_server
