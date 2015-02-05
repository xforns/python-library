import urbanairship as ua
import csv
import listwriterconfig as lwc
import logging


class ListWriter():
    """ Helper class that aids in the retrieval of devices (ios, android or channels) 
        and writes them to a file

    """
    
    logger = logging.getLogger('urbanairship')
    airship = None
    key = lwc.ListWriterConfig.get('key')
    secret = lwc.ListWriterConfig.get('secret')
    
    devices = { 'channel': [], 
                'ios': [], 
                'android': [] }
    base_output_dir = lwc.ListWriterConfig.get('base_output_dir')
    files = {   'channel':    base_output_dir + lwc.ListWriterConfig.get('file_channel'), 
                'ios':        base_output_dir + lwc.ListWriterConfig.get('file_ios'), 
                'android':    base_output_dir + lwc.ListWriterConfig.get('file_android') }


    def __init__(self):
    	""" Initializes various variables
	
    	"""
    	self.airship = ua.Airship(self.key,self.secret)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        ch.setLevel(logging.ERROR)
        self.logger.addHandler(ch)
        
    	print 'Connected to UA'


    def retrieveDevices(self,typeList):
    	""" Retrieves the devices from UA
	
    	"""
        
    	if typeList != 'channel' and typeList != 'ios' and typeList != 'android':
    		print 'Specified type does not exist!'
    		return
        
        if typeList == 'channel':
    		self.devices[typeList] = ua.ChannelList(self.airship)
    	elif typeList == 'ios':
    		self.devices[typeList] = ua.DeviceTokenList(self.airship)
    	elif typeList == 'android':
    		self.devices[typeList] = ua.APIDList(self.airship)


    def writeListsToCSV(self,typeList):
    	""" Writes the devices to CSV files
	
    	"""
        
    	if typeList != 'channel' and typeList != 'ios' and typeList != 'android':
    		print 'Specified type does not exist!'
    		return
        
    	file_desc = open(self.files[typeList], 'w')
    	writer = csv.writer(file_desc,quoting=csv.QUOTE_ALL)
    	data = self.buildHeaders(typeList)
	
    	for dev in self.devices[typeList]:
    		data.append( self.buildRow(typeList,dev) )
    
    	writer.writerows(data)
    	file_desc.close()


    def buildHeaders(self,typeList):
    	""" Retrieves the header colums for this type list
	
    	"""
    	if typeList == 'channel':
    		return [['channel','type','push address','opt in','installed','created','last registration','tags','alias','badge (ios)','quiettime start (ios)','quiettime end (ios)','tz (ios)']]
    	elif typeList == 'ios':
    		return [['deviceID','platform','tags','alias']]
    	elif typeList == 'android':
    		return [['deviceID','platform','tags','alias']]

    def buildRow(self,typeList,device):
    	""" Retrieves the data values for this type list
	
    	"""
    	if typeList == 'channel':
            if hasattr(device,'ios'):
                return [device.channel_id,device.push_address,device.opt_in,device.installed,
                        device.created,device.last_registration,device.tags,device.alias,
                        device.ios['badge'],device.ios['quiettime']['start'],device.ios['quiettime']['end'],device.ios['tz']]
            else:
                return [device.channel_id,device.push_address,device.opt_in,device.installed,
                        device.created,device.last_registration,device.tags,device.alias,
                        '','','','']
    	elif typeList == 'ios':
    		return [device.device_token,'iOS',device.tags,device.alias]
    	elif typeList == 'android':
    		return [device.apid,'Android',device.tags,device.alias]

