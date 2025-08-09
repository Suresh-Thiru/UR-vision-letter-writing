“From Virtual Board to Real Pen!” 🖊️🤖

Youtube video: https://youtu.be/cZ9ZRlGGIS8

Weekend Learning Project: As a follow-up to my previous “virtual whiteboard” demo, I decided to add a physical twist—making the UR5e robot actually write down the recognized text with a marker.

What it does:

🖥️ I write text in the air on a virtual whiteboard (MediaPipe + OpenCV).

🔍 EasyOCR recognizes the text and saves it.

✏️ Predefined stroke templates for all 26 alphabets map each letter into vector movements.

🤖 The UR5e executes the strokes using a marker attached to its gripper, writing it on a real surface.

Tech stack (all open-source): Python • MediaPipe • OpenCV • EasyOCR • URScript (socket communication)

Why I built it:
Just a fun way to connect computer vision with a real robot arm—mainly for practice and learning. It’s basic, and anyone could build it with some time and curiosity, but it was satisfying to see the robot “write” my virtual text.

Possible future improvements with ML:

Handwriting recognition models (e.g., CRNN or TrOCR) to better handle cursive or stylized writing.

Stroke optimization using reinforcement learning for smoother and faster writing paths.

Dynamic scaling and alignment via CNN-based vision feedback for better letter proportions.

Real-time correction using a language model (BERT or GPT-based) to fix OCR errors before writing.

Nothing groundbreaking here—just another small step in experimenting with computer vision, OCR, and robotics, while thinking about how such concepts could scale into real automation or HRI (human-robot interaction) use cases in the future.
