
  

  app.controller('TabController', function(){
    this.tab = 3;

    this.setTab = function(newValue){
      this.tab = newValue;
    };

    this.isSet = function(tabName){
      return this.tab === tabName;
    };
  });

  
  
  app.controller("retriveCtrl",['$scope','$filter','NgTableParams',function($scope,$filter,NgTableParams){
	
$scope.users = [{name: "Moroni", assigname: "Varun",module:"UI",desc:"Demo1",sdate:"09/09/2017",edate:"09/10/2017",status1:"Complete"},

{name: "Kumar", assigname: "Nitin",module:"UI",desc:"Demo1",sdate:"09/09/2017",edate:"09/10/2017",status1:"Complete"},
{name: "Bindra", assigname: "Shauktik",module:"UI",desc:"Demo1",sdate:"09/09/2017",edate:"09/10/2017",status1:"InComplete"}



];
$scope.tableParams = new NgTableParams({
	
	
 page: 1,            // show first page
      total: $scope.users.length, // length of data
      count: 20,          // count per page
      sorting: {
        name: 'asc'     // initial sorting
      }
	  
	  });
	  
  }]);
  
  
  
  
  
  app.directive('jqdatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'dd/mm/yy',
                onSelect: function (date) {
                    scope.date = date;
                    scope.$apply();
              ngModelCtrl.$setViewValue(date);
                }
            });
        }
    };
});
  
  



// getting data from api
app.controller("CreateModuleApi", ['$scope','$http', function($scope,$http) {
   $http({
			method : 'GET',
			url : '/getAllProfiles'
		}).success(function(data, status, headers, config) {
			$scope.personalDetails = data;
		}).error(function(data, status, headers, config) {
			alert( "failure");
		});
    
        $scope.remove = function(){
            var newDataList=[];
            $scope.selectedAll = false;
            angular.forEach($scope.personalDetails, function(selected){
                if(!selected.selected){
                    newDataList.push(selected);
                }
            }); 
            $scope.personalDetails = newDataList;
        };
     $scope.addNew = function(personalDetail){
            $scope.personalDetails.push({ 
                'uid':$scope.uid,
            'module':$scope.personalDetails[2].module,
            'moduleid':'',
			 'description':''
            });
        };
    
    $scope.checkAll = function () {
        if (!$scope.selectedAll) {
            $scope.selectedAll = true;
        } else {
            $scope.selectedAll = false;
        }
        angular.forEach($scope.personalDetails, function(personalDetail) {
            personalDetail.selected = $scope.selectedAll;
        });
    };    
    
    
}]);




  app.controller("assign", ['$scope','$http', function($scope,$http) {
	  
	  
	    $scope.sizes = [
          "small (12-inch)",
          "medium (14-inch)",
          "large (16-inch)",
          "insane (42-inch)"
      ];
      $scope.toppings = [
        { category: 'meat', name: 'Pepperoni' },
        { category: 'meat', name: 'Sausage' },
        { category: 'meat', name: 'Ground Beef' },
        { category: 'meat', name: 'Bacon' },
        { category: 'veg', name: 'Mushrooms' },
        { category: 'veg', name: 'Onion' },
        { category: 'veg', name: 'Green Pepper' },
        { category: 'veg', name: 'Green Olives' }
      ];
      $scope.selectedToppings = [];
      $scope.printSelectedToppings = function printSelectedToppings() {
        var numberOfToppings = this.selectedToppings.length;

        // If there is more than one topping, we add an 'and'
        // to be gramatically correct. If there are 3+ toppings
        // we also add an oxford comma.
        if (numberOfToppings > 1) {
          var needsOxfordComma = numberOfToppings > 2;
          var lastToppingConjunction = (needsOxfordComma ? ',' : '') + ' and ';
          var lastTopping = lastToppingConjunction +
              this.selectedToppings[this.selectedToppings.length - 1];
          return this.selectedToppings.slice(0, -1).join(', ') + lastTopping;
        }

        return this.selectedToppings.join('');
      };
   
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
$scope.counter = 0;
 $scope.names = ["Daily", "Weekly", "Monthly"];
  $scope.multiple = [2,3,4];
  $scope.user = {
    roles: [3, 5]
  };

   $scope.personalDetails1 = [
        {
            'assignename':'Varun',
			
            'module':'UI',
            'moduleid':'module 1',
			 'startdate':'',
			 'enddate':'',
			 'frequency':'Daily',
			 'users':[{
            "id": 1,
            "name": "Varun",
        }, {
            "id": 3,
            "name": "Neetika",
        }, {
            "id": 5,
            "name": "Rini"
        }],
		"multiple":""
        },
        {
            'assignename':'Varun',
			
            'module':'UI',
            'moduleid':'module 1',
			 'startdate':'',
			 'enddate':'',
			 'frequency':''
        },
        {
            'assignename':'Varun',
			
            'module':'UI',
            'moduleid':'module 1',
			 'startdate':'',
			 'enddate':'',
			 'frequency':''
        }];
    
        $scope.remove = function(){
            var newDataList=[];
            $scope.selectedAll = false;
            angular.forEach($scope.personalDetails1, function(selected){
                if(!selected.selected){
                    newDataList.push(selected);
                }
            }); 
            $scope.personalDetails1 = newDataList;
        };
     $scope.addNew = function(inc){
              $scope.counter += inc;
            $scope.personalDetails1.push({ 
                'assignename' : '',
				
				'module' :'',
                
				'startdate':'',
                 'enddate':'',
				 'frequency':'',
				  'users':[{
            "id": 1,
            "name": "Varun",
        }, {
            "id": 3,
            "name": "Neetika",
        }, {
            "id": 5,
            "name": "Rini"
        }],
		
		"multiple":""
            });
        };
    	$scope.addstatus = function(){		
	//	$scope.personalDetails.push({ 'fname':$scope.fname, 'module': $scope.module, 'moduleid':$scope.moduleid,'description':$scope.description });
		// Writing it to the server
		//	
var dataObj = [{
				assignename:'',
			
            task_name:'',
           
			 start_date:'',
			 end_date:'',
			 frequency:'',
			 participants:[{}],
			 
		multiple:'',
		login_id:''
		}];
      var s=$scope.counter;
      
	  for(var i=$scope.personalDetails1.length-1;i>$scope.personalDetails1.length-1-s;i--)
	  {            if($scope.personalDetails1[i].moduleid!='')
		   dataObj.push( {
				'assignename' : $scope.personalDetails1[i].assignename,
				
				'task_name' :$scope.personalDetails1[i].module,
                
				'start_date':$scope.personalDetails1[i].startdate,
                 'end_date':$scope.personalDetails1[i].enddate,
				 'frequency':$scope.personalDetails1[i].frequency,
				 'participants':$scope.user.roles,
				 'multiple':$scope.personalDetails1[i].multiple,
				 'login_id':$scope.uid
	  })};	
		var res = $http.post('api/v1/assign.php', dataObj);
		res.success(function(data, status, headers, config) {
			$scope.message = data;
alert(data);
		});
		res.error(function(data, status, headers, config) {
			alert( "failure message: " + JSON.stringify({data: data}));
		});		
		// Making the fields empty
		//
		$scope.name='';
		$scope.employees='';
		$scope.headoffice='';
	};
    $scope.checkAll = function () {
        if (!$scope.selectedAll) {
            $scope.selectedAll = true;
        } else {
            $scope.selectedAll = false;
        }
        angular.forEach($scope.personalDetails, function(personalDetail) {
            personalDetail.selected = $scope.selectedAll;
        });
    };    
    
    
}]);



app.controller('showChart', function ($scope) {
             $scope.selectedValue = "Please click on any column above.";
      $scope.events = {
        dataplotclick: function(ev, props) {
          $scope.$apply(function() {
            //create a table if possible to show all data for that person
            $scope.colorValue = "background-color:" + props.categoryLabel + ";";
            $scope.selectedValue = "You clicked on " + props.categoryLabel + "  column!";
          });
        }
      };
      $scope.dataSource = {
        "chart": {
          "caption": "Missed Work",
          "captionFontSize": "30",
          "captionPadding": "25",
          "baseFontSize": "16",
          "canvasBorderAlpha": "0",
          "showPlotBorder": "0",
          "placevaluesInside": "1",
          "valueFontColor": "#ffffff",
          "captionFontBold": "0",
          "bgColor": "#2C3E50",
          "divLineAlpha": "50",
          "plotSpacePercent": "10",
          "bgAlpha": "95",
          "canvasBgAlpha": "0",
          "outCnvBaseFontColor": "#FFFFFF",
          "showValues": "0",
          "baseFont": "Open Sans",
          "paletteColors": "#6495ED, #FF6347, #90EE90, #FFD700, #FF1493",
          "theme": "zune",
          
          // tool-tip customization
          "toolTipBorderColor": "#FFFFFF",
          "toolTipBorderThickness": "1",
          "toolTipBorderRadius": "2",
          "toolTipBgColor": "#000000",
          "toolTipBgAlpha": "70",
          "toolTipPadding": "12",
          "toolTipSepChar": " - ",
          // axis customization
          "xAxisNameFontSize": "18",
          "yAxisNameFontSize": "18",
          "xAxisNamePadding": "10",
          "yAxisNamePadding": "10",
          "xAxisName": "Name",
          "yAxisName": "No of times missed",
          "xAxisNameFontBold": "0",
          "yAxisNameFontBold": "0",
          "showXAxisLine": "1",
          "xAxisLineColor": "#999999",
        },
        "data": [{
          "label": "Varun",
          "value": "1"
        }, {
          "label": "Nitin",
          "value": "2"
        }, {
          "label": "Shauktik",
          "value": "0"
        }, {
          "label": "Bindra",
          "value": "2"
        }, {
          "label": "Manish",
          "value": "4"
        }]
      };
    });



