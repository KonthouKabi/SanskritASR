import subprocess

def transcribe_audio(audio_path):
    # Replace with your Kaldi decoding command
    kaldi_cmd = f"sudo bash steps/decode.sh --nj 1 --cmd run.pl --skip-scoring true exp/mono/graph/HCLG.fst {audio_path} exp/mono/decode_test"
    
    # sudo steps/decode.sh --nj 1 --cmd run.pl --skip-scoring true

    # Execute the Kaldi command using subprocess
    try:
        subprocess.run(kaldi_cmd, shell=True, check=True, executable="/bin/bash")
    except subprocess.CalledProcessError as e:
        print("Error executing Kaldi command:", e)
        return

    # Read the transcribed text from the 'test_filt.txt' file in 'scoring_kaldi' folder
    try:
        with open('exp/mono/decode_test/scoring_kaldi/test_filt.txt', 'r') as text_file:
            transcriptions = text_file.readlines()

        for line in transcriptions:
            utterance_id, transcription = line.strip().split(' ', 1)
            print(f"Utterance ID: {utterance_id}, Transcription: {transcription}")

    except FileNotFoundError:
        print("Error: 'test_filt.txt' file not found. Please check if decoding was successful.")

if __name__ == "__main__":
    audio_path = "digits_audio/test/1/1.wav"
    transcribe_audio(audio_path)

