#!/bin/sh

(
set -e
. ./first.txt
git clone https://github.com/openware/opendax.git && cd "$(basename "$_" .git)"
#. ./second.txt
)

if [ "$?" -ne 0 ]; then
  echo "The world is on fire!" | mail -s 'Doom is upon us' you@youremail.com
fi

