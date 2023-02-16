#Date of creation:2023-2-15
#Author: Yihang Fang
import json 
import copy
import os
from StaticEplusEngine import run_eplus_model, convert_json_idf
def run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
	                            parameter_key, parameter_vals, outgain_dir):
def data_sum(value, all_sum_temperature)
	value = value + "outer temperature"
	all_sum_temperature = sum(value)

res_dict = {}
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
	for parameter_val in parameter_vals:
		this_output_dir = output_dir + f'/{parameter_val}'    #+ /output_paths
		this_res_path = run_one_simulation_helper(eplus_run_path, idf_path)
		outgain_dir = outgain_dir + f'/{parameter_vals}'
		this_res_path = output_dir{parameter_key}
for parameter_val in parameter_vals():
	this_res_path = this_output_dir
	all_sum_temperature = data_sum
	sum_data = sum(data)
	epjson_path = idf_path.split('.idf')[0] +'.epJSON'
	for i in range(len(parameter_key)):
		if i < len(parameter_key) - 1:
			inner_dict = inner_dict[parameter_key[i]]
	inner_dict[parameter_key[-1]] = parameter_val

