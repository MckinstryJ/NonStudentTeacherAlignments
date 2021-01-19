# NonStudentTeacherAlignments
A public repo to generate the files needed for Alignment based Mel Spectros vs Attention based.

For the models like [FastSpeech2](https://arxiv.org/pdf/2006.04558.pdf) (and other alignment based models), you are required to have what are called TextGrid files. These files contain information on what was said and at what time range within each audio file.

Here is an example of what it may look like:
```
...

xmin = 0.0
xmax = 2.0240625
tiers? <exists>
size = 2
item []:
	item [1]:
		class = "IntervalTier"
		name = "words"
		xmin = 0.0
		xmax = 2.0240625
		intervals: size = 8
			intervals [1]:
				xmin = 0.0
				xmax = 0.060
				text = ""
			intervals [2]:
				xmin = 0.060
				xmax = 0.230
				text = "their"

...
```

In order to get these TextGrid files, you can use the Praat software to generate them manually or you can take a more automated approach via [Montreal Forced Aligner (MFA)](https://montreal-forced-aligner.readthedocs.io/en/latest/index.html). How MFA generates these files automatically is by using Machine Learning to find the appropriate segments within your audio files. 

This could be seen as the 'teacher' in the attention based models, however, MFA is breaking that off as a sepearate research area and if newer models are using this as the 'teacher' then we could expect faster improvement for this forced aligner vs isolated development in those other teacher models (personal opinion).

What this repo outlines is how to get MFA working for new audio data within the Windows 10 environment. I doubt there is large differences between the operating systems but its worth noting. So, lets say you are wanting to utilize FastSpeech2 using [ming024's implementation](https://github.com/ming024/FastSpeech2). To do so you would need TextGrid files but all you have is your audio files of some person talking.

## Step 1: Create Metadata file
The first step towards these TextGrid files is to create a metadata file. 

This file is a CSV file that contains: 

| file            | text               |
|-----------------|--------------------|
| bob_audio_0_001 | I went to the park |

For the sake of simplicity later, each file should be of type 'wav' and if possible make it a tab sepearted file. At the very least, do make this file a CSV file. 

Note:
<ul>
  <li>Don't put the words spoken in text in quotes</li>
  <li>Don't include the file type inside the audio file name</li>
  <li>Don't put in any spaces in the file name (certain programs have issues with spaces... they are working on it)</li>
</ul>

Sadly, this is a manual process but if you want to make this automatic you will have to trust current Speech-to-text (STT) models to transcribe the audio. As a side note, the Deaf and Hard of Hearing community depend on these (STT) models to provide accurate closed captioning for movies, video, and in general audio files. For more info, check out this article on the [2019 guide for automatic speech recgonition](https://heartbeat.fritz.ai/a-2019-guide-for-automatic-speech-recognition-f1e1129a141c).

## Step 2: Resample You Audio via SoX
From what I could gather, SoX is the go-to for adjusting the audio so that MFA can process the audio correctly. It would appear that the best sampling rate is 16kHz and it should only contain 1 channel. To make this easy, I included the code for this step within this repo. You will just need to figure out how to install it so the code works.
