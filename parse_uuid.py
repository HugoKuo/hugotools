import re

def parse_uuid():
	import commands
	prog_uuid = re.compile('UUID="(.+?)"')
	uuid_map = dict()
	blkids = set()
	blkids_ = commands.getoutput("blkid").splitlines()
	for blkid in blkids_:
		uuid = prog_uuid.search(blkid).group(1)

		blkid = blkid[:blkid.index(':')]
		blkids.add(blkid)

		uuid_map[blkid] = uuid
    
	disks = parse_fdisk(commands.getoutput("fdisk -l"))
	osdisks = set(disks.keys())

	devices = blkids - osdisks
	uuids = dict([(dev, uuid_map[dev]) for dev in devices])
	print uuids
	return uuids
def parse_fdisk(fdisk_output):
        result = {}
        for line in fdisk_output.split("\n"):
                if not line.startswith("/"): continue
                parts = line.split()
                #print parts
                inf = {}
                if parts[1] == "*":
                        inf['bootable'] = True
                        del parts[1]
                else:
                        inf['bootable'] = False
                        inf['start'] = int(parts[1])
                        inf['end'] = int(parts[2])
                        inf['blocks'] = int(parts[3].rstrip("+"))
                        inf['partition_id'] = int(parts[4], 16)
                        inf['partition_id_string'] = " ".join(parts[5:])
                result[parts[0]] = inf

		#print result
        return result


def main():
	parse_uuid()
	
if __name__ == '__main__': main()
