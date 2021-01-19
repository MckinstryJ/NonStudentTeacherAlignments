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

What this repo outlines is how to get MFA working for new audio data within the Windows 10 environment. I doubt there are large differences between operating systems but its worth noting. So, lets say you are wanting to utilize FastSpeech2 using [ming024's implementation](https://github.com/ming024/FastSpeech2). To do so, you would need TextGrid files but lets say all you have is a collection of audio files of some person talking.

## Step 1: Create Metadata file
The first step towards these TextGrid files is to create a metadata file. 

This file is a CSV file that contains: 

| file            | text               |
|-----------------|--------------------|
| bob_audio_0_001 | I went to the park |

For the sake of simplicity later, each audio file should be of type 'wav' and, if possible, make the metadata file a tab delim file. 

Note:
<ul>
  <li>Don't put the words spoken in text in quotes</li>
  <li>Don't include the file type inside the audio file name</li>
  <li>Don't put in any spaces in the file name (certain programs have issues with spaces... they are working on it)</li>
</ul>

Sadly, this is a manual process but if you want to make this automatic you will have to trust current Speech-To-Text (STT) models to transcribe the audio. As a side note, the Deaf and Hard of Hearing community depend on these (STT) models to provide accurate closed captioning for movies, video, and in general audio files. For more info, check out this article on the [2019 Guide for Automatic Speech Recgonition](https://heartbeat.fritz.ai/a-2019-guide-for-automatic-speech-recognition-f1e1129a141c).

## Step 2: Resample Your Audio via SoX
From what I could gather, SoX is the go-to for adjusting the audio so that MFA can process the audio correctly. Take this with a grain of salt but I tried pysox and other approaches but they all didn't work for me. 

It would appear that the best sampling rate is 16kHz and it should only contain 1 channel. To make this easy, I included the required code for this step within this repo. You will just need to figure out how to [install sox](http://sox.sourceforge.net/) so that the code works.

## Step 3: Generate LAB files via Prosodylab Aligner Tools
For whatever reason, MFA looks for these so called lab files before creating the alignments. If you don't have them, it won't budge. What's funny, however, is the fact that these lab files are individual files that have the "audio file name" as the lab file name and the "words spoken in text" as the text in all caps within the file. A true head scratcher in terms of why is this a show stopper... but to get these lab files via Prosodylab Aligner Tools you will need to run the following in your command prompt:

```
git clone https://github.com/prosodylab/prosodylab.alignertools
```

Then modify their code to be up-to-date. I've uploaded the modified relabel_clean.py file to save you some time but the modifications might effect your setup so first try to run their original code but if you get a bunch of lab files with the same "words spoken in text" then use mine. 

You will most likely find it easy to interact with this file since they provide prompts to understand what you are wanting to do but for the sake of making a complete "how to" here are my inputs:
<ol>
	<li>1</li>
	<li>en (short for english)</li>
	<li>"abs location to tab delimited metadata file"</li>
	<li>just hit enter</li>
	<li>"abs location to your wav audio directory"</li>
	<li>just hit enter (default is wav)</li>
	<li>just hit enter</li>
	<li>y</li>
</ol>

Do note that if you made your metadata file (mentioned in step 1) to be comma sepearted then you will have to run a script to generate a tab delim metadata file. The needed script isn't difficult to make so I won't add that code.

The first several times I did this, I kept finding empty TextGrid files generated by prosodylab.alignertools. So if you find a bunch of these empty files, get rid of every single one (via script... unless you like slow and creeping pain) but keep all the lab files.

## Step 4: Install and Run MFA
Follow these [installation](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html) steps to effectively use MFA. Once completed, run the following within your command prompt:

```
activate aligner
mfa train C:/'path to wavs directory' C:/'path to librispeech-lexicon.txt' C:/'desired output path for TextGrid files'
```

This process will take some time since its training the model and optimizing it's weights. The librispeech lexicon for english can be downloaded here: [LibriSpeech Lexicon](https://drive.google.com/open?id=1dAvxdsHWbtA1ZIh3Ex9DPn9Nemx9M1-L).

## Step 5: Check Results
The final step is to make sure you check the results. This was important for me since the first attempt produced so many strange errors but if the first couple of files look correct you're safe to assume the remainding files are also correct.

## FINAL NOTE
If you tried these steps but still get an error somewhere, let me know (post inside the issues tab) so I can modify this "how to" to fit the general case plus the other special cases. Besides that, keep pushing to make these TTS models better!
