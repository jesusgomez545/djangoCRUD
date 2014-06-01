function editData(u, e)
{
	$.ajax({
		type: 'POST',
		url: '/edit',
		data: {
		'u': u,
		'e': e,
		csrfmiddlewaretoken:  document.getElementsByName('csrfmiddlewaretoken')[0].value,},
		success: function() {
			$("td[class='"+u+"']").html(e);
			$(".msgtext").html("Datos actualizados exitosamente");
			$("#modalMsg").modal("show");
		},
		error: function(xhr, textStatus, errorThrown) {
			alert('Please report this error: '+errorThrown+xhr.status+xhr.responseText);
		}
	});
}

function deleteData()
{
	var t = []
	var u = $(".toggle-slave:checked").each(function(){t.push(this.id);})
	if(t.length>0){
		$.ajax({
			type: 'POST',
			url: '/delete',
			data:{
			't':t.join(),
			csrfmiddlewaretoken:  document.getElementsByName('csrfmiddlewaretoken')[0].value,},
			success: function() {
				window.location.replace("/home");
			},
			error: function(xhr, textStatus, errorThrown) {
				alert('Please report this error: '+errorThrown+xhr.status+xhr.responseText);
			}
		});
	}
}