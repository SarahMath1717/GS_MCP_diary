from lib.diary import Diary
from lib.diary_entry import DiaryEntries
from lib.diary_todo import ToDoList

def test_add_entry_to_diary():
    de = DiaryEntries("Monday", "I think I might be getting the hang of this")
    de.add()
    assert de.entries == ["Monday: I think I might be getting the hang of this"]
    de.count_words()
    assert de.count_words() == 10
    assert de.reading_time(5) == 2

def test_entry_list():
    de1 = DiaryEntries("Monday", "I think I might be getting the hang of this")
    de1.add()
    de2 = DiaryEntries("Tuesday", "I'm not sure this is making so much sense actually")
    de2.add()
    de3 = DiaryEntries("Wednesday", "...oh no")
    de3.add()
    d = Diary()
    d.list = de1.entries + de2.entries + de3.entries
    assert d.list == ["Monday: I think I might be getting the hang of this", "Tuesday: I'm not sure this is making so much sense actually", "Wednesday: ...oh no"]


