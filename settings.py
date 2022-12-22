import os

# AssemblyAI API
UPLOAD_ENDPOINT = 'https://api.assemblyai.com/v2/upload'
TRASCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
ASSEMBLY_KEY = 'a308bc93996143eaa1da0c49cb5e55b5'
# Cohere API
COHERE_KEY = 'COHERE_KEY'
COHERE_MODEL = 'large'
# Pinecone API
PINECONE_KEY = 'PINECONE_KEY'
PINECONE_ENV = 'us-west1-gcp'
PINCEONE_INDEX = 'cohere-pinecone-bible'

# The Root Directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

OUT_DIR = os.path.join(ROOT_DIR, 'output/')
RECORDING_DIR = os.path.join(OUT_DIR, 'recording')

WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")

# Audio configurations
INPUT_DEVICE = 0
MAX_INPUT_CHANNELS = 1  # Max input channels
DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
DURATION = 10   # 3 seconds
CHUNK_SIZE = 1024
