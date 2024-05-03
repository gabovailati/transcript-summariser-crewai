import os
from dotenv import load_dotenv
load_dotenv()

from transcript_summariser_crew.crew import TranscriptSummariserCrew

def run():
    inputs = {
        'podcast_name': 'Andrew Huberman',
    }
    TranscriptSummariserCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()