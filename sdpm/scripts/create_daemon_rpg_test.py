from django.conf import settings
from rpgs.models import RPG
from rpgs.core.rules.models import Rules
from rpgs.accounts.models import Creator
from rpgs.characters.models import *
from rpgs.characters.controllers.controller import Controller
from rpgs.maps.models import *
from rpgs.maps.tiles.models import *
from rpgs.bases.daemon.daemonCreator import DaemonCreator
from rpgs.maps.generator.basic_generator import MapGenerator
from os.path import join
from shutil import copyfile

def run():
    try:
        rpg = RPG.objects.get(pk=1)
        rules = Rules.objects.get(pk=1)
        rpg.delete()
        rules.delete()
    except:
        pass

    rpg_name ='RPG Daemon'
    creator = DaemonCreator()
    rpg = creator.create(rpg_name)
    rpg.description = "A nice rpg."
    c = Creator(rpg=rpg)
    c.user_id = 2
    c.save()
    
    pallet = Pallet(name="default",image='sprites/def_test_32.png',width=96,height=96,rpg=rpg)
    pallet.save()
    map_generator = MapGenerator(rpg)
    map_generator.generate()
    #wm = WorldMap(name="nome",rpg=rpg)
    #wm.save()
    #zn = wm.zones.create(name="zone", areaSize=9)
    #area = zn.areas.create(name="area")
    for area in Zone.objects.get(pk=1).areas.all():          
        for x,y in area.coordinatesMatrix:
            id_sprite = (x+y + (x*y -1) + (x+1)%(y+1) )%8
            id_sprite = 5 if id_sprite == 2 else id_sprite
            id_sprite = 1 if id_sprite != 5 and id_sprite %2 !=0 else id_sprite
            area.coordinatesMatrix[x,y]['id_sprite'] = id_sprite
            if id_sprite == 5:
                area.coordinatesMatrix[x,y]['occupy'] = 0
            
        area.save()
    
    h = Character.objects.get(pk=1)
    h.main_area = area
    h.area = area
    h.coordinates = [4,4]
    h.active=True
    h.player_id = 1
    h.save()
    h2 = Character.objects.get(pk=2)
    h2.main_area = area
    h2.area = area
    h2.coordinates = [3,3]
    h2.active=True
    h2.save()
    c = Controller()
    c.add_character(h)
