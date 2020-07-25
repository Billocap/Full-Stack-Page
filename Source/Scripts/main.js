function $( query_ ) {
    return document.querySelector( query_ );
}

function update(id_){
    $(".active").className = "";
    $("#"+id_).className = "active";
    
    var xhttp = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");

    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            $("#content").innerHTML = this.responseText;
        }
    }
    xhttp.open('GET',id_+'.html');
    xhttp.send();
}

update("home");