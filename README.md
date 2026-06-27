# Career Guidance System

A comprehensive web-based career guidance platform built with Flask that helps users discover suitable career paths based on their skills, interests, and preferences.

## Project Overview

The Career Guidance System is an intelligent career recommendation platform that assists students and professionals in finding the right career path. Users complete an assessment questionnaire, and the system provides personalized career recommendations along with detailed information about each career including required skills, educational requirements, salary expectations, and learning resources.

## Features

- **Interactive Career Assessment**: Comprehensive questionnaire with multiple choice and checkbox options
- **Intelligent Recommendation Engine**: Multi-factor analysis based on interests, skills, and work preferences
- **Detailed Career Information**: Complete guidance for 18 different careers across 7 industries
- **Responsive Design**: Mobile-friendly interface using modern CSS and Bootstrap
- **Form Validation**: Client-side and server-side validation for data integrity
- **Contact System**: Direct communication channel for user inquiries
- **Professional UI/UX**: Modern animations, gradients, and smooth interactions

## Supported Career Paths

### Programming Sector
- Software Engineer
- AI Engineer
- Data Scientist

### Medical Sector
- Doctor
- Pharmacist
- Nurse

### Business Sector
- Business Analyst
- Entrepreneur
- Marketing Manager

### Arts Sector
- Graphic Designer
- Animator
- Content Writer

### Government Sector
- Civil Services Officer
- Police Officer
- Banking Officer

### Mechanical Sector
- Mechanical Engineer
- Automobile Engineer

### Electronics Sector
- Embedded Engineer
- Robotics Engineer

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone or Download the Project**
   ```bash
   cd CareerGuidance
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Ensure Virtual Environment is Activated**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Run the Flask Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

4. **Stop the Server**
   Press `Ctrl + C` in the terminal

## Folder Structure

```
CareerGuidance/
│
├── app.py                          # Main Flask application with routes and logic
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── templates/                      # HTML templates folder
│   ├── index.html                 # Home page with hero section
│   ├── assessment.html            # Career assessment form
│   ├── result.html                # Career recommendation results
│   └── contact.html               # Contact form and details
│
└── static/                        # Static assets folder
    ├── css/
    │   └── style.css              # Professional stylesheet with animations
    ├── js/
    │   └── script.js              # Client-side JavaScript functionality
    └── images/                    # Image assets (placeholder)
```

## File Descriptions

### Backend
- **app.py**: Contains all Flask routes, career recommendation logic, form validation, and database (career information)

### Frontend
- **index.html**: Home page with navigation, hero section, features, and call-to-action
- **assessment.html**: Interactive assessment form with all required fields
- **result.html**: Displays personalized career recommendations with detailed information
- **contact.html**: Contact form and business contact information

### Styling & Interaction
- **style.css**: Professional stylesheet with:
  - Gradient backgrounds
  - Responsive flexbox/grid layouts
  - Card components with hover effects
  - Smooth animations and transitions
  - Media queries for mobile responsiveness
  - Modern typography and color scheme

- **script.js**: JavaScript functionality including:
  - Form validation
  - Smooth scrolling navigation
  - Navbar toggle for mobile
  - Scroll animations
  - Button animations and interactions

## Usage Guide

### For Users

1. **Visit Home Page**: Explore the platform and learn about its features
2. **Take Assessment**: Click "Start Assessment" to complete the questionnaire
3. **Fill Form**: Provide your information and preferences
4. **Get Recommendations**: View personalized career recommendations with full details
5. **Contact Support**: Use the contact page for any queries

### Career Assessment Form Fields

- **Full Name**: Your complete name (required)
- **Email**: Valid email address (required)
- **Highest Qualification**: Current educational level (required)
- **Age**: Your age (must be 13-80)
- **Gender**: Select your gender (required)
- **Interest**: Choose your primary interest area (required)
- **Skills**: Select applicable skills via checkboxes (optional)
- **Work Style**: Choose preferred work environment (required)

### Career Result Information

Each career recommendation includes:
- **Career Name**: Job title
- **Description**: Overview of the career
- **Required Skills**: Technical and soft skills needed
- **Higher Studies**: Educational qualifications required
- **Salary**: Expected salary range in India
- **Future Scope**: Career growth and opportunities
- **Learning Resources**: Recommended courses and platforms

## Technical Details

### Backend Technologies
- **Framework**: Flask 2.3.2
- **Language**: Python 3.8+
- **Request Handling**: Flask routing with GET/POST methods

### Frontend Technologies
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript**: ES6+ for interactivity
- **Bootstrap**: CDN for responsive components

### Key Features Implementation

**Career Recommendation Algorithm**:
- Base recommendation from selected interest area
- Skill matching analysis
- Work style preference weighting
- Multi-factor scoring system

**Form Validation**:
- Email format validation using regex
- Age range validation (13-80)
- Required field checking
- Minimum character requirements

**Responsive Design**:
- Mobile-first approach
- Flexbox and CSS Grid layout
- Media queries for different screen sizes
- Touch-friendly interface elements

## Browser Compatibility

- Chrome (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## API Endpoints

### GET Endpoints
- `/` - Home page
- `/assessment` - Assessment form page
- `/result` - Results page
- `/contact` - Contact page

### POST Endpoints
- `/submit-assessment` - Process assessment form (returns JSON)
- `/submit-contact` - Process contact form (returns JSON)

## Error Handling

- 404 Not Found: Returns home page
- 500 Server Error: Returns error message
- Form Validation: Client-side and server-side validation
- Email Validation: Regex pattern matching

## Future Enhancements

- Database integration (SQLAlchemy + SQLite/PostgreSQL)
- Email notification system for contact submissions
- User registration and login system
- Assessment history tracking
- Advanced analytics and reporting
- AI-powered recommendations using machine learning
- Video tutorials for each career
- Interview preparation resources
- Salary calculator with location-based data
- Mentor connection system

## Performance Optimization

- Minified CSS and JavaScript
- Optimized image assets
- Efficient form validation
- Server-side error handling
- Session management ready

## Security Considerations

- Input validation and sanitization
- Email validation
- Error message generalization
- CSRF protection ready (Flask-WTF ready)
- Environment variable support for secrets

## Troubleshooting

### Port 5000 Already in Use
```bash
# On Windows
netstat -ano | findstr :5000

# On macOS/Linux
lsof -i :5000
```
Kill the process or use a different port:
```bash
python app.py --port 5001
```

### Module Not Found Error
Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Template Not Found Error
Ensure the `templates/` folder is in the same directory as `app.py`

## Support and Contact

For issues, suggestions, or feature requests, use the contact page within the application.

## License

This project is open source and available for educational purposes.

## Author Notes

This Career Guidance System is designed as a comprehensive educational tool. The career recommendations are based on general industry trends and should be considered alongside professional career counseling.

## Version History

**Version 1.0 (Current)**
- Initial release with 18 careers across 7 sectors
- Assessment form with validation
- Personalized recommendations
- Contact system
- Responsive design

---

**Last Updated**: 2024
# CareerGuide
