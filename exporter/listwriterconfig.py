class ListWriterConfig():
    """ Configuration properties used by listwriter.py

    """
    
    ######
    
    # UA credentials
    key = ''
    secret = ''

    # Output dir for CSV files
    base_output_dir = 'export_files/'

    # File names
    file_channel = 'devices_channel.csv'
    file_ios = 'devices_ios.csv'
    file_android = 'devices_android.csv'
    
    ######
    
    config = { 'key': key, 'secret': secret, 'base_output_dir': base_output_dir, 'file_channel': file_channel, 'file_ios': file_ios, 'file_android': file_android }
    
    
    @classmethod
    def get(self,key):
        """ Returns the configuration parameters given the key

        """
        return self.config[key]
