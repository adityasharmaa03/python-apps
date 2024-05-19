import json

def load_data():
    try:
        # load data from a file and convert it into json 
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    
    # if file is not found return empty list
    except FileNotFoundError:
        return []

# a helper method for saving all data
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 60)
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']}, Duration: {video['time']}')
        
    print("\n")
    print("*" * 60)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter length of video: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("Completed...")
    print("\n")
    print("*" * 60)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update: "))
    if index >=1 and index <= len(videos):
        name = input("Enter name of video: ")
        time = input("Enter duration of video: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data(videos)
        print("Completed...")
        print("\n")
        print("*" * 60)
    else:
        print("Invalid selection...")
        print("\n")
        print("*" * 60)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to be deleted: "))
    if index >=1 and index <= len(videos):
        del videos[index-1]
        save_data(videos)
        print("Completed...")
        print("\n")
        print("*" * 60)
    else:
        print("Invalid Selection....")
        print("\n")
        print("*" * 60)

def main():
    videos = load_data()
    while True:
        print('Youtube Manager app | Choose your options')
        print('1. List all youtube videos')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit app')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice...")
            

if __name__ == '__main__':
    main()
