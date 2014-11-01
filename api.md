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