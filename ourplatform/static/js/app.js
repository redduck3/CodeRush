angular.module('tongji', [
    'ngRoute',
    'ui.bootstrap',
])
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/views/dashboard.html'
    });
    
    $routeProvider.when('/login', {
        templateUrl: '/static/views/login.html'
    });
}])
