#!/bin/bash

const_is_var = "0"
with_size = "0"

while [ -n "$1" ]
do
case "$1" in
-rtl-type) rtl_type="$2";;
-const-is-var) const_is_var="1";;
-gen-type) gen_type="$2";;
-op-per-lvl) op_per_lvl="$2";;
-res-per-lvl) res_per_lvl="$2";;
-stages-res) stages_res="$2";;
-with-size) with_size="1";;
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

# with_size = "0" - without size
# with_size = "1" - with size

if [[ "$rtl_type" = "0"]] && [["$with_size" = "0"]] then
    rtl_00_generator_without_sizes_odn.py 
fi

if [[ "$rtl_type" = "0"]] && [["$with_size" = "1"]] then
    rtl_01_generator_with_sizes_numbers.py 
fi

if [[ "$rtl_type" = "1"]] && [["$with_size" = "0"]] then
   rtl_10_generator_without_sizes.py 
fi

if [[ "$rtl_type" = "1"]] && [["$with_size" = "1"]] then
    rtl_11_generator_with_sizes.py 
fi