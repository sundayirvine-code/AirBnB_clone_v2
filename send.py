from fabric import Connection

# Define the remote hosts
hosts = ['54.160.103.207', '34.202.159.134']

# Define the path to the file on the local machine
local_path = '0-setup_web_static.sh'

# Define the path to the remote directory where the file will be uploaded
remote_dir = '/tmp/'

def send_file():
    # Loop through the remote hosts and upload the file
    for host in hosts:
        # Create a connection object to the remote host
        conn = Connection(host)

        # Use the put command to upload the file to the remote host
        conn.put(local_path, remote=remote_dir)

        # Close the connection
        conn.close()

# Call the task to send the file
send_file()

