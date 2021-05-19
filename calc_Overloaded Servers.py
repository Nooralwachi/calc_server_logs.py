from collections import defaultdict
def calc(filename):
	with open(filename, 'r') as f:
		cpu_f=ram_f=disk_f = 0
		previous_time=defaultdict(list)
		for line in f:
			# print(line)
			server, time,date,cpu,ram,disk = line.strip().split()
			
			if cpu_f>1:
				if len(previous_time['cpu']) > 0:
					prev= previous_time['cpu'][0]
					print(f'Warning: {server} CPU load is over 80% from {prev} to {time} {date}')
					cpu_f= False
			elif ram_f >1 :
				if len(previous_time['ram']) > 0:
					prev= previous_time['ram'][0]
					print(f'Warning: {server} RAM load is over 80% from {prev} to {time} {date}')
					ram_f =False
			elif disk_f >1:
				if len(previous_time['disk']) > 0:
					prev= previous_time['disk'][0]
					print(f'Warning: {server} Disk load is over 80% from {prev} to {time} {date}')
					disk_f = False
			
			if  float(cpu) >= 0.8:
				cpu_f+=1
				previous_time['cpu'].append(time + ' '+date)
			else:
				cpu_f=0
				previous_time['cpu']=[]
			if float(ram) >= 0.8:
				ram_f+=1
				previous_time['ram'].append(time + ' '+date)
			else:
				ram_f=0
				previous_time['ram']=[]
			if float(disk) >= 0.8:
				disk_f+=1
				previous_time['disk'].append(time + ' '+date)
			else:
				disk_f=0
				previous_time['disk']=[]
			# print(cpu_f,ram_f,disk_f,previous_time )
			
calc("servers_logs.py")
