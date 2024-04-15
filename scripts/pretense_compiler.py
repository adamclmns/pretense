filesToRead = []
with open("ORDER",'r') as order:
	filesToRead = order.readlines()
	
with open("Pretense_Compiled_1.lua","w") as compiled:
	for file in filesToRead:
		with open(file,'r') as script:
			file = file.strip()
			lines = script.readlines()
			compiled.write("-----------------[[ " + file + " ]]-----------------\n")	
			compiled.writelines(lines)
			compiled.write("-----------------[[ END OF " + file + " ]]-----------------\n")

