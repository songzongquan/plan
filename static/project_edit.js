

function ProjectListViewModel(){
	var self = this;
	self.id = ko.observable();
	self.name = ko.observable();
	self.memo = ko.observable();
	self.owner = ko.observable();
	self.updateProject = function(){
		self.update();
	}
	self.update = function(){
		return $.ajax({
			url: '/api/v1/project/'+self.id(),
			contentType:'application/json',
			type:'PUT',
			data:JSON.stringify({
			//	'id':self.id(),
				'name': self.name(),
				'memo': self.memo(),
				'owner': self.owner()
			}),
			success: function(data){
				alert("更新成功");

			},
			error: function(){
				alert("更新失败");
				
			}
		});
	};
	self.load = function(id){

		return $.ajax({
			url: '/api/v1/project/'+id,
			contentType:'application/json',
			type:'GET',
			success: function(data){

				self.id(id);
				self.name(data.name);
				self.memo(data.memo);
				self.owner(data.owner);
			},
			error: function(){
				alert("更新失败");
				
			}
		});
	};
	self.load(id);
}

ko.applyBindings(new ProjectListViewModel());


