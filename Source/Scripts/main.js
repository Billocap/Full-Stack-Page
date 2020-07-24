function $( query_ ) {
    return document.querySelector( query_ );
}

function update(id_){
    $(".active").className = "";
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            $("#content").innerHTML = this.responseText;
        }
    }
    xhttp.open('GET',id_);
    xhttp.send();

    $("#"+id_).className = "active";
}

update("home");