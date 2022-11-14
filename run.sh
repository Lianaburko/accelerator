#!/bin/bash

const_is_var = "0"

while [ -n "$1" ]
do
case "$1" in
-rtl-type) rtl_type="$2";;
-const-is-var) const_is_var="1";;
-gen-type) gen_type="$2";;
-op-per-lvl) op_per_lvl="$2";;
-res-per-lvl) res_per_lvl="$2";;
-stages-res) stages_res="$2";;
esac
shift
done

case "$gen_type" in
    0) echo "$stages_res" > temp.tmp && python3 0_code.py < temp.tmp && rm temp.tmp;;
    1) echo "$op_per_lvl $res_per_lvl $stages_res" > temp.tmp && python3 1_code.py < temp.tmp && rm temp.tmp;;  
    2) echo "$op_per_lvl $res_per_lvl $stages_res" > temp.tmp && python3 2_code.py < temp.tmp && rm temp.tmp;;  
esac

python3 graph_viziualize.py
dot -Tpng -O graph.gv

if [ "$rtl_type" = "0" && "$const_is_var" = "0"]; then
    python3 rtl_generator_with_sizes_numbers.py
