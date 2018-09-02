
function Project(data){
	this.id = ko.observable(data.id);
	this.name = ko.observable(data.name);
	this.memo = ko.observable(data.memo);
	this.owner = ko.observable(data.owner);
}

function ProjectListViewModel(){
	var self = this;

	self.project_list = ko.observableArray([]);

        self.refresh = function(){

		$.getJSON('/api/v1/projects',function(projectModels){
		//	console.log(projectModels);
			var t = $.map(projectModels,function(item){
				return new Project(item);
			});
		self.project_list(t);
		});
	};
	self.refresh();

	self.removeProject =  function(project){
		console.log(project);
		var id = project.id();
		return $.ajax({

			url: '/api/v1/project/'+id,
			contentType:'application/json',
			type:'DELETE',
			success: function(data){
				alert("删除成功");

                                self.refresh();
			},
			error: function(){
				alert("删除失败");
				
			}
		});
	};
	self.goAdd = function(){
		document.location="/add_project";
	};
	self.updateProject = function(project){
		document.location="/edit_project?id="+project.id();
	};

}


ko.applyBindings(new ProjectListViewModel());
