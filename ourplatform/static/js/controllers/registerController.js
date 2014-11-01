angular.module('tongji')
.controller('registerController', ['$scope', '$http', function($scope, $http){
    $scope.success = false;
    $scope.user = {};
   
    $scope.fields = [
        {name: "username", describe: "用户名"},
        {name: "password", describe: "密码", type: 'password', needConfirm: true},
        {name: "gender", describe: "性别", type: 'radio', 
            options:[
                {text: "男", value: 1}, 
                {text: "女", value: 0}
            ]
        }     
    ];
    
    $scope.register = function(){
        console.log($scope.user);
        var url = '/login/';
        var postData = $scope.user;
        $http.post(url, postData).then(
            function(res){
                console.log(res);
            },
            function(res){
            }
        );
    }
}])
