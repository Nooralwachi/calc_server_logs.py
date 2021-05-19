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
print("-----------")


def overload(logname):
    server = ''
    cpu_load = [0,0,0]
    ram_load = [0,0,0]
    disk_load = [0,0,0]
    with open(logname, 'r') as f:
        for line in f:
            words = line.split()
            server = words[0]
            date = words[1] + ' ' + words[2]
            cpu = words[3]
            ram = words[4]
            disk = words[5]
            cpu_load = helper(server, 'CPU', date, cpu_load, cpu)
            ram_load = helper(server, 'RAM', date, ram_load, ram)
            disk_load = helper(server, 'Disk', date, disk_load, disk)
    if cpu_load[2] >= 3:
        print("Warning: {} CPU load is over 80% from {} to {}".format(server, cpu_load[0], cpu_load[1]))
    if ram_load[2] >= 3:
        print("Warning: {} RAM load is over 80% from {} to {}".format(server, ram_load[0], ram_load[1]))
    if disk_load[2] >= 3:
        print("Warning: {} Disk load is over 80% from {} to {}".format(server, disk_load[0], disk_load[1]))
    return

def helper(server, type, date, data, load):
    if float(load) >= 0.8:
        if data[2] > 0:
            data[1] = date
            data[2] += 1
        else:
            data[0] = date
            data[2] = 1
    else:
        if data[2] >= 3:
            print("Warning: {} {} load is over 80% from {} to {}".format(server, type, data[0], data[1]))
        data = [0, 0, 0]
    return data 

overload('servers_logs.py')