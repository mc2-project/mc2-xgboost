#!/usr/bin/env bash

set -e

ret=$(cat /proc/sys/kernel/randomize_va_space)
if [ $ret -ne 0 ]; then
    echo "ASLR is NOT disabled. Please disable ASLR."
    exit 1
fi

echo "Generating random arrays"
./gen_arr.sh A
./gen_arr.sh B

echo "Building"
g++ -w -O2 -fno-strict-aliasing sort_A.cc ../../include/xgboost/common/obl_primitives.h -o sort_A
g++ -w -O2 -fno-strict-aliasing sort_B.cc ../../include/xgboost/common/obl_primitives.h -o sort_B

echo "Done"
