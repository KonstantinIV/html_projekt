function myFunction() {
    
    var userID = $('#userID').val();
    var passID =  $('#passID').val();
    
    $.ajax({
        url: "get_graph.php",
        type: "POST",
        data:{postUserID: userID, postPassID:passID},
        success:function(data){
            window.alert(data);
            image(data);
        }
    })

}
function image(thisImg) {
    var img = document.createElement("IMG");
    img.src = thisImg;
    document.getElementById('Graafik').appendChild(img);
}
