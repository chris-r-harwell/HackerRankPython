#!/bin/bash

set -e
set -u
set -o pipefail

n=findThePercentage
f=$(mktemp)
./$n.py < $n.in > $f

set +e
diff $f $n.out
RC=$?
set -e
if [[ $RC -eq 0 ]] ; then
	echo PASS
else
	echo FAIL
	cat $f
fi

rm -f $f
