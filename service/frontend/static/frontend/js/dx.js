function $$(id){return document.getElementById(id);}
function Wnew(len){
	for(var ui=1; ui<=len; ui++){
		var playbox=$$("play_"+ui)
		var ulbox=$$("vlink_"+ui),litag=ulbox.getElementsByTagName('li'),isno2,rhtml;
		rhtml="";
		if(litag.length>25){playbox.className="play-box";}else{playbox.className="play-box";}
		for(var uii=litag.length-1;uii>=0;uii--){
			if(uii==litag.length-1){isno2='<li>';}else{isno2='<li>';}
			rhtml+=isno2+litag[uii].innerHTML+"</li>";
		}
		rhtml="<ul>"+rhtml+"</ul>";
		ulbox.innerHTML=rhtml;
	}
}