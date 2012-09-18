// Filename: main.js
(function() {
    
    require.config({
        paths : {
              jquery                : 'jquery'
            , underscore            : 'js/lib/underscore-1.3.2-amd'
            , backbone              : 'js/lib/backbone-0.9.2-amd'
            , text                  : 'js/lib/require/text'
        }
        , baseUrl : "./"
    })
    
    require(['backbone', 'js/router'], function(Backbone, Workspace) {
        
        window.TodoRouter = new Workspace()
        
        Backbone.history.start({
            pushState : false
        })        
    })
}())
