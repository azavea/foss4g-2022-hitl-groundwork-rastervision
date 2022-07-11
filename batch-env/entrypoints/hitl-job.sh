#!/bin/bash

set -e

ANNOTATION_PROJECT_ID=$1

function usage() {
    echo -n \
        "Usage: 
"
}

if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    python -m compoundrisk "${1}"
fi
