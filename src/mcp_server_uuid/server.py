from uuid import uuid4
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("UUID")


@mcp.tool()
def generate_uuid_v4():
    """
    Generate UUID V4
    """

    id = uuid4()

    return id


def stdio_server():
    mcp.run(transport="stdio")
