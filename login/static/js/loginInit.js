$(function(){
	$(".toggle-master").click(toggleMaster);
	$(".toggle-slave").click(toggleSlave);
	$(".editButton").click(function(){
		$(".unameTittle").html($(this).attr("uname"));
		$(".emailField").val($("td[class='"+$(this).attr("uname")+"']").html());
		$("#modalEdit").modal("show");}
	);
	$(".editform").submit(function(e){
		e.preventDefault();
		$("#modalEdit").modal("hide");
		editData($(".unameTittle").html(), $(".emailField").val());
	});

	$(".del-button").click(deleteData);
});