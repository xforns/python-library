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




"""

- Notifica.re import file format

	deviceID,osVersion,appVersion,platform,language,userID,userName
	"b489bc0c0c4420dc6b09f54270548292a102ac9","8.0","1.1","iOS","nl","test123@example.com","Test User 1"


- DeviceToken format:

	"device_token": "0101F9929660BAD9FFF31A0B5FA32620FA988507DFFA52BD6C1C1F4783EDA2DB",
    "active": false,
    "alias": null,
    "tags": []


- APID format:

	"c2dm_registration_id": null,
	"created": "2013-01-25 00:55:06",
	"tags": [
		"tag1"
	],
	"apid": "11111111-1111-1111-1111-111111111111",
	"alias": "alias1",
	"active": true


- Channel format:

	"channel_id": "9c36e8c7-5a73-47c0-9716-99fd3d4197d5",
	"device_type": "ios",
	"push_address": "FE66489F304DC75B8D6E8200DFF8A456E8DAEACEC428B427E9518741C92C6660",
	"opt_in": true,
	"installed": true,
	"created": "2014-03-06T18:52:59",
	"last_registration": "2014-10-07T21:28:35",
	"alias": "your_user_id",
	"tags": [
		"tag1",
		"tag2"
	],
	"ios": {
		"badge": 2,
		"quiettime": {
			"start": "22:00",
			"end": "8:00"
		},
		"tz": "America/Los_Angeles"
	}

"""