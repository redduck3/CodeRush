angular.module('tongji')
.controller('masterController', ['$scope','$http', function($scope, $http) {
    $scope.hello = "市级标题";


}]);

angular.module('tongji')
.controller('imageViewerController', ['$scope', function($scope) {
  $scope.myInterval = 5000;
  var slides = $scope.slides = [];
  $scope.addSlide = function(i) {
    slides.push({
      image: '/static/image/' + i +  '.jpg',
      // text: ['More','Extra','Lots of','Surplus'][slides.length % 4] + ' ' +
      //   ['Cats', 'Kittys', 'Felines', 'Cutes'][slides.length % 4]
      text: ['have sports toghter', 'Play game toghter'][i]
    });
  };
  for (var i=0; i<2; i++) {
    $scope.addSlide(i);
  }
}]);