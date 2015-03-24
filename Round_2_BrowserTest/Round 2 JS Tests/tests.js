// An Example of how Qunit works
test('Example test', function(){
	equal(1, 1, 'One is one');
})

function allday(val) {
	if (val === 'true') {
		return allDay = true;
	} else {
		return allDay = false;
	}
}

				
test('Event All Day False', function(){
	equal(allday('false'), false);
})

test('Event All Day True', function(){
	equal(allday('true'), true);
})

function selectable(val) {
	if (val) {
		return true;
	} else {
		return false;
	}
}

function selectHelper(val) {
	if (val) {
		return true;
	} else {
		return false;
	}
}

test('Selectable True', function(){
	equal(selectable(true), true);
})

test('Selectable False', function(){
	equal(selectable(false), false);
})

test('selectHelper True', function(){
	equal(selectHelper(true), true);
})

test('selectHelper False', function(){
	equal(selectHelper(false), false);
})

function formatDate(val) {
	n = val.length
	if (n == 19) {
		return true;
	} else {
		return false;
	}
}

test('formatDate Correct length True', function(){
	equal(formatDate('yyyy-MM-dd HH:mm:ss'), true);
})

test('formatDate Correct length False', function(){
	equal(formatDate('yyyy-MM-ddHH:mm:ss'), false);
})

asyncTest('events.php', function(){
	expect(1); // we have one async test to run
	
	var xhr = $.ajax({
		type: 'GET',
		url: 	'events.php'
	})
	.always(function(data, status){
		var $data = $(data);
		var pageTitle = $data.filter('title').text();
		equal(pageTitle, 'events.php', 'Title of events.php should be \'events.php\'');
		start(); // we have our answer for this assertion, continue testing other assertions
	});

});

asyncTest('add_events.php', function(){
	expect(1); // we have one async test to run
	
	var xhr = $.ajax({
		type: 'GET',
		url: 	'add_events.php'
	})
	.always(function(data, status){
		var $data = $(data);
		var pageTitle = $data.filter('title').text();
		equal(pageTitle, 'add_events.php', 'Title of add_events.php should be \'add_events.php\'');
		start(); // we have our answer for this assertion, continue testing other assertions
	});

});

asyncTest('update_events.php', function(){
	expect(1); // we have one async test to run
	
	var xhr = $.ajax({
		type: 'GET',
		url: 	'update_events.php'
	})
	.always(function(data, status){
		var $data = $(data);
		var pageTitle = $data.filter('title').text();
		equal(pageTitle, 'update_events.php', 'Title of update_events.php should be \'update_events.php\'');
		start(); // we have our answer for this assertion, continue testing other assertions
	});

});

asyncTest('delete_event.php', function(){
	expect(1); // we have one async test to run
	
	var xhr = $.ajax({
		type: 'GET',
		url: 	'delete_event.php'
	})
	.always(function(data, status){
		var $data = $(data);
		var pageTitle = $data.filter('title').text();
		equal(pageTitle, 'delete_event.php', 'Title of delete_event.php should be \'delete_event.php\'');
		start(); // we have our answer for this assertion, continue testing other assertions
	});

});





