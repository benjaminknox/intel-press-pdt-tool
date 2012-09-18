// js/router.js
define(function(require) {

    var   $ = require('jquery')
        , _ = require('underscore')
        , Backbone = require('backbone')
        , TodoList = require('js/collections/todos')
        , Todo = require('js/models/todo')
        , AppView = require('js/views/app')

	// Todo Router
	// ----------

	return Backbone.Router.extend({
		
		routes:{
			'*filter': 'setFilter'
		}

		, initialize : function() {
			// Create our global collection of **Todos**.
			window.Todos = new TodoList();

			// Kick things off by creating the **App**.
        	window.AppView = new AppView();

        	window.ENTER_KEY = 13;
		}

		, setFilter: function( param ) {
			// Set the current filter to be used
			window.TodoFilter = param.trim() || ''

			// Trigger a collection filter event, causing hiding/unhiding
			// of Todo view items
			window.Todos.trigger('filter')
		}
	})
})
