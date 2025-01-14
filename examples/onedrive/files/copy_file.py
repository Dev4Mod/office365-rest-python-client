"""
This example copies a file identified by {server relative path} into a folder identified with a {server relative path}.
The new copy of the file will be named Sample (copy).rtf.

https://learn.microsoft.com/en-us/graph/api/driveitem-copy?view=graph-rest-1.0
"""

from office365.graph_client import GraphClient
from tests import test_client_id, test_password, test_tenant, test_username

client = GraphClient(tenant=test_tenant).with_username_and_password(
    test_client_id, test_username, test_password
)
# source_path = "archive/Sample.rtf"
local_path = "../../data/Financial Sample.xlsx"
source_file = client.me.drive.root.upload_file(local_path).execute_query()

#  source_file = client.me.drive.root.get_by_path(source_path)  # source file item
target_path = "archive/2018"
target_folder = client.me.drive.root.get_by_path(target_path)
# result = source_file_item.copy(name=new_name).execute_query()  # copy to the same folder with a different name
result = source_file.copy(
    parent=target_folder
).execute_query()  # copy to another folder
print(result.value)
