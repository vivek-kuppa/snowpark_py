from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# Replace these variables with your Snowflake account details
connection_parameters = {
    "account": "yfqjinr-hj52378",
    "user": "Vivek",
    "password": "Icui4cu@",
    "role": "AccountAdmin",
    "warehouse": "compute_wh",
    "database": "sp",
    "schema": "s"
}

# Create a new session with the connection parameters
session = Session.builder.configs(connection_parameters).create()

# Now you can use the session object to interact with your Snowflake account
# For example, you can perform a query as follows:

df = session.table("COMPANY").select(col("pincode"))
df.show(10)

# Remember to close the session when you're done
session.close()
