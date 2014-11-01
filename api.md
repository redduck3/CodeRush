# Activity

## post/activities/

method: post

input:

	{'uid',
     'starttime',
     'endtime',
     'description'}

return:

	{'aid',
     'uid',
     'starttime',
     'endtime',
     'description'}

## get/activities/

method: get

return:

	[{'aid'
    'uid'
    'starttime'
    'endtime'
	'description'}]

## get/activities/{id}

method: get

return:

	{'aid'
    'uid'
    'starttime'
    'endtime'
	'description'}

## get/activities/undo

method: get

return:

	[{'aid'
    'uid'
    'starttime'
    'endtime'
	'description'}]

## put/activities/{aid}

method: post

input:

	{'uid'
    'starttime'
    'endtime'
	'description'}

return:

	200OK
	
	
# User

## login/

	return: 
		200 OK
		
		
## logout/	
		
	return:
		200 OK
		
		
## post/users/
	
return:
	200 OK
	400 Fail
	{'uid':userid
	 'username':username
	}
	
## get/users/{id}
	
return:
	200 OK
	400 Fail
	{'uid'
	 'username'
	 'password'
	 'gender'
	
	}
	
## delete/users/{id}
	
	return:
		200 OK
		400 Fail(did not login)
		403 Fobidden
## put/users/

	return:
		200 OK
		400 Fail(did not login)
		403 Fobidden
