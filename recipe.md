# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Diary                      │
│                            │
│   => [Diary Entries]       │
│ - list all entries         │
│ - pull entry by size       │
│ - pull entry w/ phone no.  |
│   => [To Do]               │
│ - pull 'to do' list entry  |
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Diary Entries           │
│                         │
│ - add entry             │
│ - format()              │
│ - lenght/word check     │
│ - todo entries          │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘

```

_Also design the interface of each class in more detail._

```python

class Diary:
    # Where user can view diary entries

    def __init__(self):
        # holds diary items
        pass

    def entry_list(self):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_phone_numbers(self, phone_no):
        # check all entries for contact numbers and return those entries (format focused)
        # Returns: list of strings
        pass # No code here yet

    def search_for_todo_entries(self, todo):
        # check all entries for 'todo' and return those entries
        # Returns: list of strings
        pass

    def search_for_entry_by_size(self):
        # input read time and pull compatible diary entries
        # Returns: single string
        pass


class DiaryEntries:
    # Where user can add diary entries
    #   date: string
    #   entry: string

    def __init__(self, date, entry):
        # Parameters:
        #   date: string
        #   entry: string
        # Side-effects:
        #   Sets the title and artist properties
        pass

    def add_diary(self, date, entry):
        # Parameters:
        #   date: string
        #   entry: string
        # Actions:
        #   Creates diary entry

    def format(self):
        # Returns:
        #   A string of the form "date: entry"
        pass


class Todo:
    #store items to be done

    def __init__(self, task):
        # Storage for 'to do' tasks
        pass
    
    def add_todo(self, task):
        # create new task entry
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
