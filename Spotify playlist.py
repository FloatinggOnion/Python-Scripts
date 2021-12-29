playlist = {
    'title': 'AJR', 
    'author': 'JP', 
    'songs': [
        {'title': 'Way less sad', 'artist': ['AJR'], 'duration': 3.26},
        {'title': 'Sober up', 'artist': ['AJR', 'Rivers Cuomo'], 'duration': 3.49},
        {'title': 'Weak', 'artist': ['AJR'], 'duration': 3.24},
        {'title': 'Burn the house down', 'artist': ['AJR'], 'duration': 3.32},
        {'title': 'Three thirty', 'artist': ['AJR'], 'duration': 3.30},
        {'title': 'Addiction', 'artist': ['Paul The Messenger'], 'duration': 3.39}
    ]
}

total_duration = 0
for song in playlist['songs']:
    print(song['duration'])
    duration = float(song['duration'])
    total_duration += duration
    
print('Length: ', total_duration)