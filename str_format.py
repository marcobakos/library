def poem_title_card(poet, title):
  poem_desc = "The poem \"{}\" is written by {}".format(title, poet)
  return poem_desc
print(poem_title_card("Walt Whitman", "I Hear America Singing"))