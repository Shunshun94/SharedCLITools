#!/bin/bash

for LINE in `find | grep _raw.html`
do
  staticrypt $LINE consensus -o ${LINE%_raw.html}.html
done
