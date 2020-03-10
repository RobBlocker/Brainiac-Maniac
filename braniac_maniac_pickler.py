import pickle

geography = {1:['Ah', 'Yo']}

datafile = open("geography_questions.pickle", "wb")
pickle.dump(geography, datafile)
datafile.close()

history = {1:['', '']}

datafile = open("history_questions.pickle", "wb")
pickle.dump(history, datafile)
datafile.close()

music = {1:['', '']}

datafile = open("music_questions.pickle", "wb")
pickle.dump(music, datafile)
datafile.close()

vidgames = {1:['', '']}

datafile = open("vidgames_questions.pickle", "wb")
pickle.dump(vidgames, datafile)
datafile.close()

mix = {1:['asd', 'asd']}

datafile = open("mix_questions.pickle", "wb")
pickle.dump(mix, datafile)
datafile.close()

geowrong = {1:['', '', '']}

datafile = open("geography_wrong.pickle", "wb")
pickle.dump(geowrong, datafile)
datafile.close()

historywrong = {1:['', '']}

datafile = open("history_wrong.pickle", "wb")
pickle.dump(historywrong, datafile)
datafile.close()

vidwrong = {1:['', '']}

datafile = open("vidgames_wrong .pickle", "wb")
pickle.dump(vidwrong, datafile)
datafile.close()

