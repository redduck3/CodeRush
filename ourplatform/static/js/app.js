angular.module('tongji', [
    'ngRoute',
    'ui.bootstrap',
])
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'views/dashbroad.html'
    });
    
    $routeProvider.when('/login', {
        templateUrl: 'views/login.html'
    });
}])
