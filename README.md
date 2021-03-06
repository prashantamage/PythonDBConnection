# PythonDBConnection

## This is sample file to check DB connection with oracle database.

### Prerequisite -

* cx_Oracle - This python module is required to check the connections with DB.
    use `pip install cx-Oracle` to install cx_Oracle on your machine.
    Refer [cx_Oracle](https://pypi.org/project/cx-Oracle/) for more information about cx_Oracle module.

* Oracle instant Client - This is require to connect with Oracle DB.
    Download Oracle Instant Client from following link. 
    Choose appropriate version depending on you OS.
    Refer [Oracle instant Client](https://www.oracle.com/in/database/technologies/instant-client.html) for more information.

### Execution - 
Get the connection.py from project  and modify as per your requirement.
Replace your database details.
![details](https://user-images.githubusercontent.com/13764086/124274856-65217680-db5f-11eb-8a81-1e546deb0fb2.PNG)

### Details 
userName = '<USER_NAME>'   -- Database user name to login

password = '<PASSWORD>'    -- Password for the user
    
hostName = '<HOST>'        -- Hoste name where Database is installed.
    
port = '<PORT>'            -- Port to connect with the database.
    
serviceId = '<SERVICE_ID>' -- Service ID for the database
    
userRole = 'SYSDBA' or ''  -- This is user role , Replce 'SYSDBA' or keep it blank ''. 

After doing required changes run connection.py by using following command.

`$python connection.py`

This will execute the connection.py file and will try to connect to Database.

### Output - 
After successfull connection you will get following output.

![pythonDbCheck](https://user-images.githubusercontent.com/13764086/124273722-027bab00-db5e-11eb-8e15-b7bd4e94fabb.PNG)

Here User Role is 'SYS DBA' or 'Normal User'.
At end connection will be terminated/closed to avoid multiple session opened issue.

For any support contact [prashantamage](https://github.com/prashantamage). 👍

Thank You.



