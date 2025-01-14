"""
Demonstrates how to download a large file

By default, file gets downloaded immediately.
The following example demonstrates how to download a large file without reading the whole content of a file
into memory.
"""

import os
import tempfile

from office365.graph_client import GraphClient
from tests import test_client_id, test_password, test_tenant, test_username


def print_progress(offset):
    # type: (int) -> None
    print("Downloaded '{0}' bytes...".format(offset))


client = GraphClient(tenant=test_tenant).with_username_and_password(
    test_client_id, test_username, test_password
)
# # 1. address file by path and get file metadata
file_item = (
    client.me.drive.root.get_by_path("archive/big_buck_bunny.mp4").get().execute_query()
)
# 2 download a large file (chunked file download)
with tempfile.TemporaryDirectory() as local_path:
    with open(os.path.join(local_path, file_item.name), "wb") as local_file:
        file_item.download_session(
            local_file, print_progress, chunk_size=1024 * 512
        ).execute_query()
    print(
        "File '{0}' has been downloaded into {1}".format(
            file_item.name, local_file.name
        )
    )
