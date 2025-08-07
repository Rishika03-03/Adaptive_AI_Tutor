# Adaptive AI Tutor 🎓

An intelligent, personalized learning platform that adapts to individual student performance and provides tailored educational content using AI-powered tutoring.

## 🌟 Features

### 🧠 Intelligent Tutoring
- **Adaptive Learning**: Automatically adjusts difficulty based on student performance
- **Personalized Content**: Generates concept explanations tailored to your education level and current grades
- **Smart Progression**: Tracks taught concepts to avoid repetition and ensure comprehensive coverage

### 📚 Multi-Subject Support
- **School Level**: Supports Grades 1-12 with curriculum-aligned subjects
- **College Level**: Custom subject configuration for higher education
- **Subject-Specific**: Tailored content for Mathematics, Science, English, Computer Science, and more

### 🎯 Interactive Assessment
- **Dynamic Quizzes**: AI-generated multiple-choice questions based on taught concepts
- **Performance Tracking**: Real-time score calculation and feedback
- **Progress Monitoring**: Visual representation of learning progress over time

### 👤 User Management
- **Personal Profiles**: Individual learning profiles with subject grades and progress
- **Session Persistence**: Saves learning history and progress across sessions
- **Customizable Settings**: Easy profile updates and subject management

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: Google Gemini 2.0 Flash
- **Data Storage**: JSON-based local storage
- **Language**: Python 3.7+

## 📋 Requirements

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key

### Python Dependencies
```
streamlit>=1.28.0
google-generativeai>=0.3.0
```

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/adaptive-ai-tutor.git
cd adaptive-ai-tutor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Key
You need a Google Gemini API key to use the AI features:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Replace the API key in `tutor/ai_tutor.py` and `tutor/quiz_engine.py`:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

### 4. Run the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

### Getting Started
1. **Enter Your Name**: Start by entering your name to create or load your profile
2. **Set Education Level**: Choose between School or College level
3. **Configure Subjects**: 
   - For School: Select your grade and subjects will be automatically configured
   - For College: Add custom subjects and your current grades

### Learning Process
1. **Select Subject**: Choose a subject you want to learn
2. **Learn Concepts**: Click "Teach me a concept" to get AI-generated explanations
3. **Take Quizzes**: Test your understanding with interactive quizzes
4. **Track Progress**: Monitor your performance in the Performance tab

### Features Overview

#### 🏠 Home Tab
- User profile setup and management
- Subject selection
- Concept learning with AI explanations
- Interactive quiz generation and evaluation

#### 📊 Performance Tab
- View quiz history and scores
- Track progress across subjects
- Performance analytics

#### ⚙️ Settings Tab
- Update subject list and grades
- Modify learning preferences
- Profile management

## 🔧 Configuration

### Customizing Subjects
You can customize the available subjects by modifying the subject lists in `Home.py`:

```python
school_subjects = {
    "Grade 1-5": ["English", "Mathematics", "Science", "Social Studies"],
    "Grade 6-8": ["English", "Mathematics", "Science", "Computer Science", "History", "Geography", "Civics"],
    # Add more subjects as needed
}
```

### Adjusting Difficulty Levels
Modify the difficulty calculation in `tutor/ai_tutor.py`:

```python
def get_difficulty_level(marks):
    if marks >= 80:
        return "advanced"
    elif marks >= 60:
        return "intermediate"
    else:
        return "basic"
```
## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Voice-based interaction
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Integration with learning management systems
- [ ] Mobile app version
- [ ] Collaborative learning features
- [ ] Advanced assessment types (essays, coding challenges)

---

**Made with ❤️ for better education**
