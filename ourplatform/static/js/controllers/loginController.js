angular.module('tongji')
.controller('loginController', ['$scope', '$http', function($scope, $http){
    $scope.success = false;
    $scope.user = {};
   
    $scope.fields = [
        {name: "username", describe: "用户名"},
        {name: "password", describe: "密码", type: 'password', needConfirm: false},
    ];
    
    $scope.login = function(){
        console.log($scope.user);
        var url = '/post/users/';
        var postData = $scope.user;
        $http(url, postData).then(
            function(res){
                $scope.success = true;
                console.log(res);
            },
            function(res){
            }
        );
    }
}])
