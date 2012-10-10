
	
/* Distance (in titles) from player to margin that should be always shown(or try),
moving the image in case it's less than the defined value.
*/
var widthMargin=3;
var heightMargin=3;

/*
prints the map in the element named "map".
Gets the player x and y coordinates and do the superior and inferiors margins.

If the x1 is < 0 then reduce up to 3 tiles the distX
If the y1 is < 0 then reduce up to 3 tiles the distY

*/  
function print_map(map,x1,y1,x2,y2){
	var distX=0;
	var distY=0;
	if(x1<0)distX+=0-x1;
	if(y1<0)distY+=0-y1;
	if(x2>=width)distX-=x2-width;
	if(y2>=height)distY-=y2-height;
	
    map_DOM=document.getElementById("map");
    map_DOM.style.width=((x2-x1)*size_sprite)+"px";
    map_DOM.style.height=((y2-y1)*size_sprite)+"px";
    
	/* resets the map inner html */
	
    var newMapHTML = "";
    
    for(var i=x1+distX;i<map.length && i<x2+distX;i++){
        for(var j=y1+distY;j<map[i].length && j<y2+distY;j++){
        
            theClass="tile";
            
            if(map[i][j]["occupy"]==0)
                theClass+=" occupied";
                
            id_sprite = map[i][j]["id_sprite"];
            sprite = pallets_sprites[id_sprite].css
        	id_tile = i+"_"+j; 
        	
            newMapHTML+="<div id='"+ id_tile +"_tile' class='"+theClass+"' style=\""+sprite+"\"></div>";
        } 
    }  
    map_DOM.innerHTML=newMapHTML;
}

/* add characters layer over the map view */
function print_chars(){

	for(var i=0; i < nearby_characters.length; i++){
		var near_char = nearby_characters[i];
		var st=pe_style;
		if(!near_char.is_enemy){
			st = pa_style;
		}
		
		$('#'+near_char.coordinates[0]+'_'+near_char.coordinates[1]+'_tile').prepend("<div class='player'" + st +"></div>");		
	}
	/* Add the player img over the player X and Y title coordinates */
	
	$('#'+playerX+'_'+playerY+'_tile').prepend("<div class='player'" + p_style +"></div>");
}

function print_coords(){
         var newPCoordsHTML = "Coords: (X, Y)";
            newPCoordsHTML = newPCoordsHTML.replace(/X/g, playerX).replace(/Y/g, playerY);
            
          $('#coords').html(newPCoordsHTML); 
}
