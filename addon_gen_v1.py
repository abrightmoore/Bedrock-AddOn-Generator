#  @TheWorldFoundry
_VERSION = "0.0.1"

#  Instructions:
SEED = 23846237894  #  CHANGE THIS VALUE FOR UNIQUE UUIDs AND TEXTURES

'''
    PURPOSE:
    Read the text key value file for a Minecraft add-on, and then create stubs for all the things
    that are defined in it.

    DevLog: https://peoplemaking.games/@TheWorldFoundry/111762017474772111
'''

import os
import json
import pygame
import random
import shutil
from math import floor, sqrt

class AddOn:
    
    class Tools:
        def __init__(self):
            pass
            
        def makedir(self, path):
            if not os.path.exists(path):
                os.makedirs(path)
        
        def clean_string(self, val):
            return val.replace(":","_").replace(" ","_")
            
        def write_json(self, path, file, data):
            with open(os.path.join(path, file), "w") as outfile:
                json.dump(data, outfile, indent=4, sort_keys=True)

        def write_image(self, path, file, image):
            pygame.image.save(image, os.path.join(path, file))

        def make_uuid(self, R):
            digits = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
            
            result = ""
            for i in range(0,32):
                result += digits[R.randint(0,len(digits)-1)]
                if len(result) == 8 or len(result) == 13 or len(result) ==  18 or len(result) == 23:
                    result += "-"
            return result

    tools = Tools()

    class Texture:
        library_tex = {}
    
        spawn_egg_mask = [
            "0000000000000000",
            "0000000000000000",
            "0000000##0000000",
            "00000##11##00000",
            "0000#111111#0000",
            "0000#111111#0000",
            "000#11111111#000",
            "000#11111111#000",
            "00#1111111111#00",
            "00#1111111111#00",
            "00#1111111111#00",
            "000#11111111#000",
            "000##111111##000",
            "00000#1111#00000",
            "000000####000000",
            "0000000000000000"
        ]
    
        item_mask = [    #  via https://kirilllive.github.io/ASCII_Art_Paint/ascii_paint.html
            "0000000000000000",
            "0000########0000",
            "000#111111111#00",
            "0000######1111#0",
            "000000000#1111#0",
            "00000000#11##1#0",
            "0000000#11#0#1#0",
            "000000#11#00#1#0",
            "00000#11#000#1#0",
            "0000#11#0000#1#0",
            "000#11#00000#1#0",
            "00#11#000000#1#0",
            "0#11#00000000#00",
            "0###000000000000",
            "0000000000000000",
            "0000000000000000"
        ]
    
        palette0 = [
            (254, 254, 254),         # "wool_colored_white.png": 
            (157, 157, 151),        # "wool_colored_silver.png", 
            (71, 79, 82),           # "wool_colored_gray.png", 
            (37, 37, 41),           # "wool_colored_black.png", 
            (131, 84, 50),          # "wool_colored_brown.png", 
            (214, 96, 209),         # "wool_colored_magenta.png", 
            (244, 178, 201),        # "wool_colored_pink.png", 
            (184, 52, 44),          # "wool_colored_red.png", 
            (249, 147, 43),         # "wool_colored_orange.png", 
            (254, 217, 63),         # "wool_colored_yellow.png", 
            (134, 204, 38),         # "wool_colored_lime.png", 
            (101, 134, 36),         # "wool_colored_green.png", 
            (62, 77, 178),          # "wool_colored_blue.png", 
            (78, 197, 231),         # "wool_colored_light_blue.png", 
            (22, 155, 156),         # "wool_colored_cyan.png", 
            (151, 67, 205),         # "wool_colored_purple.png", 
        ]

        palette1 = [
            (37, 37, 41),           # "wool_colored_black.png", 
            (131, 84, 50),          # "wool_colored_brown.png", 
            (184, 52, 44),          # "wool_colored_red.png", 
            (249, 147, 43),         # "wool_colored_orange.png", 
            (254, 217, 63),         # "wool_colored_yellow.png", 
            (254, 254, 254),         # "wool_colored_white.png": 
            (254, 254, 254),         # "wool_colored_white.png": 
            (254, 254, 254),         # "wool_colored_white.png": 
            (254, 254, 254),         # "wool_colored_white.png": 
            (254, 217, 63),         # "wool_colored_yellow.png", 
            (249, 147, 43),         # "wool_colored_orange.png", 
            (184, 52, 44),          # "wool_colored_red.png", 
            (131, 84, 50),          # "wool_colored_brown.png", 
            (37, 37, 41),           # "wool_colored_black.png", 
    #        (157, 157, 151),        # "wool_colored_silver.png", 
    #        (71, 79, 82),           # "wool_colored_gray.png", 
    #        (214, 96, 209),         # "wool_colored_magenta.png", 
    #        (244, 178, 201),        # "wool_colored_pink.png", 
    #        (134, 204, 38),         # "wool_colored_lime.png", 
    #        (101, 134, 36),         # "wool_colored_green.png", 
    #        (62, 77, 178),          # "wool_colored_blue.png", 
    #        (78, 197, 231),         # "wool_colored_light_blue.png", 
    #        (22, 155, 156),         # "wool_colored_cyan.png", 
    #        (151, 67, 205),         # "wool_colored_purple.png", 
        ]

        palette2 = [
            (249, 147, 43),         # "wool_colored_orange.png", 
            (254, 217, 63),         # "wool_colored_yellow.png", 
            (254, 254, 254),         # "wool_colored_white.png": 
            (254, 254, 254),         # "wool_colored_white.png": 
            (184, 52, 44),          # "wool_colored_red.png", 
            (131, 84, 50),          # "wool_colored_brown.png", 
            (37, 37, 41),           # "wool_colored_black.png", 
        ]

        palette3 = [
            (37, 37, 41),           # "wool_colored_black.png", 
            (71, 79, 82),           # "wool_colored_gray.png", 
            (157, 157, 151),        # "wool_colored_silver.png", 
            (254, 254, 254),         # "wool_colored_white.png": 
            (254, 254, 254),         # "wool_colored_white.png": 
            (134, 204, 38),         # "wool_colored_lime.png", 
            (101, 134, 36),         # "wool_colored_green.png", 
            (37, 37, 41),           # "wool_colored_black.png", 
        ]
    
        def __init__(self, width, height, R):
            self.R = R
            self.image = pygame.Surface((width,height), pygame.SRCALPHA)

            palettes = [self.palette0, self.palette1, self.palette2, self.palette3]
            # Random palette
            self.palette = palettes[self.R.randint(0,len(palettes)-1)]    

            self.colours = []
            num_col = self.R.randint(2,len(self.palette))
            for i in range(0, num_col):
                self.colours.append( self.palette[ self.R.randint(0, len(self.palette)-1)])

            self.make_pattern_modulo(self.R)

        def apply_mask(self, mask):
            for y in range(0, self.image.get_height()):
                for x in range(0, self.image.get_width()):
                    if mask[y][x] == '0':
                        self.image.set_at((x,y), (0,0,0,0))
                    elif mask[y][x] == "#":
                        r,g,b,a = self.image.get_at((x,y))
                        self.image.set_at((x,y), (r>>1,g>>1,b>>1,a))
        
        def make_pattern_modulo(self,R):
            width = self.image.get_width()
            height = self.image.get_height()

            modulo = R.randint(2,11)
            style = R.randint(0,2)
            
            attempts = 100
            keep_going = True
            while attempts > 0 and keep_going:
                attempts -= 1
                key_pattern = (modulo, style, len(self.palette))
                if key_pattern not in self.library_tex:
                    keep_going = False
                    self.library_tex[key_pattern] = key_pattern
            
            for y in range(0, height):
                for x in range(0, width):
                    val = 0
                    if style == 0:
                        val = (x*y)%modulo
                    if style == 1:
                        val = (x+y)%modulo
                    if style == 2:
                        val = (x**y)%modulo
                                        
                    col = self.palette[val%len(self.palette)]
                    self.image.set_at((x,y), col)
            
            

    class Tile:
        def __init__(self, id, name):
            self.id = id
            self.id_cleaned = AddOn.tools.clean_string(self.id)
            self.name = name
            
        def render_to_files(self,R):
            #  Create the addon files and return them in a dictionary keyed off the filenames.
            
            tile_bp = {
                "format_version": "1.20.20",
                "minecraft:block": {
                    "description": {
                        "identifier": self.id,  #  "myname:sample_block",
                        "menu_category": {
                            "category": "construction",
                            "group": "itemGroup.name.wool"
                        }
                    },
                    "components": {
                        "minecraft:collision_box": True,
                        "minecraft:selection_box": True,
                        "minecraft:destructible_by_mining": {
                            "seconds_to_destroy": 1
                        },
                        "minecraft:destructible_by_explosion": {
                            "explosion_resistance": 30
                        },
                        "minecraft:flammable": {
                            "destroy_chance_modifier": 20,
                            "catch_chance_modifier": 5
                        },
                        "minecraft:geometry": "geometry."+self.id_cleaned, #  sample_block",
                        "minecraft:material_instances": {
                            "*": {
                                "texture": self.id_cleaned+"_t_tex",  #  "sample_block",
                                "render_method": "alpha_test"
                            }
                        },
                        "minecraft:map_color": "#ff00fd"
                    }
                }
            }
            tile_tex = AddOn.Texture(16,16,R).image
            #  rp/models/blocks
            tile_model = {
                "format_version": "1.19.0",
                "minecraft:geometry": [
                    {
                        "description": {
                            "identifier": "geometry."+self.id_cleaned, #  sample_block",
                            "texture_width": 16,
                            "texture_height": 16,
                            "visible_bounds_width": 2,
                            "visible_bounds_height": 2.5,
                            "visible_bounds_offset": [0, 0.75, 0]
                        },
                        "bones": [
                            {
                                "name": "block",
                                "pivot": [0, 0, 0],
                                "cubes": [
                                    {
                                        "origin": [-8, 0, -8],
                                        "size": [16, 16, 16],
                                        "uv": {
                                            "north": {
                                                "uv": [0, 0],
                                                "uv_size": [16, 16]
                                            },
                                            "east": {
                                                "uv": [0, 0],
                                                "uv_size": [16, 16]
                                            },
                                            "south": {
                                                "uv": [0, 0],
                                                "uv_size": [16, 16]
                                            },
                                            "west": {
                                                "uv": [0, 0],
                                                "uv_size": [16, 16]
                                            },
                                            "up": {
                                                "uv": [16, 16],
                                                "uv_size": [-16, -16]
                                            },
                                            "down": {
                                                "uv": [16, 16],
                                                "uv_size": [-16, -16]
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
            return {
                "model" : tile_model,
                "behavior" : tile_bp,
                "texture" : tile_tex
            }
            
    class Entity:
        def __init__(self, id, name):
            self.id = id
            self.id_cleaned = AddOn.tools.clean_string(self.id)
            self.name = name

        def render_to_files(self,R):
            #  Create the addon files and return them in a dictionary keyed off the filenames.
            
            entity_rp = {
                "format_version": "1.10.0",
                "minecraft:client_entity": {
                    "description": {
                        "identifier": self.id,  #  "myname:sample_entity",
                        "materials": {
                            "default": "entity_alphatest"
                        },
                        "textures": {
                            "default": "textures/entities/"+self.id_cleaned+"_tex",  #  sample_entity"
                        },
                        "geometry": {
                            "default": "geometry."+self.id_cleaned,  #  sample_entity"
                        },
                        "render_controllers": ["controller.render.default"],
                        "spawn_egg": {
                            "texture": self.id_cleaned+"_spawn_egg_tex"  #  "sample_entity_spawn_egg"
                        }
                    }
                }
            }
            entity_bp = {
                "format_version": "1.16.100",
                "minecraft:entity": {
                    "description": {
                        "identifier": self.id,  #  "myname:sample_entity",
                        "is_spawnable": True,
                        "is_summonable": True,
                        "is_experimental": False
                    },
                    "components": {
                        "minecraft:physics": {
                            "has_gravity": True,
                            "has_collision": True
                        },
                        "minecraft:pushable": {
                            "is_pushable": False
                        },
                        "minecraft:push_through": {
                            "value": 1
                        }
                    }
                }
            }
            entity_tex = AddOn.Texture(16,16,R)
            entity_spawn_egg_tex = AddOn.Texture(16,16,R)
            entity_spawn_egg_tex.image.blit(entity_tex.image, [0,0])  # Copy the entity pattern and colours
            entity_spawn_egg_tex.apply_mask(entity_spawn_egg_tex.spawn_egg_mask)
            entity_spawn_egg_tex = entity_spawn_egg_tex.image
            entity_tex = entity_tex.image
            entity_model = [
                {
                "format_version": "1.12.0",
                "minecraft:geometry": [
                    {
                        "description": {
                            "identifier": "geometry."+self.id_cleaned,
                            "texture_width": 16,
                            "texture_height": 16,
                            "visible_bounds_width": 2,
                            "visible_bounds_height": 1.5,
                            "visible_bounds_offset": [0, 0.25, 0]
                        },
                        "bones": [
                            {
                                "name": "root",
                                "pivot": [0, 0, 0]
                            },
                            {
                                "name": "right",
                                "parent": "root",
                                "pivot": [0, 0, 0],
                                "rotation": [0, 0, -45],
                                "cubes": [
                                    {"origin": [-0.25, 1, 0], "size": [0.25, 4, 4], "uv": [0, 0]},
                                    {"origin": [-0.25, 0, -6], "size": [0.25, 7, 6], "uv": [0, 0]},
                                    {"origin": [-0.25, 1, 4], "size": [0.25, 1, 4], "uv": [0, 0]}
                                ]
                            },
                            {
                                "name": "left",
                                "parent": "root",
                                "pivot": [0, 0, 0],
                                "rotation": [0, 0, 45],
                                "cubes": [
                                    {"origin": [0, 1, 0], "size": [0.25, 4, 4], "uv": [0, 0], "mirror": True},
                                    {"origin": [0, 0, -6], "size": [0.25, 7, 6], "uv": [0, 0], "mirror": True},
                                    {"origin": [0, 1, 4], "size": [0.25, 1, 4], "uv": [0, 0], "mirror": True}
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "format_version": "1.12.0",
                "minecraft:geometry": [
                    {
                        "description": {
                            "identifier": "geometry."+self.id_cleaned,
                            "texture_width": 16,
                            "texture_height": 16,
                            "visible_bounds_width": 3,
                            "visible_bounds_height": 2.5,
                            "visible_bounds_offset": [0, 0.75, 0]
                        },
                        "bones": [
                            {
                                "name": "root",
                                "pivot": [0, 0, 0]
                            },
                            {
                                "name": "right",
                                "parent": "root",
                                "pivot": [0, 0, 0],
                                "rotation": [0, 0, -45],
                                "cubes": [
                                    {"origin": [-0.25, 1, 0], "size": [0.25, 13, 3], "uv": [0, 0]},
                                    {"origin": [-0.25, 0, -4], "size": [0.25, 15, 3], "uv": [0, 0]}
                                ]
                            },
                            {
                                "name": "left",
                                "parent": "root",
                                "pivot": [0, 0, 0],
                                "rotation": [0, 0, 45],
                                "cubes": [
                                    {"origin": [0, 1, 0], "size": [0.25, 13, 3], "uv": [0, 0], "mirror": True},
                                    {"origin": [0, 0, -4], "size": [0.25, 15, 3], "uv": [0, 0], "mirror": True}
                                ]
                            },
                            {
                                "name": "body",
                                "parent": "root",
                                "pivot": [0, 0, 0],
                                "cubes": [
                                    {"origin": [-2, 0, -8], "size": [4, 2, 2], "uv": [0, 0]},
                                    {"origin": [-1, 0, -6], "size": [2, 1, 19], "uv": [0, 0]}
                                ]
                            }
                        ]
                    }
                ]
            }
            
            ]
            entity_model = entity_model[(ord(self.id[-1]) & 0x01)%len(entity_model)]  #  Variety - pick a model for display
            
            
            '''
            {
                "format_version": "1.12.0",
                "minecraft:geometry": [
                    {
                        "description": {
                            "identifier": "geometry."+self.id_cleaned,  #  sample_entity",
                            "texture_width": 64,
                            "texture_height": 64,
                            "visible_bounds_width": 2,
                            "visible_bounds_height": 1.5,
                            "visible_bounds_offset": [0, 0.25, 0]
                        },
                        "bones": [
                            {
                                "name": "root",
                                "pivot": [0, 0, 0],
                                "cubes": [
                                    {
                                        "origin": [-6, 0, -6],
                                        "size": [12, 8, 12],
                                        "uv": [0, 0]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
            '''
            
            return {
                "model" : entity_model,
                "behavior" : entity_bp,
                "resource" : entity_rp,
                "texture" : entity_tex,
                "texture spawn egg" : entity_spawn_egg_tex

            }
    
    class Item:
        def __init__(self, id, name):
            self.id = id
            self.id_cleaned = AddOn.tools.clean_string(self.id)
            self.name = name

        def render_to_files(self, R):
            #  Create the addon files and return them in a dictionary keyed off the filenames.
            
            item_2d_bp = {
                "format_version": "1.20.30",
                "minecraft:item": {
                    "description": {
                        "identifier": self.id,  #  "myname:sample_2d_item",
                        "menu_category": {
                            "category": "equipment"
                        }
                    },
                    "components": {
                        "minecraft:max_stack_size": 64,
                        "minecraft:icon": {
                            "texture": self.id_cleaned+"_i_tex"  #  "sample_2d_item"
                        }
                    }
                }
            }
            item_3d_bp = {
                        "format_version": "1.20.30",
                        "minecraft:item": {
                            "description": {
                                "identifier": self.id,  #  "myname:sample_item",
                                "menu_category": {
                                    "category": "equipment",
                                    "group": "itemGroup.name.sword"
                                }
                            },
                            "components": {
                                "minecraft:max_stack_size": 64,
                                "minecraft:icon": {
                                    "texture": "item_"+self.id_cleaned+"_tex"  #  "sample_item"
                                }
                            }
                        }
                    }
            # rp/animations/attachable
            item_animation = {
                "format_version": "1.8.0",
                "animations": {
                    "animation."+self.id_cleaned+".first_person_hold": {
                        "loop": True,
                        "bones": {
                            "root_item": {
                                "rotation": [90, 56, -32],
                                "position": [9, 18, 5]
                            }
                        }
                    },
                    "animation."+self.id_cleaned+".third_person_hold": {
                        "loop": True,
                        "bones": {
                            "root_item": {
                                "rotation": [25, 0, 0],
                                "position": [0.5, 19, -2.5],
                                "scale": 0.85
                            }
                        }
                    }
                }
            }
            # rp/attachables
            item_attachable = {
                "format_version": "1.10.0",
                "minecraft:attachable": {
                    "description": {
                        "identifier": self.id,  #  "myname:sample_item",
                        "render_controllers": ["controller.render.item_default"],
                        "materials": {
                            "default": "entity_alphatest",
                            "enchanted": "entity_alphatest_glint"
                        },
                        "textures": {
                            "default": "textures/entities/attachable/"+self.id_cleaned+"_tex",  #  sample_item",
                            "enchanted": "textures/misc/enchanted_item_glint"
                        },
                        "geometry": {
                            "default": "geometry."+self.id_cleaned  #  sample_item"
                        },
                        "animations": {
                            "first_person_hold": "animation."+self.id_cleaned+".first_person_hold",
                            "third_person_hold": "animation."+self.id_cleaned+".third_person_hold"
                        },
                        "scripts": {
                            "animate": [
                                {
                                    "first_person_hold": "c.is_first_person"
                                },
                                {
                                    "third_person_hold": "!c.is_first_person"
                                }
                            ]
                        }
                    }
                }
            }
            
            # rp/model/entity/attachable
            item_model = { 
                            "format_version": "1.19.0",
                            "minecraft:geometry": [
                                {
                                    "description": {
                                        "identifier": "geometry."+self.id_cleaned,  #  sample_item",
                                        "texture_width": 16,
                                        "texture_height": 16
                                    },
                                    "bones": [
                                        {
                                            "name": "root_item",
                                            "pivot": [0, 0, 0],
                                            "binding": "q.item_slot_to_bone_name(c.item_slot)",
                                            "cubes": [
                                                {
                                                    "origin": [-2.5, 0, -1.5],
                                                    "size": [5, 11, 3],
                                                    "uv": [0, 0]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
            item_tex = AddOn.Texture(16, 16, R)
            item_attachable_tex = AddOn.Texture(16,16, R)
            item_attachable_tex.image.blit(item_tex.image, [0,0])  #  Same same
            item_tex.apply_mask(item_tex.item_mask)
            item_tex = item_tex.image
            item_attachable_tex = item_attachable_tex.image
            
            item_recipe = {
                "format_version": "1.13.0", 
                "minecraft:recipe_shapeless": {
                    "description": {
                        "identifier": self.id+" recipe"
                    }, 
                    "ingredients": [
                        {
                            "item": self.id
                        }, 
                        {
                            "item": "minecraft:wool"
                        }
                    ], 
                    "result": {
                        "item": self.id
                    }, 
                    "tags": [
                        "crafting_table"
                    ]
                }
            }
        
            
            return {
                "model" : item_model,
                "behavior" : item_2d_bp,
                "behavior 3d" : item_3d_bp,
                "animation" : item_animation,
                "attachable" : item_attachable,
                "recipe" : item_recipe,
                "texture" : item_tex,
                "texture attachable" : item_attachable_tex
            }

    def __init__(self, fn, seed):
        self.R = random.Random(seed)  #  Ensure consistency on repeated invocations
        self.asset_ids = { "tile." : [],
                        "item." : [],
                        "entity." : []
                      }

        self.tiles = {}     #  This is a collection of Block objects
        self.entities = {}  #  This is a collection of Entity objects
        self.items = {}     #  This is a collection of Item objects

        self.lang = {}  #  This is a collection of parsed key/value lines
        
        self.create_from_keyvalue_file(fn)

    def create_from_keyvalue_file(self, path):
        #   Read each line in the file, working out each key and value.
        #   Create a stub object for each thing
        
        with open(path) as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                self.lang[name.strip()] = var.strip()
        
        NAME_MARK = ".name"
        #   For each key, is it describing the existence of a block, item or entity?
        for key in self.lang:
            if key.endswith(NAME_MARK) and not key.startswith("item.spawn_egg."):
                for asset_type in self.asset_ids:
                    if key.startswith(asset_type):
                        print(key)
                        asset_id = key[len(asset_type):len(key)-len(NAME_MARK)]    #  grab the object identifier
                        asset_id = asset_id.replace(".",":",1)    #  Replace the first . with : for namespace formatting
                        self.asset_ids[asset_type].append(asset_id)
                        
                        if asset_type == "tile.":
                            self.tiles[asset_id] = AddOn.Tile(asset_id, self.lang[key])
                        if asset_type == "item.":
                            self.items[asset_id] = AddOn.Item(asset_id, self.lang[key])
                        if asset_type == "entity.":
                            self.entities[asset_id] = AddOn.Entity(asset_id, self.lang[key])

    def render_to_files(self):
        #  Creates the BP and RP file system and files
        ft = AddOn.Tools()
        ROOT_RP = ft.clean_string(self.lang["pack.name"]+"_RP")
        ROOT_BP = ft.clean_string(self.lang["pack.name"]+"_BP")
        
        #  Don't change this order, only add entries to the end.
        list_of_dirs = [
            ROOT_RP, # 0
            ROOT_BP, # 1
            os.path.join(ROOT_BP,"blocks"),                 # 2
            os.path.join(ROOT_BP,"items"),                  # 3
            os.path.join(ROOT_BP,"entities"),               # 4
            
            os.path.join(ROOT_RP,"entity"),                 # 5
            os.path.join(ROOT_RP,"models"),                 # 6
            os.path.join(ROOT_RP,"models/blocks"),          # 7
            os.path.join(ROOT_RP,"models/entity"),          # 8
            os.path.join(ROOT_RP,"models/entity/attachable"),  # 9
            os.path.join(ROOT_RP,"texts"),                  # 10
            os.path.join(ROOT_RP,"textures"),               # 11
            os.path.join(ROOT_RP,"textures/blocks"),        # 12
            os.path.join(ROOT_RP,"textures/entities"),        # 13
            os.path.join(ROOT_RP,"textures/items"),         # 14
            os.path.join(ROOT_RP,"animations"),             # 15
            os.path.join(ROOT_RP,"animations/attachables"), # 16
            os.path.join(ROOT_RP,"attachables"),            # 17
            os.path.join(ROOT_RP,"textures/attachable"),    # 18
            os.path.join(ROOT_BP,"recipes"),                # 19
            os.path.join(ROOT_RP,"textures/eggs")           # 20
        ]
        for path in list_of_dirs:
            ft.makedir(path)

        shutil.copy("en_US.lang", list_of_dirs[10])  #  Remember to add a stub texts on BP with pack name/desc

        #  Manifests.
        manifest_rp_uuid = ft.make_uuid(self.R)
        manifest_rp = {
            "format_version": 2,
            "header": {
                "name": self.lang["pack.name"]+" Pack",
                "description": self.lang["pack.description"],
                "uuid": manifest_rp_uuid,
                "version": [1, 0, 0],
                "min_engine_version": [1, 16, 0]
            },
            "metadata": {
                "authors": ["@TheWorldFoundry"],
                "generated_with": {
                    "AddOn Gen ": [_VERSION]
                }
            },
            "modules": [
                {
                    "description": self.lang["pack.name"]+" Pack",
                    "type": "resources",
                    "uuid": ft.make_uuid(self.R),
                    "version": [1, 0, 0]
                }
            ]
        }

        manifest_bp = {
            "format_version": 2,
            "header": {
                "name": self.lang["pack.name"]+" Pack",
                "description": self.lang["pack.description"],
                "uuid": ft.make_uuid(self.R),
                "version": [1, 0, 0],
                "min_engine_version": [1, 16, 0]
            },
            "metadata": {
                "authors": ["@TheWorldFoundry"],
                "generated_with": {
                    "AddOn Gen ": [_VERSION]
                }
            },
            "modules": [
                {
                    "description": "Behavior",
                    "version": [1, 0, 0],
                    "uuid": ft.make_uuid(self.R),
                    "type": "data"
                }
            ],
            "dependencies": [
                {
                    "uuid": manifest_rp_uuid,
                    "version": [1, 0, 0]
                }
            ]
        }
        
        ft.write_json(list_of_dirs[0], "manifest.json", manifest_rp)
        ft.write_json(list_of_dirs[1], "manifest.json", manifest_bp)
        
        textures_list_json = []
        
        #  Aggregate block-specific files
        terrain_texture_json = {
            "resource_pack_name": "vanilla",
            "texture_name": "atlas.terrain",
            "padding": 8,
            "num_mip_levels": 4,
            "texture_data": {
                #  "sample_block": {
                #    "textures": "textures/blocks/sample_block.png"
                #  }
            }
        }

        blocks_json = {}
        #  Now we've got to make instances of all the relevant files from the assets repo.
        for block in self.tiles:
            block = self.tiles[block]  # Use the key to get the object
            files = block.render_to_files(self.R)

            model = files["model"]
            behavior = files["behavior"]
            texture = files["texture"]
            
            #  Per-block files
            ft.write_json(list_of_dirs[2], block.id_cleaned+".block.json", behavior)
            ft.write_json(list_of_dirs[7], block.id_cleaned+".geo.json", model)
            blocks_json[block.id_cleaned] = {
                "sound": "stone"
            }
            if texture is not None:
                ft.write_image(list_of_dirs[12], block.id_cleaned+"_tex.png", texture)
                textures_list_json.append((list_of_dirs[12]+"/"+block.id_cleaned+"_tex.png").replace("\\","/"))
                
            terrain_texture_json["texture_data"][block.id_cleaned+"_t_tex"] = {
                "textures": "textures/blocks/"+block.id_cleaned+"_tex.png"
            }
            
        ft.write_json(list_of_dirs[11], "terrain_texture.json", terrain_texture_json)
        ft.write_json(list_of_dirs[0], "blocks.json", blocks_json)

        item_texture_json = {
            "texture_data": {
            }
        }

        for item in self.items:
            item = self.items[item]
            files = item.render_to_files(self.R)

            model = files["model"]
            behavior = files["behavior"]
            behavior_3d = files["behavior 3d"]
            texture = files["texture"]
            texture_attachable = files["texture attachable"]
            animation = files["animation"]
            attachable = files["attachable"]
            recipe = files["recipe"]
            if recipe is not None:
                ft.write_json(list_of_dirs[19], item.id_cleaned+"_recipe.json", recipe)
            if texture is not None:
                ft.write_image(list_of_dirs[14], item.id_cleaned+"_tex.png", texture)
                textures_list_json.append((list_of_dirs[14]+"/"+item.id_cleaned+"_tex.png").replace("\\","/"))
                
            item_texture_json["texture_data"][item.id_cleaned+"_i_tex"] = {
                    "textures": "textures/items/"+item.id_cleaned+"_tex.png"
            }
            #if texture_attachable is not None:
            #    ft.write_image(list_of_dirs[18], item.id_cleaned+"_attach_tex.png", texture_attachable)
            #    textures_list_json.append((list_of_dirs[18]+"/"+item.id_cleaned+"_attach_tex.png").replace("\\","/"))
                #ft.write_image(list_of_dirs[14], item.id_cleaned+"_attach_tex.png", texture)

            ft.write_json(list_of_dirs[9], item.id_cleaned+".geo.json", model)
            ft.write_json(list_of_dirs[16], item.id_cleaned+".animation.json", animation)
            # ft.write_json(list_of_dirs[17], item.id_cleaned+".attachable.json", attachable)
            #  ft.write_json(list_of_dirs[3], item.id_cleaned+".item.json", behavior_3d)
            ft.write_json(list_of_dirs[3], item.id_cleaned+".item.json", behavior) # 2d version

        sounds_json = {
            "entity_sounds": {
                "entities": {}
            }
        }
        
        

        for entity in self.entities:
            entity = self.entities[entity]
            files = entity.render_to_files(self.R)
            model = files["model"]
            behavior = files["behavior"]
            resource = files["resource"]
            texture = files["texture"]
            texture_spawn_egg = files["texture spawn egg"]
            if texture is not None:
                ft.write_image(list_of_dirs[13], entity.id_cleaned+"_tex.png", texture)
                textures_list_json.append((list_of_dirs[13]+"/"+entity.id_cleaned+"_tex.png").replace("\\","/"))
                
            #item_texture_json["texture_data"]["entity_"+entity.id_cleaned+"_tex"] = {
            #        "textures": "textures/entities/"+entity.id_cleaned+"_tex.png"
            #}
            if texture_spawn_egg is not None:
                ft.write_image(list_of_dirs[20], entity.id_cleaned+"_spawn_egg_tex.png", texture_spawn_egg)
                textures_list_json.append((list_of_dirs[20]+"/"+entity.id_cleaned+"_spawn_egg_tex.png").replace("\\","/"))
            item_texture_json["texture_data"][entity.id_cleaned+"_spawn_egg_tex"] = {
                    "textures": "textures/eggs/"+entity.id_cleaned+"_spawn_egg_tex.png"
            }

            ft.write_json(list_of_dirs[8], entity.id_cleaned+".geo.json", model)
            ft.write_json(list_of_dirs[5], entity.id_cleaned+".entity.json", resource)
            ft.write_json(list_of_dirs[4], entity.id_cleaned+".entity.json", behavior)


        ft.write_json(list_of_dirs[11], "item_texture.json", item_texture_json)
        ft.write_json(list_of_dirs[11], "textures_list.json", textures_list_json)


#  Test it

my_addon = AddOn("en_US.lang", SEED)
my_addon.render_to_files()


print("BLOCKS:")
print(my_addon.asset_ids["tile."])
print(len(my_addon.tiles))

print("ITEMS:")
print(my_addon.asset_ids["item."])
print(len(my_addon.items))

print("ENTITIES:")
print(my_addon.asset_ids["entity."])
print(len(my_addon.entities))
        

'''
pack.name=Spells
pack.description=Resource Pack for Spells
entity.twf:dragonfly.name=Dragonfly
item.spawn_egg.entity.twf:dragonfly.name=Spawn Dragonfly
entity.twf:moth.name=Moth
item.spawn_egg.entity.twf:moth.name=Spawn Moth
action.hint.exit.twf:twf_vehiclick=SNEAK to stand up
action.hint.exit.twf:oscillator=SNEAK to stand up
entity.twf:twf_vehiclick.name=Vehiclick
item.spawn_egg.entity.twf:twf_vehiclick.name=Spawn Vehiclick
item.twf.twf_vehiclick.name=Spawn Vehiclick Shard
entity.twf:oscillator.name=Oscillator
item.spawn_egg.entity.twf:oscillator.name=Spawn Oscillator
item.twf.oscillator.name=Spawn Oscillator Shard
tile.twf:eyetwoframes.name=Eyetwoframes
tile.twf:eyetwoframes1.name=Eyetwoframes1
tile.twf:eyefourframes.name=Eyefourframes
tile.twf:eyefourframes1.name=Eyefourframes1
tile.twf:eyefourframes3.name=Eyefourframes3
tile.twf:eyefourframes2.name=Eyefourframes2
tile.twf:eyebase.name=Eyebase
tile.twf:twf_tentacle_a.name=Tentacle
entity.twf:twf_tentacle_a.name=Tentacle
item.spawn_egg.entity.twf:twf_tentacle_a.name=Spawn Tentacle
item.twf:twf_tentacle_a_item.name=Tentacle Piece
tile.twf:purtal_0_2.name=Purtal_0_2
tile.twf:purtal_0_0.name=Purtal_0_0
tile.twf:purtal_0_1.name=Purtal_0_1
tile.twf:purtal_2_0.name=Purtal_2_0
tile.twf:purtal_2_1.name=Purtal_2_1
tile.twf:purtal_2_2.name=Purtal_2_2
tile.twf:purtal_1_2.name=Purtal_1_2
tile.twf:purtal_1_1.name=Purtal_1_1
tile.twf:purtal_1_0.name=Purtal_1_0
tile.twf:twf_block.name=Block
entity.twf:twf_block.name=Block
item.spawn_egg.entity.twf:twf_block.name=Spawn Block
item.twf:twf_block_item.name=Block Shard
entity.twf:spells_1.name=1
entity.twf:spells_2.name=2
entity.twf:spells_3.name=3
entity.twf:spells_4.name=4
entity.twf:spells_5.name=5
entity.twf:spells_6.name=6
entity.twf:spells_7.name=7
entity.twf:spells_8.name=8
entity.twf:spells_9.name=9
entity.twf:spells_0.name=0
entity.twf:spells_upper_a.name=A
entity.twf:spells_upper_b.name=B
entity.twf:spells_upper_c.name=C
entity.twf:spells_upper_d.name=D
entity.twf:spells_upper_e.name=E
entity.twf:spells_upper_f.name=F
entity.twf:spells_upper_g.name=G
entity.twf:spells_upper_h.name=H
entity.twf:spells_upper_i.name=I
entity.twf:spells_upper_j.name=J
entity.twf:spells_upper_k.name=K
entity.twf:spells_upper_l.name=L
entity.twf:spells_upper_m.name=M
entity.twf:spells_upper_n.name=N
entity.twf:spells_upper_o.name=O
entity.twf:spells_upper_p.name=P
entity.twf:spells_upper_q.name=Q
entity.twf:spells_upper_r.name=R
entity.twf:spells_upper_s.name=S
entity.twf:spells_upper_t.name=T
entity.twf:spells_upper_u.name=U
entity.twf:spells_upper_v.name=V
entity.twf:spells_upper_w.name=W
entity.twf:spells_upper_x.name=X
entity.twf:spells_upper_y.name=Y
entity.twf:spells_upper_z.name=Z
entity.twf:spells_lower_a.name=a
entity.twf:spells_lower_b.name=b
entity.twf:spells_lower_c.name=c
entity.twf:spells_lower_d.name=d
entity.twf:spells_lower_e.name=e
entity.twf:spells_lower_f.name=f
entity.twf:spells_lower_g.name=g
entity.twf:spells_lower_h.name=h
entity.twf:spells_lower_i.name=i
entity.twf:spells_lower_j.name=j
entity.twf:spells_lower_k.name=k
entity.twf:spells_lower_l.name=l
entity.twf:spells_lower_m.name=m
entity.twf:spells_lower_n.name=n
entity.twf:spells_lower_o.name=o
entity.twf:spells_lower_p.name=p
entity.twf:spells_lower_q.name=q
entity.twf:spells_lower_r.name=r
entity.twf:spells_lower_s.name=s
entity.twf:spells_lower_t.name=t
entity.twf:spells_lower_u.name=u
entity.twf:spells_lower_v.name=v
entity.twf:spells_lower_w.name=w
entity.twf:spells_lower_x.name=x
entity.twf:spells_lower_y.name=y
entity.twf:spells_lower_z.name=z

item.twf:spells_1.name=1
item.twf:spells_2.name=2
item.twf:spells_3.name=3
item.twf:spells_4.name=4
item.twf:spells_5.name=5
item.twf:spells_6.name=6
item.twf:spells_7.name=7
item.twf:spells_8.name=8
item.twf:spells_9.name=9
item.twf:spells_0.name=0
item.twf:spells_upper_a.name=A
item.twf:spells_upper_b.name=B
item.twf:spells_upper_c.name=C
item.twf:spells_upper_d.name=D
item.twf:spells_upper_e.name=E
item.twf:spells_upper_f.name=F
item.twf:spells_upper_g.name=G
item.twf:spells_upper_h.name=H
item.twf:spells_upper_i.name=I
item.twf:spells_upper_j.name=J
item.twf:spells_upper_k.name=K
item.twf:spells_upper_l.name=L
item.twf:spells_upper_m.name=M
item.twf:spells_upper_n.name=N
item.twf:spells_upper_o.name=O
item.twf:spells_upper_p.name=P
item.twf:spells_upper_q.name=Q
item.twf:spells_upper_r.name=R
item.twf:spells_upper_s.name=S
item.twf:spells_upper_t.name=T
item.twf:spells_upper_u.name=U
item.twf:spells_upper_v.name=V
item.twf:spells_upper_w.name=W
item.twf:spells_upper_x.name=X
item.twf:spells_upper_y.name=Y
item.twf:spells_upper_z.name=Z
item.twf:spells_lower_a.name=a
item.twf:spells_lower_b.name=b
item.twf:spells_lower_c.name=c
item.twf:spells_lower_d.name=d
item.twf:spells_lower_e.name=e
item.twf:spells_lower_f.name=f
item.twf:spells_lower_g.name=g
item.twf:spells_lower_h.name=h
item.twf:spells_lower_i.name=i
item.twf:spells_lower_j.name=j
item.twf:spells_lower_k.name=k
item.twf:spells_lower_l.name=l
item.twf:spells_lower_m.name=m
item.twf:spells_lower_n.name=n
item.twf:spells_lower_o.name=o
item.twf:spells_lower_p.name=p
item.twf:spells_lower_q.name=q
item.twf:spells_lower_r.name=r
item.twf:spells_lower_s.name=s
item.twf:spells_lower_t.name=t
item.twf:spells_lower_u.name=u
item.twf:spells_lower_v.name=v
item.twf:spells_lower_w.name=w
item.twf:spells_lower_x.name=x
item.twf:spells_lower_y.name=y
item.twf:spells_lower_z.name=z
item.spawn_egg.entity.twf:spells_1.name=Spawn 1
item.spawn_egg.entity.twf:spells_2.name=Spawn 2
item.spawn_egg.entity.twf:spells_3.name=Spawn 3
item.spawn_egg.entity.twf:spells_4.name=Spawn 4
item.spawn_egg.entity.twf:spells_5.name=Spawn 5
item.spawn_egg.entity.twf:spells_6.name=Spawn 6
item.spawn_egg.entity.twf:spells_7.name=Spawn 7
item.spawn_egg.entity.twf:spells_8.name=Spawn 8
item.spawn_egg.entity.twf:spells_9.name=Spawn 9
item.spawn_egg.entity.twf:spells_0.name=Spawn 0
item.spawn_egg.entity.twf:spells_upper_a.name=Spawn A
item.spawn_egg.entity.twf:spells_upper_b.name=Spawn B
item.spawn_egg.entity.twf:spells_upper_c.name=Spawn C
item.spawn_egg.entity.twf:spells_upper_d.name=Spawn D
item.spawn_egg.entity.twf:spells_upper_e.name=Spawn E
item.spawn_egg.entity.twf:spells_upper_f.name=Spawn F
item.spawn_egg.entity.twf:spells_upper_g.name=Spawn G
item.spawn_egg.entity.twf:spells_upper_h.name=Spawn H
item.spawn_egg.entity.twf:spells_upper_i.name=Spawn I
item.spawn_egg.entity.twf:spells_upper_j.name=Spawn J
item.spawn_egg.entity.twf:spells_upper_k.name=Spawn K
item.spawn_egg.entity.twf:spells_upper_l.name=Spawn L
item.spawn_egg.entity.twf:spells_upper_m.name=Spawn M
item.spawn_egg.entity.twf:spells_upper_n.name=Spawn N
item.spawn_egg.entity.twf:spells_upper_o.name=Spawn O
item.spawn_egg.entity.twf:spells_upper_p.name=Spawn P
item.spawn_egg.entity.twf:spells_upper_q.name=Spawn Q
item.spawn_egg.entity.twf:spells_upper_r.name=Spawn R
item.spawn_egg.entity.twf:spells_upper_s.name=Spawn S
item.spawn_egg.entity.twf:spells_upper_t.name=Spawn T
item.spawn_egg.entity.twf:spells_upper_u.name=Spawn U
item.spawn_egg.entity.twf:spells_upper_v.name=Spawn V
item.spawn_egg.entity.twf:spells_upper_w.name=Spawn W
item.spawn_egg.entity.twf:spells_upper_x.name=Spawn X
item.spawn_egg.entity.twf:spells_upper_y.name=Spawn Y
item.spawn_egg.entity.twf:spells_upper_z.name=Spawn Z
item.spawn_egg.entity.twf:spells_lower_a.name=Spawn a
item.spawn_egg.entity.twf:spells_lower_b.name=Spawn b
item.spawn_egg.entity.twf:spells_lower_c.name=Spawn c
item.spawn_egg.entity.twf:spells_lower_d.name=Spawn d
item.spawn_egg.entity.twf:spells_lower_e.name=Spawn e
item.spawn_egg.entity.twf:spells_lower_f.name=Spawn f
item.spawn_egg.entity.twf:spells_lower_g.name=Spawn g
item.spawn_egg.entity.twf:spells_lower_h.name=Spawn h
item.spawn_egg.entity.twf:spells_lower_i.name=Spawn i
item.spawn_egg.entity.twf:spells_lower_j.name=Spawn j
item.spawn_egg.entity.twf:spells_lower_k.name=Spawn k
item.spawn_egg.entity.twf:spells_lower_l.name=Spawn l
item.spawn_egg.entity.twf:spells_lower_m.name=Spawn m
item.spawn_egg.entity.twf:spells_lower_n.name=Spawn n
item.spawn_egg.entity.twf:spells_lower_o.name=Spawn o
item.spawn_egg.entity.twf:spells_lower_p.name=Spawn p
item.spawn_egg.entity.twf:spells_lower_q.name=Spawn q
item.spawn_egg.entity.twf:spells_lower_r.name=Spawn r
item.spawn_egg.entity.twf:spells_lower_s.name=Spawn s
item.spawn_egg.entity.twf:spells_lower_t.name=Spawn t
item.spawn_egg.entity.twf:spells_lower_u.name=Spawn u
item.spawn_egg.entity.twf:spells_lower_v.name=Spawn v
item.spawn_egg.entity.twf:spells_lower_w.name=Spawn w
item.spawn_egg.entity.twf:spells_lower_x.name=Spawn x
item.spawn_egg.entity.twf:spells_lower_y.name=Spawn y
item.spawn_egg.entity.twf:spells_lower_z.name=Spawn z
tile.twf:underhall_pu_5_4.name=Underhall_pu_5_4
tile.twf:underhall_pu_5_5.name=Underhall_pu_5_5
tile.twf:underhall_pu_5_2.name=Underhall_pu_5_2
tile.twf:underhall_pu_5_3.name=Underhall_pu_5_3
tile.twf:underhall_pu_5_0.name=Underhall_pu_5_0
tile.twf:underhall_pu_5_1.name=Underhall_pu_5_1
tile.twf:underhall_pu_4_5.name=Underhall_pu_4_5
tile.twf:underhall_pu_4_4.name=Underhall_pu_4_4
tile.twf:underhall_pu_4_3.name=Underhall_pu_4_3
tile.twf:underhall_pu_4_2.name=Underhall_pu_4_2
tile.twf:underhall_pu_4_1.name=Underhall_pu_4_1
tile.twf:underhall_pu_4_0.name=Underhall_pu_4_0
tile.twf:underhall_pu_2_5.name=Underhall_pu_2_5
tile.twf:underhall_pu_2_4.name=Underhall_pu_2_4
tile.twf:underhall_pu_2_1.name=Underhall_pu_2_1
tile.twf:underhall_pu_2_0.name=Underhall_pu_2_0
tile.twf:underhall_pu_2_3.name=Underhall_pu_2_3
tile.twf:underhall_pu_2_2.name=Underhall_pu_2_2
tile.twf:underhall_pu_1_2.name=Underhall_pu_1_2
tile.twf:underhall_pu_1_3.name=Underhall_pu_1_3
tile.twf:underhall_pu_1_0.name=Underhall_pu_1_0
tile.twf:underhall_pu_1_1.name=Underhall_pu_1_1
tile.twf:underhall_pu_1_4.name=Underhall_pu_1_4
tile.twf:underhall_pu_1_5.name=Underhall_pu_1_5
tile.twf:underhall_pu_0_3.name=Underhall_pu_0_3
tile.twf:underhall_pu_0_2.name=Underhall_pu_0_2
tile.twf:underhall_pu_0_1.name=Underhall_pu_0_1
tile.twf:underhall_pu_0_0.name=Underhall_pu_0_0
tile.twf:underhall_pu_0_5.name=Underhall_pu_0_5
tile.twf:underhall_pu_0_4.name=Underhall_pu_0_4
tile.twf:underhall_pu_3_4.name=Underhall_pu_3_4
tile.twf:underhall_pu_3_5.name=Underhall_pu_3_5
tile.twf:underhall_pu_3_0.name=Underhall_pu_3_0
tile.twf:underhall_pu_3_1.name=Underhall_pu_3_1
tile.twf:underhall_pu_3_2.name=Underhall_pu_3_2
tile.twf:underhall_pu_3_3.name=Underhall_pu_3_3
item.spawn_egg.entity.twf:spells_exclamation_mark.name=Spawn exclamation mark
item.twf:spells_exclamation_mark.name=exclamation mark
item.spawn_egg.entity.twf:spells_hash.name=Spawn hash
item.twf:spells_hash.name=hash
item.spawn_egg.entity.twf:spells_percent.name=Spawn percent
item.twf:spells_percent.name=percent
item.spawn_egg.entity.twf:spells_dollar.name=Spawn dollar
item.twf:spells_dollar.name=dollar
item.spawn_egg.entity.twf:spells_ampersand.name=Spawn ampersand
item.twf:spells_ampersand.name=ampersand
item.spawn_egg.entity.twf:spells_right_parenthesis.name=Spawn right parenthesis
item.twf:spells_right_parenthesis.name=right parenthesis
item.spawn_egg.entity.twf:spells_left_parenthesis.name=Spawn left parenthesis
item.twf:spells_left_parenthesis.name=left parenthesis
item.spawn_egg.entity.twf:spells_plus.name=Spawn plus
item.twf:spells_plus.name=plus
item.spawn_egg.entity.twf:spells_asterix.name=Spawn asterix
item.twf:spells_asterix.name=asterix
item.spawn_egg.entity.twf:spells_hyphen.name=Spawn hyphen
item.twf:spells_hyphen.name=hyphen
item.spawn_egg.entity.twf:spells_comma.name=Spawn comma
item.twf:spells_comma.name=comma
item.spawn_egg.entity.twf:spells_forward_slash.name=Spawn forward slash
item.twf:spells_forward_slash.name=forward slash
item.spawn_egg.entity.twf:spells_period.name=Spawn period
item.twf:spells_period.name=period
item.spawn_egg.entity.twf:spells_equals.name=Spawn equals
item.twf:spells_equals.name=equals
item.spawn_egg.entity.twf:spells_less_than.name=Spawn less than
item.twf:spells_less_than.name=less than
item.spawn_egg.entity.twf:spells_question_mark.name=Spawn question mark
item.twf:spells_question_mark.name=question mark
item.spawn_egg.entity.twf:spells_greater_than.name=Spawn greater than
item.twf:spells_greater_than.name=greater than
item.spawn_egg.entity.twf:spells_at_sign.name=Spawn at sign
item.twf:spells_at_sign.name=at sign
item.spawn_egg.entity.twf:spells_left_square_brace.name=Spawn left square brace
item.twf:spells_left_square_brace.name=left square brace
item.spawn_egg.entity.twf:spells_right_square_brace.name=Spawn right square brace
item.twf:spells_right_square_brace.name=right square brace
item.spawn_egg.entity.twf:spells_backslash.name=Spawn backslash
item.twf:spells_backslash.name=backslash
item.spawn_egg.entity.twf:spells_underscore.name=Spawn underscore
item.twf:spells_underscore.name=underscore
item.spawn_egg.entity.twf:spells_circumflex.name=Spawn circumflex
item.twf:spells_circumflex.name=circumflex
item.spawn_egg.entity.twf:spells_apostrophe.name=Spawn apostrophe
item.twf:spells_apostrophe.name=apostrophe
item.spawn_egg.entity.twf:spells_left_curly_brace.name=Spawn left curly brace
item.twf:spells_left_curly_brace.name=left curly brace
item.spawn_egg.entity.twf:spells_right_curly_brace.name=Spawn right curly brace
item.twf:spells_right_curly_brace.name=right curly brace
item.spawn_egg.entity.twf:spells_pipe.name=Spawn pipe
item.twf:spells_pipe.name=pipe
item.spawn_egg.entity.twf:spells_tilda.name=Spawn tilda
item.twf:spells_tilda.name=tilda

item.twf:oscillator.name=Oscillator
item.twf:twf_vehiclick.name=Vehiclick
item.twf:output4424124846_item.name=Mystery piece 1
item.twf:output4638028600_item.name=Mystery piece 2
item.twf:output5640119400_item.name=Mystery piece 3
item.twf:output7564670460_item.name=Mystery piece 4
item.twf:output8946837583_item.name=Mystery piece 5

item.spawn_egg.entity.twf:twf_tentacle_a_horizontal.name=Tentacle (horizontal)
'''