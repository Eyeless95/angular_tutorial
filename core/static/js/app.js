/**
 * Created by bogdan on 7/5/16.
 */
var app = angular.module('myApp', []);

app.controller("myCtrl", function($scope) {
    $scope.firstName = 'Bogdan';
    $scope.lastName = 'Zagrebin';
});
