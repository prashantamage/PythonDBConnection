# PythonDBConnection

## This is sample file to check DB connection with oracle database.

### Prerequisite -
        cx_Oracle - This python module is required to check the connections with DB.
            use "pip install cx-Oracle" to install cx_Oracle on your machine.
            Refer [cx_Oracle](https://pypi.org/project/cx-Oracle/) for more information about cx_Oracle module.
        
        Oracle instant Client - This is require to connect with Oracle DB.
            Download Oracle Instant Client from following link. Choos appropriate version depending on you OS.
            Refer [Oracle instant Client](https://www.oracle.com/in/database/technologies/instant-client.html) for more information.

### Execution - 
        Get the connection.py from project and run by using following command.
        
        `$python connection.py`
        
        This will execute the connection.py file and will try to connect to Database.

### Output - 
        After successfull connection you will get following output.


        Trying to Connect
        Successfully connected to Database as <USER_ROLE>
        ___________________________________________
                *** DB DETAILS ***
            Username   --> <USER_NAME>
            Host       --> <HOST_NAME>
            Port       --> <PORT>
            Service id --> <SERVICE_ID>
            DB Version --> <DB_VERSION>
        ___________________________________________
        Testing Query
        Query Executed Successfully.
        Connection Closed.

        Here User Role is 'SYS DBA' or 'Normal User'.
        At end connection will be terminated/closed to avoid multiple session opened issue.

For any support contact @github/support prashantamage. @octocat :+1

Thank You.



