from parametric_simulation import run_one_parameter_parametric
import numpy as np
eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
parameter_key = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient']
parameter_vals = np.arange(0.25, 0.75, 0.02) 
output_dir = './para_res'
run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals)