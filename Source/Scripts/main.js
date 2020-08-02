//JQuery like query function;
function $( query_ ) {
    return document.querySelector( query_ );
}

//AJAX Function.
function update(id_){
    //Resets the current selected tab;
    $(".active").className = "";
    $("#"+id_).className = "active";
    
    //Creates the request object according to Web Browser;
    var xhttp = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");

    //Update the page content;
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            $("#content").innerHTML = this.responseText;
        }
    }
    //Builds and sends the request;
    xhttp.open('GET',id_+'.html');
    xhttp.send();
}

//Starts the page in the home info;
update("home");