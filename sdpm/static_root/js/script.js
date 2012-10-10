

function loadPage(){
	var map=new Array();
	for(var i=0;i<10;i++){
		map[i]=new Array();
		for(var j=0;j<10;j++){
			map[i][j]=new Object();
			map[i][j]["occupy"] = Math.floor(Math.random()*2);  
			map[i][j]["id_tile_type"] = "#";
		}
	}
	
	imp(map,0,0,9,9);
}
function imp(map,x1,y1,x2,y2){
	map_DOM=document.getElementById("map");
	map_DOM.style.width=((x2-x1)*50)+"px";
	map_DOM.style.height=((y2-y1)*50)+"px";/**/
	for(var i=x1;i<map.length && i<x2;i++){
		for(var j=y1;j<map[i].length && j<y2;j++){
			theClass="tile";
			if(map[i][j]["occupy"]==1)
				theClass+=" occupied";
				map_DOM.innerHTML+="<div class='"+theClass+"'><img src="+map[i][j]["id_tile_type"]+"></div>"
			//alert(map[i][j]["occupy"] + " , " + map[i][j]["id_tile_type"]);
		} 
	}  
}
