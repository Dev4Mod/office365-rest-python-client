"""
Update users in batch mode

https://learn.microsoft.com/en-us/graph/api/user-update
"""

from office365.graph_client import GraphClient
from tests import test_client_id, test_password, test_tenant, test_username

client = GraphClient(tenant=test_tenant).with_username_and_password(
    test_client_id, test_username, test_password
)
users = (
    client.users.get()
    .filter("startswith(displayName, 'testuser')")
    .top(50)
    .execute_query()
)

for u in users:
    u.set_property("officeLocation", "18/2111").update()

client.execute_batch()
