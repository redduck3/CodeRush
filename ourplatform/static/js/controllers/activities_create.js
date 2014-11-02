angular.module('tongji')
.controller('activitiesCreateController',['$scope', '$http', '$location', function($scope, $http, $location) {
  $scope.activity = {};
  $scope.fields = [
    {name: "title", describe: "标题"},
    {name: "startDate", describe: "开始时间", type: "date"},
    {name: "startTime", describe: "", type: "time"},
    {name: "endDate", describe: "报名结束时间", type: "date"},
    {name: "endTime", describe: "", type: "time"},
    {name: "description", describe: "描述"}
  ];
  
  $scope.createActivities = function(){
      var url = "/post/activities";
      var postData = {};
      postData.uid = 1;
      postData.title = $scope.activity.title;
      postData.starttime = $scope.activity.startDate + $scope.activity.startTime;
      postData.endtime = $scope.activity.endDate + $scope.activity.endTime;
      postData.description = $scope.activity.description;
      $location.path("/activities");
      
  }
  
}])

.controller('activitiesController', ['$scope', 'dataService', function($scope, dataService) {
    dataService.getData('/static/json/activity2.json').then(function(res){
        $scope.data = res.data;
    });
    console.log($scope.data);
    
}]) 
