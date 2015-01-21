import listwriter


""" Main entry point of execution

"""

lw = listwriter.ListWriter()
        
print 'Retrieving channels..'
lw.retrieveDevices('channel')

print 'Retrieving iOS devices..'
lw.retrieveDevices('ios')

print 'Retrieving Android devices..'
lw.retrieveDevices('android')

print 'Writing CSV channel file..'
lw.writeListsToCSV('channel')

print 'Writing CSV iOS file..'
lw.writeListsToCSV('ios')

print 'Writing CSV Android file..'
lw.writeListsToCSV('android')

