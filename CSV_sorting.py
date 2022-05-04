from csv import reader

class FishPost:
    def __init__(self, index, imageURL, datePosted, timePosted, interactions):
        self.index = index
        self.imageURL = imageURL
        self.datePosted = datePosted
        self.timePosted = timePosted
        self.interactions = interactions

    def compareInteractions(self, fish):
        return int(self.interactions) - int(fish.interactions)
        # return < 0 if passed object is greater


path = "C:/Users/raybo/OneDrive/Documents/School/Comp 363/images/fish.csv"

fish_posts = []
with open(path, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        fish_posts.append(row)

fish_post_objects = []
for i in range(1, int(len(fish_posts)/2)):
    current_fish_post = fish_posts[i * 2]
    fish_post_objects.append(FishPost(current_fish_post[0], current_fish_post[1], current_fish_post[2], current_fish_post[3], current_fish_post[4]))

fish_times = []
fish_dates = []
fish_interactions = []
for fish in fish_post_objects:
    fish_times.append([fish, fish.timePosted])
    fish_dates.append([fish, fish.datePosted])
    fish_interactions.append([fish, fish.interactions])

