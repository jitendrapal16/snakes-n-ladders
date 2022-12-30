# Usage

The Usage of the Console Application Work Follows :

-> There are two delieverable

### via `Python Script`
It Works with console Application, by using command :
- **Clone** the Repository
    ```bash 
    git clone https://github.com/jitendrapal16/Snakes-n-ladders.git
    cd Snakes-n-ladders/
    ```
- **Install** the dependencies and Run
   ```python
   pip install -r requirements.txt
   python app.py
   ```
   ---------------------------------------
  1. The Flow of Application Works like :
   ---------------------------------------
   > Game Start  --> Setup Players --> Setup Board(Snake & Ladder Config) -->
   --> setup Utility(Dice and Random config) --> setup game (customizable config) --> Start Play


   ---------------------------------------------------------------------------
  2. The Snakes and Ladders Game includes the following key Points & Entities :
   ---------------------------------------------------------------------------
   - **Board** :
      - The Board key Point Includes setup of `Board` and Its `Configurations`
      - It also covers `Snake` and `Ladder`,  Setup and Configuration
      - Board keeps the `Architecture` Simpler by keeping the Flow Simpler 
      by having the Entity and Property, which Should be on Board.
   -  **Players** :
      - The Players Entity Setup the `Player` and Its `Configuration` 
      which keeps the Flow and Connectivity Simpler with Board.
      - The Players having its Own `State` and `features`
   - **Utility** :
	   - The Utility Setup the `Dice` and its `Configuration`
   - **App Driver** :
	   - The App keeps the setup in sync, by following the Programming Principle,
	which makes the Code `simpler`, `easy to read`, `no repeatation`, and usage of `OOP's Paradigm`

### Via `Executable's` / `Binaries`
It also having the Executable/Binary in `Executables`[app.exe] directory
- The Executable can also be run as a package, without need to execute any command!

------------------------------------------------------------------------------------------------------

#### Points Considered :
1. The game support `min` of `2 players`, and can be used by `more than 2`,
 which also `generates` the `brief Result`.
2. Application is `configurable` to `customize` different **snakes and ladders configuration**
3. The **Solution** can be `build / compile` and run and also the `standard coding guidelines` has been followed with proper *Interaction* with **Class Implementation**

