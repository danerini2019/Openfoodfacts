from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import json
import os
from loguru import logger



TABLES = [ 
    {"name":"Additive", "fields":["name"]},
    {"name":"Allergen", "fields":["name"]}
]


# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="http://192.168.1.37:9080/v1/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

for table in TABLES:
# Provide a GraphQL query
    query = gql(
        "query GetData {{ {} {{ {} }}}}".format(table['name'], '\n'.join(table['fields']))
    )

    # Execute the query on the transport
    result = client.execute(query)
    # Parse result and write source
    file_path = os.path.join(os.path.dirname(__file__), f"sources\\en\\{table['name']}.json")
    fd = open(file_path, "w")
    source_data = {}
    for elem in result[table["name"]]:
        source_data[elem["name"]] = elem["name"]
    fd.write(json.dumps(source_data, indent=4))
    logger.debug(f"Translation file for table {table['name']} exported")
