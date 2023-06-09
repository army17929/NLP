from doccano_client import DoccanoClient

# Instantiate a client and log into a Doccano instance 
client = DoccanoClient('http://127.0.0.1:8000')
client.login(username='army17929',password='64rnjsdhghkd!')

# Get basic information about the authorized user.
user = client.get_profile()

# List all projects
projects = client.list_projects()
print(projects)