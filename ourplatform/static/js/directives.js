'use strict';

/* Directives */
angular.module('tongji')
.directive('formCustom', ['pregMatchService', '$timeout', function (pregMatchService, $timeout) {
    return {
        restrict: 'A',
        templateUrl: "/static/js/template/form.html",
        replace: true,
        transclude: true,
        scope : {
            fields: "=formCustom",
            model: "=model",
            state: "=?state",
            alerts: "=?alerts",
            submitButton: "@?submitButton",
            formSubmit: "&formSubmit",
            hideError: "=?hideError",
        },
        link: function (scope, element, attrs) {
            scope.alerts = scope.alerts || [];
            scope.state = scope.form;
            scope.state.setAlerts = function (alerts) {
                if (!Array.isArray(alerts)) {
                    alerts = [alerts];
                }
                scope.alerts = alerts;
            };
            scope.extra = {};
            scope.closeAlert = function (i) {
                scope.alerts.splice(i, 1);
            };
            scope.validators = {
                'minLength': function (scope, args) {
                    var field = scope.field;
                    if (field.minLength == null && field.type == 'password') {
                        // 密码至少6字符长。
                        field.minLength = 6;
                    }
                    return field.minLength == null || args.$value == null ||
                        args.$value.toString().length >= field.minLength;
                },
                'maxLength': function (scope, args) {
                    var field = scope.field;
                    return field.maxLength == null || args.$value == null ||
                        args.$value.toString().length >= field.maxLength;
                },
                'custom': function (scope, args) {
                    var field = scope.field;
                    if (typeof field.validate == 'function') {
                        return field.validate(args.$value, field);
                    }
                    return true;
                }
            };
            scope.isSuccess = function (form, fieldName) {
                fieldName = fieldName || 'input';
                return form[fieldName].$dirty && !!form[fieldName].$valid;
            };
            scope.isError = function (form, fieldName) {
                fieldName = fieldName || 'input';
                if (scope.hideError && !scope.attempted &&
                    form[fieldName].$pristine) {
                    return false;
                }
                return !form[fieldName].$valid;
            };
            scope.patternForField = function (field) {
                if (field.pattern) {
                    if (typeof field.pattern == 'string') {
                        return pregMatchService.regExpression[field.pattern];
                    } else {
                        return field.pattern;
                    }
                } else {
                    // 如果有对应输入类型的正则，就用那个。否则匹配所有输入。
                    return pregMatchService.regExpression[field.type] || /(?:)/;
                }
            };
            scope.onFormSubmit = function () {
                scope.attempted = true;
                if (scope.state.$invalid) {
                    scope.alerts = [
                        {type: 'danger', msg: '请更正表单中的错误！'}
                    ];
                    return;
                }
                if (scope.state.$pristine) {
                    scope.alerts = [{type: 'warning', msg: '你什么也没有修改'}];
                    return;
                }
                scope.formSubmit(scope.model);
            };
        }
    }
}]);
