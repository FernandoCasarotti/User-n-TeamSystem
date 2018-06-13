window.apiRoot = '/_ah/api/';

var scope_dev, root_dev, loc;

var mod = angular.module('teams-n-userSystem', ['ngRoute'], function () {});

mod.run(function ($rootScope, $http, $timeout, $location, $window) {
  root_dev = $rootScope;
  loc = $location;

  $rootScope.gapiLoaded = false;

  $rootScope.apiKey = 'AIzaSyAYSA0MoPmeOLI1yobGsHln71hJnIcFl_s';

  $rootScope.$on('$routeChangeSuccess', function (event, current, previous) {
    $('title').html(current.$$route.title);
  });

  $window.initGapi = function () {
    $rootScope.onGoogleApiLoad(...arguments);
  };

  $rootScope.onGoogleApiLoad = function () {
    let apisToLoad = 1;

    $rootScope.loading();

    let cback = () => {
      if (--apisToLoad === 0) {
        gapi.client.setApiKey(this.apiKey);
        $rootScope.gapiLoaded = true;
      }
    }

    gapi.client.load('user_n_teamsystem', 'v1.0', cback, $window.apiRoot);

  };

  $rootScope.safeApply = function (fn, repeated) {
    let phase = this.$root.$$phase;
    if (phase == '$apply' || phase == '$digest') {
      if (fn && (typeof (fn) === 'function')) {
        $timeout(function () {
          $rootScope.safeApply(fn, true);
        }, 1500);
      }
    } else if (repeated) {
      fn();
    } else {
      this.$apply(fn);
    }
  };
});

function onGoogleApiLoad() {
  if (window.initGapi != undefined) {
    gapi.load('client', window.initGapi);
  } else {
    setTimeout(onGoogleApiLoad, 500); // wait for 500 ms
  }
}
