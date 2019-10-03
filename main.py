print("Welcome to British Columbia Tax Calculator 2016!")
salary = int(input("What is your salary?"))
print("")
print("")

fed_sal = salary 
fed_tax = 0.00
fed_lay1_marg = 45282.00	#For salaries in range 11,474 to 45,282
fed_lay2_marg = 45281.00	#For salaries in range 45,282 to 90,563
fed_lay3_marg = 49825.00	#For salaries in range 90,563 to 140,388
fed_lay4_marg = 59612.00	#For salaries in range 140,388 to 200,000
fed_lay1_perc = 0.15
fed_lay2_perc = 0.205
fed_lay3_perc = 0.26
fed_lay4_perc = 0.29
fed_lay5_perc = 0.33

pro_sal = salary 
pro_tax = 0.00
pro_lay1_marg = 38210.00	#For salaries in range 11,474 to 38,210
pro_lay2_marg = 38211.00	#For salaries in range 38,210 to 76,421
pro_lay3_marg = 11320.00	#For salaries in range 76,421 to 87,741
pro_lay4_marg = 18802.00	#For salaries in range 87,741 to 106,543
pro_lay1_perc = 0.0506
pro_lay2_perc = 0.077
pro_lay3_perc = 0.105
pro_lay4_perc = 0.1229
pro_lay5_perc = 0.147

if fed_sal > fed_lay1_marg:
	fed_tax += fed_lay1_marg*fed_lay1_perc
	fed_sal -= fed_lay1_marg
	if fed_sal > fed_lay2_marg:
		fed_tax += fed_lay2_marg*fed_lay2_perc
		fed_sal -= fed_lay2_marg
		if fed_sal > fed_lay3_marg:
			fed_tax += fed_lay3_marg*fed_lay3_perc
			fed_sal -= fed_lay3_marg
			if fed_sal > fed_lay4_marg:
				fed_tax += fed_lay4_marg*fed_lay4_perc
				fed_sal -= fed_lay4_marg
				fed_tax += fed_sal*fed_lay5_perc
				print("Your federal tax is: " + str("%.2f" % fed_tax))
				print("")
			else:
				fed_tax += fed_sal*fed_lay4_perc
				print("Your federal tax is " + str("%.2f" % fed_tax))
				print("")
		else:
			fed_tax += fed_sal*fed_lay3_perc
			print("Your federal tax is: " + str("%.2f" % fed_tax))
			print("")
	else:
		fed_tax += fed_sal*fed_lay2_perc
		print("Your federal tax is: " + str("%.2f" % fed_tax))
		print("")
else:
	fed_tax += fed_sal*fed_lay1_perc
	print("Your federal tax is: " + str("%.2f" % fed_tax))
	print("")

if pro_sal > pro_lay1_marg:
	pro_tax += pro_lay1_marg*pro_lay1_perc
	pro_sal -= pro_lay1_marg
	if pro_sal > pro_lay2_marg:
		pro_tax += pro_lay2_marg*pro_lay2_perc
		pro_sal -= pro_lay2_marg
		if pro_sal > pro_lay3_marg:
			pro_tax += pro_lay3_marg*pro_lay3_perc
			pro_sal -= pro_lay3_marg
			if pro_sal > pro_lay4_marg:
				pro_tax += pro_lay4_marg*pro_lay4_perc
				pro_sal -= pro_lay4_marg
				pro_tax += pro_sal*pro_lay5_perc
				print("Your provincial tax is: " + str("%.2f" % pro_tax))
				print("")
			else:
				pro_tax += pro_sal*pro_lay4_perc
				print("Your provincial tax is " + str("%.2f" % pro_tax))
				print("")
		else:
			pro_tax += pro_sal*pro_lay3_perc
			print("Your provincial tax is: " + str("%.2f" % pro_tax))
			print("")
	else:
		pro_tax += pro_sal*pro_lay2_perc
		print("Your provincial tax is: " + str("%.2f" % pro_tax))
		print("")
else:
	pro_tax += pro_sal*pro_lay1_perc
	print("Your provincial tax is: " + str("%.2f" % pro_tax))
	print("")

total_tax = fed_tax + pro_tax
tax_sal = salary - total_tax
print("Your total tax is " + str("%.2f" % total_tax))
print("")
print("Your remaining salary is " + str("%.2f" % tax_sal))
