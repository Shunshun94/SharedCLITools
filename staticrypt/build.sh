#!/bin/bash

for LINE in `find | grep _raw.html`
do
  staticrypt $LINE password -o ${LINE%_raw.html}.html
done
