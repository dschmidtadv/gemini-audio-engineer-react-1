import json
import mido

with open('midi_data.json', 'r') as f:
    data = json.load(f)

mid = mido.MidiFile()
ticks_per_beat = 480
mid.ticks_per_beat = ticks_per_beat
bpm = data.get("tempo", 120)
tempo = mido.bpm2tempo(bpm)

for track_data in data.get("tracks", []):
    track = mido.MidiTrack()
    mid.tracks.append(track)
    if len(mid.tracks) == 1:
        track.append(mido.MetaMessage('set_tempo', tempo=tempo))
        time_sig = data.get("time_signature", [4, 4])
        if len(time_sig) >= 2:
            track.append(mido.MetaMessage('time_signature', numerator=time_sig[0], denominator=time_sig[1]))
    
    instrument_name = track_data.get("instrument", "Track")
    track.append(mido.MetaMessage('track_name', name=instrument_name))
    
    events = []
    for note in track_data.get("notes", []):
        pitch = int(note.get("pitch", 60))
        velocity = int(note.get("velocity", 100))
        start_time = float(note.get("start_time", 0))
        duration = float(note.get("duration", 1.0))
        start_tick = int(start_time * ticks_per_beat)
        end_tick = int((start_time + duration) * ticks_per_beat)
        events.append({"type": "note_on", "note": pitch, "velocity": velocity, "time": start_tick})
        events.append({"type": "note_off", "note": pitch, "velocity": 0, "time": end_tick})
    
    events.sort(key=lambda x: (x["time"], x["type"] == "note_on"))
    last_time = 0
    for event in events:
        delta_time = event["time"] - last_time
        track.append(mido.Message(event["type"], note=event["note"], velocity=event["velocity"], time=delta_time))
        last_time = event["time"]
    
    track.append(mido.MetaMessage('end_of_track', time=0))

mid.save('Producer_Suggestion.mid')
print('Saved to Producer_Suggestion.mid')
