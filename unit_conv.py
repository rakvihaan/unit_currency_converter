import math

#defining the units and its coresponding values in terms base units i.e. meter in case of length, sq.meter in case of area, liter in case od volume and kilogram in case of mass
dbase={'dbl':{"meter":1,"centimeter":100,"millimeter":1000,"micrometer":pow(10,6),"nanometer":pow(10,9),"kilometer":0.001,"miles":0.000621371,"yards":1.09361,"ft":3.280,"inch":39.3701,"light year":(1.057*pow(10,-16)),"micron":1000000},
	   'dba':{"sq.meter":1,"sq.km":(1*pow(10,-6)),"sq.mile":(3.861*pow(10,-7)),"sq.yard":1.19599,"sq.ft":10.7639,"sq.inch":1550,"hectares":(1*pow(10,-4)),"acres":0.000247105},
	   'dbv':{"liter":1,"milliliter":1000,"gallon(US)":0.264,"gallon(UK)":0.22,"fluid.oz":33.814,"cubic meter":0.001},
	   'dbm':{"kilogram":1,"gram":1000,"pound":2.205,"tonne":0.001,"oz":35.274,"milligram":(1*pow(10,6))},
	   'dbe':{"joules":1,"kilojoules":0.001,"calories":0.239006,"kilocalories":0.00023902452482624285618,"watt hour":0.0002777778,"electron volt":6.242*(pow(10,18))},
	   'dbp':{"pascals":1,"bar":pow(10,-5),"pound per sq.inch":0.000145038,"torr":0.0075006}}

#function to recieve units on the gui side
def get_units(db):
	return list(dbase[db].keys())

def conv_unit(fr,t,fv,db):
	val=0
	tempfr=0
	#checking if base value
	if fr=='meter' or fr=='sq.meter' or fr=='liter' or fr=='kilogram' or fr=='joules' or fr=='pascals':
		for key,value in dbase[db].items():
			if key==t:
				val=fv*value
				# val=round(val,3)
				try:
					#to format the converted value in a more readable way
					v=str(val)
					v=v.replace('e',' x 10^')
					val=v
				except:
					pass
				# print("Converted value: ",val, t)
				return val
	else:
		for key,value in dbase[db].items():
			if key==fr:
				tempfr=fv/value
		for key,value in dbase[db].items():
			if key==t:
				val=tempfr*value
				# val=round(val,3)
				# print("Converted value: ",val,t)
				try:
					v=str(val)
					v=v.replace('e',' x 10^')
					val=v
				except:
					pass
				return val
		
# #test run
# fr=input("from unit:")
# t=input("to unit:")
# fv=float(input("from value:"))
# db=input("l or a or m:")

# conv_unit(fr,t,fv,db)