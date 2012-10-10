
		<div id="interactions_list">	
			<h3>Interactions: </h3>
			<ul>
				{% for other, interactions in character.get_interactions %}				
					<li>
						{{other.name}}
						<ul>
							{% for interaction_type, interaction_name in interactions %}
								{% if interaction_type == 1 %}
									<li><a href="{% url fight rpg.id other.id %}">{{interaction_name}}</a></li>
								{% else %}
									<li><a href="#{{interaction_type}}">{{interaction_name}}</a></li>
								{% endif %}
							{% endfor %}	
						</ul>
					</li>				
				{% endfor %}
			</ul>
		</div>		

		
var interactions_vect=new Array();

/* Prints the interactions list */
function print_interactions(){
    var interactions_div =  $('#interactions_list'); 
	var html = '<h3>Interactions: </h3>';
	html += '<ul>';
	for(var i =0; i< interactions_vect.length; i++){
		html += '<li>';
		
		html += '</li>';		
	}
	
}

							{% for interaction_type, interaction_name in interactions %}
								{% if interaction_type == 1 %}
									<li><a href="{% url fight rpg.id other.id %}">{{interaction_name}}</a></li>
								{% else %}
									<li><a href="#{{interaction_type}}">{{interaction_name}}</a></li>
								{% endif %}
							{% endfor %}	
							
var it_base_url = {% url fight rpg.id 0 %};
it_base_url = it_base_url.replace(it_base_url.substr(it_base_url.lastIndexOf('/') + 1), '');

/* Prints an interaction list of possible actions */
function print_interaction_sub_list(interaction){
	var html = interaction[0].name;
	html += '<ul>';
	var it_list = interaction[1];
	for(var i =0; i< it_list.length; i++){
		html += '<li>';
			html +='<a href="' + rpg_base_url;
				if(it_list.interaction_type == 1){
					html+= 'fight/'
					html+= interaction[0].id + '/';
				}
				else{
					html+= '#';				
				}
			html +='">';
			
			html += it_list.interaction_name + '</a>';
		html += '</li>';		
	}
	
}