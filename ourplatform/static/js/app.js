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

    $routeProvider.when('/register', {
        templateUrl: '/static/views/register.html'
    });
}])

.factory('pregMatchService', function() {
    var service = {
        pregMatch: function (name, value, displayName) {
            //若不存在，在默认为无需匹配
            if (typeof service.regExpression[name] === 'undefined') {
                return true;
            }
            if (value.toString().match(service.regExpression[name]) !== null) {
                return true;
            } else {
                service.error = "请输入正确的" + displayName;
                return false;
            }
        },
        regExpression : {
            email: /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/,
            student_number: /^[0-9]+$/,
            phone: /^1[3|4|5|8]\d{9}$/,
            chinese: /^[\u4E00-\u9FA5]+$/,
            identity: /^[A-Za-z0-9_]+$/
        },
        error : ""
    };

    return service;
})

