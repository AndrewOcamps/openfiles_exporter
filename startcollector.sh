#!/bin/bash
# Gerardo Ocampos

dir=$(echo $PWD) 

$dir/venv/bin/python $dir/collector.py </dev/null >> $dir/logexp.txt 2>&1 & echo $! > $dir/pidexp.txt
