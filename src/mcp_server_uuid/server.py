from uuid import uuid4, UUID
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("UUID")


@mcp.tool()
def generate_uuid_v4(num: int) -> list[UUID]:
    """
    Generates a list of random UUID version 4 objects.

    Args:
        num (int): The number of UUIDs to generate.

    Returns:
        list: A list containing `num` randomly generated UUID version 4 objects.

    Example:
        >>> generate_uuid_v4(3)
        [UUID('f47ac10b-58cc-4372-a567-0e02b2c3d479'),
         UUID('550e8400-e29b-41d4-a716-446655440000'),
         UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')]
    """
    ids = [uuid4() for _ in range(num)]

    return ids


def stdio_server():
    mcp.run(transport="stdio")
