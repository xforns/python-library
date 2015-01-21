import urbanairship as ua
import csv as csv


""" Global variables and various initializations

"""


# UA credentials
use_stl_credentials = 1
key = ""
secret = ""

channel = 'channel'
ios = 'ios'
android = 'android'

devices = { channel: [], 
            ios: [], 
            android: [] }
base_output_dir = 'import_files/'
files = {   channel: base_output_dir+'devices_channel.csv', 
            ios: base_output_dir+'devices_ios.csv', 
            android: base_output_dir+'devices_android.csv' }


def init():
	""" Initializes various variables
	
	"""
	global airship
	airship = ua.Airship(key,secret)
	print 'Connected to UA'


def retrieveDevices():
	""" Retrieves the devices from UA
	
	"""
	global devices
    
	print 'Retrieving channels..'
	devices[channel] = ua.ChannelList(airship)
    
	print 'Retrieving iOS devices..'
	devices[ios] = ua.DeviceTokenList(airship)
	
	print 'Retrieving Android devices..'
	devices[android] = ua.APIDList(airship)


def writeListsToCSV():
	""" Writes the devices to CSV files
	
	"""
    
	print 'Writing CSV channel file..'
	writeList(channel)
    
	print 'Writing CSV iOS file..'
	writeList(ios)
    
	print 'Writing CSV Android file..'
	writeList(android)


def writeList(typeList):
	""" Writes the devices type to a CSV file
	
	"""
    
	file_desc = open(files[typeList], 'w')
	writer = csv.writer(file_desc,quoting=csv.QUOTE_ALL)
	data = buildHeaders(typeList)
	
	for dev in devices[typeList]:
		data.append( buildRow(typeList,dev) )
    
	writer.writerows(data)
	file_desc.close()


def buildHeaders(typeList):
	""" Retrieves the header colums for this type list
	
	"""
	if typeList == channel:
		return [['channel','type','push address','opt in','installed','created','last registration','tags','alias','badge (ios)','quiettime start (ios)','quiettime end (ios)','tz (ios)']]
	elif typeList == ios:
		return [['deviceID','platform','tags','alias']]
	elif typeList == android:
		return [['deviceID','platform','tags','alias']]

def buildRow(typeList,device):
	""" Retrieves the data values for this type list
	
	"""
	if typeList == channel:
		return [device.channel_id,device.push_address,device.opt_in,device.installed,
                device.created,device.last_registration,device.tags,device.alias,
                device.ios['badge'],device.ios['quiettime']['start'],device.ios['quiettime']['end'],device.ios['tz']]
	elif typeList == ios:
		return [device.device_token,'iOS',device.tags,device.alias]
	elif typeList == android:
		return [device.apid,'Android',device.tags,device.alias]


""" Main entry point of execution

"""

init()
retrieveDevices()
writeListsToCSV()
