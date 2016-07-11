require(["js/i18n!nls/i18n"], function(nls) {
	
	document.homeTitle = nls.homeTitle;
	
	angular.module("home", []).controller("MainController", [ "$scope", "$http", "$sce", 
	                                                          function($scope, $http, $sce) {
		
		nls.cfPluginsRepo = $sce.trustAsHtml(nls.cfPluginsRepo);
		nls.bxPluginsRepo = $sce.trustAsHtml(nls.bxPluginsRepo);
		nls.restrictions = $sce.trustAsHtml(nls.restrictions);
		nls.proxyNote = $sce.trustAsHtml(nls.proxyNote);
		nls.moreInfo = $sce.trustAsHtml(nls.moreInfo);
		
		$scope.nls = nls;
		$scope.recordDownload = function(platform, version){
			var record = {
				platform: platform,
				userAgent: navigator.userAgent,
				userLanguage: navigator.language,
				userPlatform: navigator.oscpu || navigator.platform,
				time: (new Date()).getTime(),
				version: version
			};
			$http({
				method: "POST",
				url: "/analytics/downloads",
				data: record
			});
		}
		
		$http({ method: "GET", url: "/all_versions" }).then(function(response) {
			
			$scope.latestVersion = response.data[0];
			nls.currentVersion = nls.currentVersion.replace("{{:latest}}", $scope.latestVersion.version);
			
	    }, function(errResponse) {})["finally"](function() {
			
	    	setTimeout(function() {
	    		$(".global-spinner-wrap").remove();
	    	}, 300);
	    });
	}]);
	
	angular.bootstrap(document, ["home"]);
});
