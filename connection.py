import cx_Oracle #Need for oracle connect , also need to install instantclient from oracle
try:
    userName = '<USER_NAME>'
    password = '<PASSWORD>'
    hostName = '<HOST>'
    port = '<PORT>'
    serviceId = '<SERVICE_ID>'
    userRole = ''   #SYSDBA or ''
    if userRole == 'SYSDBA':
        userType = 'As Sys DBA'
        con = cx_Oracle.connect(userName+'/'+password+'@'+hostName+':'+port+'/'+serviceId,mode=cx_Oracle.SYSDBA)
    else:
        userType = 'as User'
        con = cx_Oracle.connect(userName+'/'+password+'@'+hostName+':'+port+'/'+serviceId)
    print('Trying to Connect')

    if con.version != '':
        print('Successfully connected to Database ' +userType+ 
        ' \n___________________________________________'+
        ' \n          *** DB DETAILS ***             '+
        ' \n    Username   --> '+userName+
        ' \n    Host       --> '+hostName+
        ' \n    Port       --> '+port+
        ' \n    Service id --> '+serviceId+
        ' \n    DB Version --> '+con.version+
        ' \n___________________________________________')
        curs = cx_Oracle.Cursor(con)
        print('Testing Query')
        dual = "select * from DUAL" # Oracle query to test
        curs.execute(dual)
        curr_version = curs.fetchone()
        x = len(curr_version) # getting length of Resultset return by query
        if x  > 0:    
            print('Query Executed Successfully.')
            #print(curr_version[0]) # Uncomment to show output of query.
        else:
            print('Query Executed , No Result Returned')
        con.close() 
        print('Connection Closed.')
except Exception as e:
    print('Exception Occured') #Exception caused by Database
    print(e)