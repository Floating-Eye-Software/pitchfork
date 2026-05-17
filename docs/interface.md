**Core Game Mechanics:**
- The game is turn-based, allowing players to take actions in a sequential order.
- The game world is grid-based, consisting of interconnected cells that represent the environment.

**Player Stats:**
- Player Health: Represents the player's remaining health points.
- Player Energy/Stamina: Represents the player's energy for performing actions.
- Player Level: Indicates the player's level of progression.

**Character Window:**
- The character window provides an overview of the player's stats and information.
- Displays player name, level, health, energy, and other relevant statistics.
- Allows players to review their character's status and make informed decisions.

**Inventory:**
- The player's inventory stores a collection of items acquired during the game.
- Each item has a name and description.

**Turn-Based Events:**
- Players take turns to perform actions within a designated turn cycle.
- A turn cycle includes movement, exploration, combat, and interactions.

**Player Movement:**
- Players can move in four primary directions: forward, backward, left, and right.
- Moving consumes a turn.
- The direction the player is facing determines the direction of movement.
- Players can choose between two movement systems: relative movement based on facing and cardinal movement (north-south-east-west).

**Strafing Mechanic:**
- Players can initiate strafing left or right.
- Strafing allows lateral movement without changing the player's facing.
- Strafing consumes a turn.

**Rotation Mechanic:**
- Players can rotate their facing to any of the four cardinal directions: north, south, east, and west.
- Changing direction (rotation) does not consume a turn.
- Players can strategically change their facing without penalty.

**Game User Interface:**
- UI includes controls for movement, strafing, rotation, and accessing the character window.
- Keyboard input is used for controlling movement, strafing, and rotation.
- UI elements display player health, energy, inventory items, available turns, and character statistics.
- Map, inventory, and character windows provide visual information about the game world and player progression.

**Exploration and Interaction:**
- Exploring reveals hidden areas, items, or events on the map.
- Players can interact with objects, NPCs, and environment elements to progress and uncover secrets.

**Combat and Challenges:**
- Combat and challenges are turn-based.
- Players engage in battles, utilizing items and abilities to defeat enemies.
- Environmental factors and tactics play a role in successful combat outcomes.

**Reactive Programming and MVI:**
- The Model-View-Intent (MVI) pattern structures the game's user interface and state management.
- Reactive programming principles are employed to manage data flow, state changes, and UI updates.
- Intents represent user actions, observables represent game state, and ViewModel handles the interaction between the two.

**Flexibility and Strategy:**
- The game offers players multiple movement options, allowing them to choose between relative movement and cardinal movement based on facing.
- The option to strafe and rotate strategically enhances the tactical depth of gameplay.
