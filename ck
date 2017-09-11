#!/bin/bash
set -e
set -u
set -o pipefail

function exit_error(){
    echo ERROR: $*
    exit 1
}

if [[ ! -d input ]]  ; then
    d=$(pwd)
    chal=${d##*/}
    curl -s https://www.hackerrank.com/rest/contests/master/challenges/$chal/download_testcases > test.zip
    unzip test.zip
    rm test.zip

    for i in input/* ; do
        echo $i
        fn=${i#*/}
        base=${fn%.txt}
        n=${base#input}
        out=output/output${n}.txt
        [[ -e $out ]] || exit_error "$out file not found"

        # add an eol which is often missing
        ed -s $out <<< w
        ed -s $i <<< w

        # sometimes ^M instead of proper line endings
        dos2unix $out
     done
fi



if [[ ! -e ans.py ]] ; then
    cp ../ans_template.py ans.py
    exit_error "ans.py not found, edit template"
fi
[[ -e ans.py ]] || exit_error "ans.py not found"

f=$(mktemp)
echo -n "pep8. "
set +e
pep8 ans.py > $f 2>&1
PRC=$?
if [[ $PRC -ne 0 ]]; then
    echo FAIL
    cat $f
    exit_error "fix pep8 complaints"
else
    echo PASS
    rm -f $f
fi

echo

for i in input/* ; do
    echo $i
    fn=${i#*/}
    base=${fn%.txt}
    n=${base#input}
    out=output/output${n}.txt
    [[ -e $out ]] || exit_error "$out file not found"

    echo "Test $n .."
    f=$(mktemp)
    chmod u+x ans.py
    set +e
    ./ans.py < $i > out 2> err
    RC=$?
    set -e
    if [[ $RC -ne 0 ]] ; then
        echo FAIL
        cat out
        cat err
        echo "non-zero exit $RC from ans.py"
    fi

    set +e
    diff out $out > $f
    DRC=$?
    set -e
    if [[ $DRC -ne 0 ]] ; then
        echo FAIL
        echo "output mismatch non-zero exit $DRC from diff"
        echo "compare out and $out"
        cat $f
    fi

    if [[ $DRC -eq 0 && $PRC -eq 0 ]] ; then
        echo PASS
    else
        echo FAIL
        exit 1
    fi

done
