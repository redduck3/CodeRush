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


method: get

return
	200 OK
	401 Did not Login
	[{uid
	  username
	  gender
	}]


method: get

return
	200 OK
	401 Did not login
	403 Fobidden
	[{aid
	  uid //ownerid
	  starttime
	  endtime
	  description
	}]

## post/joiners

method: post

input:
	uid
	 'uid'}
	200 OK
	400 Fail
	401 Did not Login
	403 Fobidden
	}
	

return:
	200 OK
	400 Fail
	401 Did not Login
	
# User

## login/

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
	200OK
		400 Fail(did not login)
		403 Fobidden
