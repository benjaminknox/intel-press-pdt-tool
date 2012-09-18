// js/collections/todos.js
define(function(require) {

	var   _ = require('underscore')
        , Backbone = require('backbone')
        , Todo = require('js/models/todo')

	// Todo Collection
	// ---------------

	// The collection of todos is backed by *localStorage* instead of a remote
	// server.
	return Backbone.Collection.extend({

		// Reference to this collection's model.
		model: Todo

		, url : location.pathname + 'todo'

		, fetch : function(options) {
            options || (options = {})
            options.contentType = 'application/json'
            return Backbone.Collection.prototype.fetch.call(this, options)
        }

		// Save all of the todo items under the `"todos"` namespace.
		// localStorage: new Store('todos-backbone'),

		// Filter down the list of all todo items that are finished.
		, completed: function() {
			return this.filter(function( todo ) {
				return todo.get('completed')
			})
		}

		// Filter down the list to only todo items that are still not finished.
		, remaining: function() {
			return this.without.apply( this, this.completed() )
		}

		// We keep the Todos in sequential order, despite being saved by unordered
		// GUID in the database. This generates the next order number for new items.
		, nextOrder: function() {
			if ( !this.length ) {
				return 1
			}
			return this.last().get('order') + 1
		}

		// Todos are sorted by their original insertion order.
		, comparator: function( todo ) {
			return todo.get('order')
		}
	})
})
