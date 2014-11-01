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

## get/joiners/byact/{aid}

method: get

return
	200 OK
	401 Did not Login
	[{uid
	  username
	  gender
	}]

## get/joiners/byuser/{uid}

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
	aid
	
return:
	200 OK
	400 Fail
	401 Did not Login
	403 Fobidden
	
	{jid:
	}
	
## delete/joiners/aid

method: post
return:
	200 OK
	400 Fail
	401 Did not Login
	
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
