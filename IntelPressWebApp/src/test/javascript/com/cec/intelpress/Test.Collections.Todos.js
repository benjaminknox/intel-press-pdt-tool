// javascript/Test.SaifeManagement.Collections.ContactGroups.js
define(['js/collections/todos'
        , 'backbone'], function(Todos, Backbone) {
  
    describe('js/collections/todos Testing', function() {
    
        var collection
        
        beforeEach(function() {
            // any set up before
            collection = new Todos()
        })
        
        it('should have the correct url', function() {
            expect(collection.url).toContain('todo')  
        })
        
        it('should initialize with 0 length', function() {
            expect(collection.length).toBe(0)
        })
    })
})