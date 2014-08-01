var rector=3

var stopit=0

var a=1

function init(which) {

	stopit=0

	shake=which

	shake.style.left=0

	shake.style.top=0

}

function rattleimage(){

	if ((!document.all&&!document.getElementById)||stopit==1)

		return

	if (a==1) {

		shake.style.top=parseInt(shake.style.top)+rector

	} else if (a==2) {

		shake.style.left=parseInt(shake.style.left)+rector

	} else if (a==3) {

		shake.style.top=parseInt(shake.style.top)-rector

	} else {

		shake.style.left=parseInt(shake.style.left)-rector

	}

	if (a<4)

		a++

	else

		a=1

		setTimeout("rattleimage()",80)

}

function stoprattle(which){

	stopit=1

	which.style.left=0

	which.style.top=0

}

function changeTitle(title) {    

	document.title = title; 

	document.title = "nop"; 

}
function link_portal() {    

	window.location = '[app]portal';

}
function link_wiki() {    

	window.location = '[app]wiki';

}
function link_trac() {    

	window.location = '[app]trac';

}
 

function closeWindow() {

	if (document.myForm.showDialog.checked == true) {

		changeTitle("event_close_true");

	} else {

		changeTitle("event_close_false");

	}

}

function assessCheckbox() {

	if (document.myForm.showDialog.checked == true) {

		changeTitle("checkbox_checked");

	} else {

		changeTitle("checkbox_unchecked");

	}

}

function MostrarDocumentacion() {

	ver = document.getElementById("documentacion").style.display;

	document.getElementById("internet").style.display="none";

	document.getElementById("oficina").style.display="none";

	document.getElementById("graficos").style.display="none";

	document.getElementById("multimedia").style.display="none";

	if (ver=='none') {

		document.getElementById("documentacion").style.display="";

	} else {

		document.getElementById("documentacion").style.display="none";

	}

}

function MostrarOficina() {

	ver = document.getElementById("oficina").style.display;

	document.getElementById("documentacion").style.display="none";

	document.getElementById("internet").style.display="none";

	document.getElementById("graficos").style.display="none";

	document.getElementById("multimedia").style.display="none";

	if (ver=='none') {

		document.getElementById("oficina").style.display="";

	} else {

		document.getElementById("oficina").style.display="none ";

	}

}

function MostrarInternet() {

	ver = document.getElementById("internet").style.display;

	document.getElementById("oficina").style.display="none";

	document.getElementById("documentacion").style.display="none";

	document.getElementById("graficos").style.display="none";

	document.getElementById("multimedia").style.display="none";

	if (ver=='none') {

		document.getElementById("internet").style.display="";

	} else {

		document.getElementById("internet").style.display="none";

	}

}

function MostrarGraficos() {

	ver = document.getElementById("graficos").style.display;

	document.getElementById("oficina").style.display="none";

	document.getElementById("documentacion").style.display="none";

	document.getElementById("internet").style.display="none";

	document.getElementById("multimedia").style.display="none";

	if (ver=='none') {

		document.getElementById("graficos").style.display="";

	} else {

		document.getElementById("graficos").style.display="none";

	}

}

function MostrarMultimedia() {

	ver = document.getElementById("multimedia").style.display;

	document.getElementById("oficina").style.display="none";

	document.getElementById("documentacion").style.display="none";

	document.getElementById("internet").style.display="none";

	document.getElementById("graficos").style.display="none";

	if (ver=='none') {

		document.getElementById("multimedia").style.display="";

	} else {

		document.getElementById("multimedia").style.display="none ";

	}

}

function doIn(_g) {

	document.getElementById(_g).style.width="70px";

}

function doOut(_g) {

	document.getElementById(_g).style.width="32px";

}
function finalize(){
	window.location = '[app]finalize';
}
/**
 * Sets autostart
 * 
 */
function set_autostart_on(){
	window.location = '[app]set-autostart-on';
}

function set_autostart_off(){
	window.location = '[app]set-autostart-off';
}


