# Copilot

python3 -m venv venv

<!-- to activate the test environment -->
MAC
source venv/bin/activate
Windows


pip install SpeechRecognition
<!-- pip install pyttsx3 -->
pip install py3-tts
pip install googletrans==4.0.0-rc1
pip install langdetect
pip install pyobjc

<!-- install Homebrew into /usr/local. -->
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

arch -arm64 brew install portaudio --HEAD


<!-- install pyaudio -->
pip install PyAudio




/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

arch -arm64 brew install mpg321




MAC
steps to install pyaudio and portaudio on Mac M1
python3 -m pip install --upgrade pip setuptools wheel
brew install portaudio --HEAD
python3 -m pip install pyaudio --global-option="build_ext" --global-option="-I/opt/homebrew/include" --global-option="-L/opt/homebrew/lib"


<!-- brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio -->

python3 translate.py


To uninstall all the package :
pip freeze | xargs pip uninstall -y