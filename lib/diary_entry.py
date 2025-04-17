class DiaryEntries:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.entries = []

    def add(self):
        entry = f"{self.title}: {self.contents}"
        self.entries.append(entry)   


    def count_words(self):
        words_in_string = self.contents.split(" ")
        return len(words_in_string)

    def reading_time(self, wpm):
        count_words = self.contents.split(" ")
        total_words = len(count_words)
        return round(total_words / wpm)
    

    # def reading_chunk(self, wpm, minutes):
    #     words_to_read = wpm * minutes
    #     reading_chunk = " ".join(self.words[self.current_chunk_index:self.current_chunk_index + words_to_read])
    #     self.current_chunk_index += words_to_read
    #     return reading_chunk


# class DiaryEntries:
#     # Where user can add diary entries
#     #   date: string
#     #   entry: string

#     def __init__(self, date, entry):
#         # Parameters:
#         #   date: string
#         #   entry: string
#         # Side-effects:
#         #   Sets the title and artist properties
#         pass

#     def add_diary(self, date, entry):
#         # Parameters:
#         #   date: string
#         #   entry: string
#         # Actions:
#         #   Creates diary entry
#         pass

#     def format(self):
#         # Returns:
#         #   A string of the form "date: entry"
#         pass