// js/models/todo.js
define(function(require) {
    
    var   _ = require('underscore')
        , Backbone = require('backbone')

	// Todo Model
	// ----------

	// Our basic **Todo** model has `title`, `order`, and `completed` attributes.
	return Backbone.Model.extend({

		// Default attributes for the todo
		// and ensure that each todo created has `title` and `completed` keys.
		defaults: {
			title: ''
			, completed: false
		}

		, urlRoot : 'todo/'

		, fetch : function(options) {
            options || (options = {})
            options.contentType = 'application/json'
            return Backbone.Model.prototype.fetch.call(this, options)
        }
        
        , destroy : function(options) {
            options || (options = {})
            options.contentType = 'application/json'
            return Backbone.Model.prototype.destroy.call(this, options)
        }

		// Toggle the `completed` state of this todo item.
		, toggle: function() {
			this.save({
				completed: !this.get('completed')
			})
		}

	})
})
