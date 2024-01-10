// Call the dataTables jQuery plugin

$(document).ready(function() {
  cargarUsuarios();
  $('#usuarios').DataTable();
});

function getHeaders(){
  return {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': localStorage.token
  }

}

async function cargarUsuarios(id) {

  const request = await fetch('api/usuarios', {
    method: 'GET',
    headers:
      getHeaders()
    ,
    //  body: JSON.stringify({a: 1, b: 'Textual content'})
  });
  const usuarios = await request.json();
  let listadoUsuariosHtml = '';
  for (let usuario of usuarios) {
    let botonEliminar = '<a href="#" onclick="eliminarUsuario('+usuario.id+')" class="btn btn-danger btn-circle btn-sm"><i class="fas fa-trash"></i></a>';

    let telefonoTexto = usuario.telefono == null ? '-' :usuario.telefono;

    let usuarioHtml = '<tr> <td class="sorting_1">'+usuario.id+'</td>' +
        '<td>'+usuario.nombre+' '+usuario.apellido+'</td>' +
        '<td>'+usuario.email+'</td>' +
        ' <td>'+ telefonoTexto +'</td>' +
        '<td>'+  botonEliminar +'</td>'+
        '</tr>';
    listadoUsuariosHtml += usuarioHtml;
  }

   document.querySelector('#usuarios tbody').outerHTML = listadoUsuariosHtml;

  console.log(usuarios);

}

async function eliminarUsuario(id){

  if(!confirm('Desea eliminar este usuario?')) {
    return;
  }
  const request = await fetch('api/usuario/delete/'+id, {
    method: 'DELETE',
    headers: getHeaders()
    ,
  });
  location.reload();
}