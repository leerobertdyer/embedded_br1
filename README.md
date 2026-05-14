# Hello you lovely little trees

This is a simple repo for ongoing work with embedded systems. 

The single `main.py` will be run on a raspberry pi zero wh intentionally limiting what is capable to force decisions to account for hardware limitations (and because I didn't know there was a pi zero 2 - and because even if I did they are all sold out)

The initial concept was a talking bob ross mint tin that has both built in and LLM responses available, and can utilize STT and TTS over the wire to have real time conversations with robot bob ross.

Libraries used:
OpenAi SDK - whisper(stt)/llm integration


`/boot/firmware/config.txt` <--- where to handle adding dtoverlays for new cards currently using google hat for both mic AND DAC

Using SOX to amplify prior to sending audio to DAC:
`sox /tmp/test3.wav -t alsa plughw:1,0 vol 3`

Common commands:
`aplay -l` `arecord -l` -List devices avaiable from dtoverlay

`aplay -D plughw:1,0 /tmp/banjo.wav` <--- play using card 1 device 0, plug allows prehandling of audio for auto conversion of sample rate etc.. at minimal cost
`arecord -D plughw:1,0 -c 2 -r 48000 -f S16_LE -d 15 /tmp/banjo.wav` <--- record needs all the flags. -c for stero/mono -r for sample rate -d for duration 