

function ProjectListViewModel(){
	var self = this;
	self.id = ko.observable();
	self.name = ko.observable();
	self.memo = ko.observable();
	self.owner = ko.observable();
	self.addProject = function(){
		self.save();
		self.id('');
		self.name("");
		self.memo("");
		self.owner("");
	};

	self.save = function(){
		return $.ajax({
			url: '/api/v1/project',
			contentType:'application/json',
			type:'POST',
			data:JSON.stringify({
				'id':self.id(),
				'name': self.name(),
				'memo': self.memo(),
				'owner': self.owner()
			}),
			success: function(data){
				alert("添加成功");

			},
			error: function(){
				alert("添加失败");
				
			}
		});
	};
}

ko.applyBindings(new ProjectListViewModel());


