module main

import veb

type Event = string 

// Our context struct must embed `veb.Context`!
pub struct Context {
	veb.Context
}

pub struct App {
	veb.StaticHandler
pub mut:
	conn chan Event
}

// This is how endpoints are defined in veb. This is the index route
pub fn (app &App) index(mut ctx Context) veb.Result {
	return $veb.html()
}

fn db() chan Event {
	ch := chan Event{}
	return ch
}

fn main() {
	mut app := &App{ 
		conn: db()
	}
	app.handle_static('static', false)!
	// Pass the App and context type and start the web server on port 8080
	veb.run[App, Context](mut app, 8080)
}
