#!/bin/bash -xe
# This script was insired by astropy-benchmarks/cron.sh

MACHINE=`python3 -c "from asv.machine import Machine; print(Machine.load('~/.asv-machine.json').machine)"`

echo "asv: "`asv --version`
echo "Machine: "$MACHINE

git checkout main
git pull origin main

asv run --quick --bench Image || true
asv run --quick --bench Tabular || true
asv run --quick --bench Compression || true

python3 postprocessing.py

asv gh-pages