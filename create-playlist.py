import os
import argparse

def get_files_with_subtitles(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.mp4'):
                video_name = os.path.splitext(filename)[0]
                subtitle = f"{video_name}.en.srt"
                if os.path.exists(os.path.join(root, subtitle)):
                    files.append(os.path.relpath(os.path.join(root, filename), directory))
    return files

def create_m3u_playlist(directory, files):
    playlist_path = os.path.join(directory, 'playlist.m3u')
    with open(playlist_path, 'w') as f:
        for file in files:
            f.write(file + '\n')
    print(f"Playlist created at: {playlist_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='Specify the directory to search for files')
    args = parser.parse_args()

    directory = args.dir if args.dir else os.getcwd()
    files = get_files_with_subtitles(directory)
    create_m3u_playlist(directory, files)

if __name__ == '__main__':
    main()