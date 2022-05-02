from csv import reader

class FishPost:
    def __init__(self, index, imageURL, datePosted, timePosted, interactions):
        self.index = index
        self.index = index
        self.imageURL = imageURL
        self.datePosted = datePosted
        self.timePosted = timePosted
        self.interactions = interactions


path = "C:/Users/raybo/OneDrive/Documents/School/Comp 363/images/fish.csv"

fish_posts = []
with open(path, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        fish_posts.append(row)

for i in range(int(len(fish_posts)/2)):
    print(fish_posts[i * 2])

fish_post_objects = []
for i in range(int(len(fish_posts)/2)):
    fish_post_objects[i * 2] = FishPost(fish_posts[0], fish_posts[1], fish_posts[2], fish_posts[3], fish_posts[4])

print(fish_post_objects)
