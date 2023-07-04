import requests
# https://picsum.photos/200/300

def get_images_urls(count):

    if count <=0:
        print("Error: Count must be greater than 0")
        return
    for i in range(0,count):
        url = f"https://picsum.photos/id/{i}/800/1200"
        yield url

urls = get_images_urls(20)