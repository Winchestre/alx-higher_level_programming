#!/bin/bash
# CURL only methods
curl -sI "$1" | grep "Allow" | sed 's/Allow: //'
