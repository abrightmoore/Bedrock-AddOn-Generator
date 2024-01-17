# Bedrock-AddOn-Generator
Creates stub Resource and Behavior packs from an en_US.lang file for Minecraft Bedrock.

Tested with Minecraft 1.20.51

## Why do this?
This script creates a working Add-On pair of Resource and Behavior folders. You can then modify the blocks, entities, items and recipes to suit your project.

Bedrock's data-driven model for extending the game is powerful, but fiddly. It can be easy to mess up a texture reference or inadvertantly use the same identifier for different assets.

Multiple different JSON files must be created with magic cross-reference strings for the game to understand what you are doing.

## How do I use this?
This Python 3 script lets you set up Blocks, Items, and Entities in a text file called en_US.lang, and then uses this information to create a working RP/BP Add-On with minimal functionality that you can test in-game.

Your workflow will look like this:
1. Install Python version 3 if you don't already have it.
2. Install Pygame with: pip install pygame
3. Create an en_US.lang file with the following keys. You can change the values to suit your project:

> pack.name=AddOnGen Test
> pack.description=Add-On pack stub generation by The World Foundry (@TheWorldFoundry)

4. Add blocks to your en_US.lang using this syntax. This example adds a block with an identifier "twf:eyetwoframes". The important part is the "tile." at the start and the ".name=" at the end of the key:

> tile.twf:eyetwoframes.name=Eyetwoframes

5. Add items to your en_US.lang using this syntax. This example adds an item with an identifier "twf.oscillator". The important part is the "item." at the start and the ".name=" at the end of the key:

> item.twf.oscillator.name=Spawn Oscillator Shard

6. Add entities to your en_US.lang using this syntax. This example adds an entity with an identifier "twf:oscillator". The important part is the "entity." at the start and the ".name=" at the end of the key:

> entity.twf:oscillator.name=Oscillator

8. Edit the SEED value for this Add-On in the AddOn Gen script. Change the number to something unique for your project. You may choose to smash the number keys a little for good entropy:

> SEED = 123456789

9. Run the script with your en_US.lang file in the same directory.

> python .\addon_gen_v1.py

10. Verify the Behavior and Resource directories are created. In this example they will be:

> AddOnGen_Test_RP

> AddOnGen_Test_BP

10. Copy the generated BP and RP folders into your development_behavior_packs and development_resource_packs folders
11. Create a new Creative world in Minecraft, and add the generated BP to it. The RP should automatically activate.

NOTE: identifiers and keys should always be lowercase.
NOTE: every entity gets a spawn egg.

### More information

Discord: https://discord.gg/h62NN5R

DevLog: https://peoplemaking.games/@TheWorldFoundry/111762017474772111
