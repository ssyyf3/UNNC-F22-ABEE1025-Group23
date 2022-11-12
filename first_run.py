# Author:Yihang Fang 20412052  Dinghan Wang 
# Date:2022-10-15

# This is the first demo script to run EnergyPlus building
# energy simulation using Python

from StaticEplusEngine import run_eplus_model

eplus_exe_path = './energyplus9.5/energyplus' # Energyplus executable file path
eplus_model_path = './1ZoneUncontrolled_win_1.idf' # Energyplus model file path
res_dir = './result1' # Simulation result directory

# run eplus simulation
run_eplus_model(eplus_exe_path, eplus_model_path, res_dir)
