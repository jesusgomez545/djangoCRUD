function toggleSlave()
{
	$(".toggle-master").prop("checked",($(".toggle-slave:checked").length == $("input[type=checkbox][class!='toggle-master']").length));
}

function toggleMaster () 
{
	var master = this.checked;
	$(".toggle-slave").each(function(){ this.checked = master});
}