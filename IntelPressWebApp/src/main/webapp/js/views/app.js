// js/views/app.js
define(function(require) {
    
    var   _ = require('underscore')
        , Backbone = require('backbone')
        , TodoView = require('js/views/todos')
        , StatsTemplate = require('text!tpl/stats-template.html')

	// The Application
	// ---------------

	// Our overall **AppView** is the top-level piece of UI.
	return Backbone.View.extend({

		// Instead of generating a new element, bind to the existing skeleton of
		// the App already present in the HTML.
		el: '#todoapp'

		// Our template for the line of statistics at the bottom of the app.
		, statsTemplate: _.template(StatsTemplate)

		// Delegated events for creating new items, and clearing completed ones.
		, events: {
			  'keypress #new-todo': 'createOnEnter'
			, 'click #clear-completed': 'clearCompleted'
			, 'click #toggle-all': 'toggleAllComplete'
		}

		// At initialization we bind to the relevant events on the `Todos`
		// collection, when items are added or changed. Kick things off by
		// loading any preexisting todos that might be saved in *localStorage*.
		, initialize: function() {
			this.input = this.$('#new-todo')
			this.allCheckbox = this.$('#toggle-all')[0]
			this.$footer = this.$('#footer')
			this.$main = this.$('#main')

			window.Todos.on( 'add', this.addAll, this )
			window.Todos.on( 'reset', this.addAll, this )
			window.Todos.on('change:completed', this.filterOne, this)
			window.Todos.on("filter", this.filterAll, this)

			window.Todos.on( 'all', this.render, this )

			window.Todos.fetch()
		}

		// Re-rendering the App just means refreshing the statistics -- the rest
		// of the app doesn't change.
		, render: function() {
			var completed = window.Todos.completed().length
			var remaining = window.Todos.remaining().length

			if ( window.Todos.length ) {
				this.$main.show()
				this.$footer.show()

				this.$footer.html(this.statsTemplate({
					completed: completed
					, remaining: remaining
				}))

				this.$('#filters li a')
					.removeClass('selected')
					.filter('[href="#/' + ( window.TodoFilter || '' ) + '"]')
					.addClass('selected')
			} else {
				this.$main.hide()
				this.$footer.hide()
			}

			this.allCheckbox.checked = !remaining
		}

		// Add a single todo item to the list by creating a view for it, and
		// appending its element to the `<ul>`.
		, addOne: function( todo ) {
			var view = new TodoView({ model: todo })
			$('#todo-list').append( view.render().el )
		}

		// Add all items in the **Todos** collection at once.
		, addAll: function() {
			this.$('#todo-list').html('')
			window.Todos.each(this.addOne, this)
		}

		, filterOne : function (todo) {
			todo.trigger("visible");
		}

		, filterAll : function () {
			window.Todos.each(this.filterOne, this)
		}

		// Generate the attributes for a new Todo item.
		, newAttributes: function() {
			return {
				title: this.input.val().trim()
				, order: window.Todos.nextOrder()
				, completed: false
			}
		}

		// If you hit return in the main input field, create new **Todo** model,
		// persisting it to *localStorage*.
		, createOnEnter: function( e ) {
			if ( e.which !== ENTER_KEY || !this.input.val().trim() ) {
				return
			}

			window.Todos.create( this.newAttributes() )
			this.input.val('')
		}

		// Clear all completed todo items, destroying their models.
		, clearCompleted: function() {
			_.each( window.Todos.completed(), function( todo ) {
				todo.destroy()
			})

			return false
		}

		, toggleAllComplete: function() {
			var completed = this.allCheckbox.checked

			window.Todos.each(function( todo ) {
				todo.save({
					'completed': completed
				})
			})
		}
	})
})
