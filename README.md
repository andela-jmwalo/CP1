[![Build Status](https://travis-ci.org/andela-jmwalo/CP1.svg?branch=develop)](https://travis-ci.org/andela-jmwalo/CP1)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c9c034ff32874e4e814db5d5bc571403)](https://www.codacy.com/app/judith-achieng/CP1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-jmwalo/CP1&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/andela-jmwalo/CP1/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-jmwalo/CP1/develop)
[![Issue Count](https://codeclimate.com/github/andela-jmwalo/CP1/badges/issue_count.svg)](https://codeclimate.com/github/andela-jmwalo/CP1)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/c9c034ff32874e4e814db5d5bc571403)](https://www.codacy.com/app/judith-achieng/CP1?utm_source=github.com&utm_medium=referral&utm_content=andela-jmwalo/CP1&utm_campaign=Badge_Coverage)

# AMITY - Room Allocation System
AMITY is a room allocation system for one of Andela’s facilities.
![screenshot](https://github.com/andela-jmwalo/CP1/blob/develop/screenshot.png)
### Installation
Clone this repo from Github to your local machine:
```
git clone https://github.com/andela-jmwalo/CP1
```
cd into the CP1 folder
```
cd CP1
```
Install requirements
```
pip install -r requirements.txt
```
to Run the program :
```
python app.py -i
```
## Commands
1. `create_room <room_type><room_name>...` - This method allows the creation of one room or many rooms
2. `add_person <person_name> <FELLOW|STAFF>` - Add a person to the system and allocates the person to a random room
3. `reallocate_person <person_identifier> <new_room_name> <room_type>` - Reallocate the person to another room using their person id

4. `load_people` This method loads people from a text file into the system
5. `print_allocations [-o=filename]` - Prints a list of allocations  onto the screen. If a file name is specified it prints the allocations into the file.
6. `print_unallocated [-o=filename]` - Prints a list of unallocated people to the screen. If a file name is specified it prints the unallocated into the text file
7. `print_room <room_name>` - Prints the names of the people in `room_name` on the screen
8. `save_state [--db=sqlite_database]` - This method persists the state of the application into an SQLite database
9. `load_state <sqlite_database>` - This method loads the data from an SQLite database

## Tests
To run the tests 
```
pytest
```