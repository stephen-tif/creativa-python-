$(document).ready( ()=> {
    $('#tpersonajes').DataTable();

    $(document).on('click','#btnFind',()=>{
        var nombre = $('#txtNombre').val();
        window.location.href = "/personajeByName/"+nombre;
    });

} );