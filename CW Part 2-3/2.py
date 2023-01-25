# Date of the first creation: 2022-12-02
# This file is for two parameters simulation, there is a class 
# to do this work. the class can take any two arbitrary simulation
# model parameters and their ranges, and return the best set of 
# parameter values with which the simulation has the 
# highest average indoor air temperature.

class Two_simulation:
	'''a class for two parameters simulation'''

	def __init__(self, val_1, val_2 ):
		'''initializes the description parameter properties '''
		self.val_1 = val_1
		self.val_2 = val_2

	def parameter_combination(slef):
		'''pairs the parameters '''
		L_1 = val_1
		L_2 = val_2
		L_3 = [[a,b] for a in L_1 for b in L_2]#list or tuples?
		print L_3 # I don't know whether I should add this commend there or not.

	def run_two_simulation(self):
		'''bring each set of parameters into helper function and
		   get series of result csv files'''
		output_paths = {}
		os.getcwd()
		if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
		for i in range(len(L_3)):
			this_output_dir = output_dir + '/run_res_' + str(i+1)
			parameter_val = L_3[i]
			#parameter_val_1 = a in i
			#parameter_val_2 = b in i #Don't know how to express
			this_res_path = run_two_simulation_helper(eplus_run_path, idf_path, this_output_dir,
                                parameter_key_1, parameter_key_2, 
                                parameter_val_1, parameter_val_2)
		output_paths[str(parameter_val)] = this_res_path

	def get_indoor_t_average(self):
		'''caculate every csv files's indooe temperature average'''
		# use python tonread a csv file and caculate the mean of
		# column. Loop through this step for all csv files.

	def get_highest_indoor_t(self):
		'''pick up the csv that has the highest indoor t average
		   and return the two related parameters'''
		#







