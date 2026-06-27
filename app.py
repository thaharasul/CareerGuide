from flask import Flask, render_template, request, jsonify
import re
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Career Recommendation Database with detailed information
CAREER_DATABASE = {
    'Software Engineer': {
        'description': 'Develop and maintain software applications and systems.',
        'skills': ['Python', 'Java', 'JavaScript', 'Problem Solving', 'Database Management'],
        'higher_studies': 'B.Tech in Computer Science, M.Tech in Software Engineering',
        'salary': '₹6,00,000 - ₹15,00,000 per annum',
        'scope': 'High demand globally, scope in AI, Cloud Computing, Cybersecurity',
        'resources': [
            'Codecademy - Interactive coding lessons',
            'LeetCode - Competitive programming',
            'GitHub - Portfolio building',
            'Coursera - Advanced certifications'
        ]
    },
    'AI Engineer': {
        'description': 'Design and develop artificial intelligence solutions and machine learning models.',
        'skills': ['Machine Learning', 'Python', 'TensorFlow', 'Data Analysis', 'Mathematics'],
        'higher_studies': 'M.Tech in AI/ML, B.Tech in Data Science',
        'salary': '₹8,00,000 - ₹20,00,000 per annum',
        'scope': 'Rapidly growing field, opportunities in autonomous vehicles, healthcare AI',
        'resources': [
            'Andrew Ng\'s Machine Learning Course',
            'Fast.ai - Deep Learning',
            'Kaggle - Data science competitions',
            'Stanford CS231N - Computer Vision'
        ]
    },
    'Data Scientist': {
        'description': 'Analyze complex data to help organizations make informed decisions.',
        'skills': ['Python', 'R', 'SQL', 'Statistics', 'Data Visualization'],
        'higher_studies': 'M.Sc in Data Science, B.Tech in Analytics',
        'salary': '₹7,00,000 - ₹18,00,000 per annum',
        'scope': 'Essential in finance, healthcare, e-commerce, and government sectors',
        'resources': [
            'DataCamp - Data science courses',
            'Mode Analytics - SQL tutorial',
            'Google Analytics Academy',
            'Tableau Public - Data visualization'
        ]
    },
    'Doctor': {
        'description': 'Diagnose and treat patients, perform medical procedures.',
        'skills': ['Medical Knowledge', 'Communication', 'Empathy', 'Decision Making', 'Teamwork'],
        'higher_studies': 'MBBS, MD/MS Specialization',
        'salary': '₹5,00,000 - ₹25,00,000+ per annum',
        'scope': 'Always in demand, private practice, research, abroad opportunities',
        'resources': [
            'NEET preparation books',
            'Medical colleges admission guides',
            'Clinical case studies',
            'Medical journals and publications'
        ]
    },
    'Pharmacist': {
        'description': 'Dispense medications and provide pharmaceutical care to patients.',
        'skills': ['Chemistry', 'Pharmacology', 'Customer Service', 'Attention to Detail'],
        'higher_studies': 'B.Pharmacy, M.Pharmacy',
        'salary': '₹3,50,000 - ₹10,00,000 per annum',
        'scope': 'Hospital, retail pharmacy, pharmaceutical industry, research',
        'resources': [
            'National Pharmacy Council resources',
            'Clinical Pharmacy journals',
            'Pharmaceutical industry certifications',
            'Online pharmacy courses'
        ]
    },
    'Nurse': {
        'description': 'Provide patient care and support medical professionals in healthcare settings.',
        'skills': ['Patient Care', 'Communication', 'Compassion', 'Physical Endurance'],
        'higher_studies': 'B.Sc Nursing, M.Sc Nursing',
        'salary': '₹3,00,000 - ₹8,00,000 per annum',
        'scope': 'Hospitals, clinics, private care, international opportunities',
        'resources': [
            'Nursing council guidelines',
            'Medical anatomy courses',
            'Patient care simulations',
            'Continuing education programs'
        ]
    },
    'Business Analyst': {
        'description': 'Analyze business needs and develop solutions to improve processes.',
        'skills': ['Data Analysis', 'Communication', 'Business Acumen', 'SQL', 'Excel'],
        'higher_studies': 'MBA, B.Tech with Business Analytics',
        'salary': '₹6,00,000 - ₹16,00,000 per annum',
        'scope': 'IT, Finance, Manufacturing, E-commerce sectors',
        'resources': [
            'IIBA - Business Analysis Body of Knowledge',
            'Google Data Analytics Certificate',
            'Business case study analysis',
            'Tableau and Power BI training'
        ]
    },
    'Entrepreneur': {
        'description': 'Start and manage your own business venture.',
        'skills': ['Leadership', 'Innovation', 'Financial Acumen', 'Risk Management', 'Sales'],
        'higher_studies': 'MBA, Business Management courses',
        'salary': 'Variable - Based on business success',
        'scope': 'Unlimited potential, impact on economy, job creation',
        'resources': [
            'Startup India portal',
            'Y Combinator startup school',
            'Lean Startup methodology',
            'Business plan templates'
        ]
    },
    'Marketing Manager': {
        'description': 'Develop and execute marketing strategies to promote products/services.',
        'skills': ['Strategic Planning', 'Creativity', 'Analytics', 'Communication', 'Digital Marketing'],
        'higher_studies': 'MBA in Marketing, B.Sc Marketing',
        'salary': '₹5,00,000 - ₹14,00,000 per annum',
        'scope': 'All industries, remote work opportunities, brand management',
        'resources': [
            'Google Digital Garage - Marketing fundamentals',
            'HubSpot Academy - Inbound marketing',
            'Coursera Marketing Specializations',
            'Social media marketing courses'
        ]
    },
    'Graphic Designer': {
        'description': 'Create visual content for various media and branding purposes.',
        'skills': ['Creative Design', 'Adobe Suite', 'UI/UX', 'Color Theory', 'Communication'],
        'higher_studies': 'B.Des Graphic Design, Diploma in Animation',
        'salary': '₹3,00,000 - ₹10,00,000 per annum',
        'scope': 'Advertising, Web Design, Animation, Gaming, Publishing',
        'resources': [
            'Adobe Creative Cloud tutorials',
            'Behance - Design portfolio platform',
            'Dribbble - Design inspiration',
            'Skillshare design courses'
        ]
    },
    'Animator': {
        'description': 'Create animated content for films, games, and digital media.',
        'skills': ['Animation Software', 'Creativity', 'Technical Skills', 'Storytelling'],
        'higher_studies': 'B.Sc Animation, Diploma in VFX',
        'salary': '₹3,50,000 - ₹12,00,000 per annum',
        'scope': 'Film industry, Gaming, Advertising, VFX Studios',
        'resources': [
            'Blender tutorials',
            'Maya animation courses',
            'Animation Mentor online classes',
            'Pixar animation masterclasses'
        ]
    },
    'Content Writer': {
        'description': 'Create engaging written content for websites, blogs, and media platforms.',
        'skills': ['Writing', 'Research', 'SEO', 'Communication', 'Creativity'],
        'higher_studies': 'B.A English, Diploma in Journalism',
        'salary': '₹2,50,000 - ₹8,00,000 per annum',
        'scope': 'Content agencies, Corporate, Freelance, Publishing',
        'resources': [
            'Copyblogger writing guides',
            'Grammarly academy',
            'SEO by Moz courses',
            'Content marketing platforms'
        ]
    },
    'Civil Services Officer': {
        'description': 'Serve the nation as an administrative officer, managing public affairs.',
        'skills': ['Leadership', 'Problem Solving', 'Ethics', 'Public Service', 'Administration'],
        'higher_studies': 'UPSC Civil Services Exam, B.A/B.Sc any stream',
        'salary': '₹9,30,000 - ₹39,00,000+ per annum',
        'scope': 'IAS, IPS, IFS, State services, high social impact',
        'resources': [
            'UPSC official portal',
            'Vision IAS study materials',
            'The Hindu newspaper',
            'Current affairs magazines'
        ]
    },
    'Police Officer': {
        'description': 'Maintain law and order, ensure public safety and security.',
        'skills': ['Discipline', 'Physical Fitness', 'Decision Making', 'Courage'],
        'higher_studies': '12th Pass, Physical fitness requirements',
        'salary': '₹5,00,000 - ₹15,00,000 per annum',
        'scope': 'Central forces, State police, specialized units',
        'resources': [
            'Police recruitment boards',
            'Physical training guides',
            'Law and order study materials',
            'Competitive exam preparation'
        ]
    },
    'Banking Officer': {
        'description': 'Manage financial operations, customer relations, and banking services.',
        'skills': ['Financial Acumen', 'Customer Service', 'Analysis', 'Compliance'],
        'higher_studies': 'B.Sc/B.Com, Banking and Finance courses',
        'salary': '₹5,50,000 - ₹12,00,000 per annum',
        'scope': 'Public/Private banks, Insurance, NBFCs',
        'resources': [
            'IBPS preparation materials',
            'Banking awareness courses',
            'RBI official publications',
            'Financial management courses'
        ]
    },
    'Mechanical Engineer': {
        'description': 'Design and develop mechanical systems and machinery.',
        'skills': ['CAD', 'Thermodynamics', 'Problem Solving', 'Technical Knowledge'],
        'higher_studies': 'B.Tech Mechanical Engineering, M.Tech',
        'salary': '₹4,50,000 - ₹14,00,000 per annum',
        'scope': 'Manufacturing, Automotive, Energy, Aerospace industries',
        'resources': [
            'ANSYS simulation software',
            'AutoCAD tutorials',
            'Mechanical engineering handbooks',
            'Industry certifications (ASME, ISO)'
        ]
    },
    'Automobile Engineer': {
        'description': 'Design and develop automobile systems and components.',
        'skills': ['CAD', 'Vehicle Dynamics', 'Embedded Systems', 'Materials Science'],
        'higher_studies': 'B.Tech Automobile Engineering, M.Tech',
        'salary': '₹4,50,000 - ₹13,00,000 per annum',
        'scope': 'Automotive industry, EV technology, Component manufacturing',
        'resources': [
            'CATIA design software',
            'MATLAB for automotive applications',
            'Automotive industry standards',
            'EV technology courses'
        ]
    },
    'Embedded Engineer': {
        'description': 'Develop embedded systems and microcontroller-based applications.',
        'skills': ['C/C++', 'Microcontrollers', 'VLSI', 'IoT', 'Real-time Systems'],
        'higher_studies': 'B.Tech Electronics, M.Tech Embedded Systems',
        'salary': '₹5,00,000 - ₹14,00,000 per annum',
        'scope': 'IoT, Consumer electronics, Telecommunications, Automotive',
        'resources': [
            'ARM Cortex-M programming',
            'Arduino and Raspberry Pi projects',
            'Embedded C courses',
            'VLSI design tutorials'
        ]
    },
    'Robotics Engineer': {
        'description': 'Design and develop robotic systems and automation solutions.',
        'skills': ['Robotics', 'AI/ML', 'Programming', 'Mechanical Design', 'Control Systems'],
        'higher_studies': 'B.Tech Robotics, M.Tech in Automation',
        'salary': '₹6,00,000 - ₹16,00,000 per annum',
        'scope': 'Manufacturing, Healthcare robotics, Space industry, Research',
        'resources': [
            'ROS (Robot Operating System)',
            'MATLAB Robotics Toolbox',
            'Computer vision courses',
            'Robotics competitions (ABU Robocon)'
        ]
    }
}

# Career mapping based on interests
CAREER_MAPPING = {
    'Programming': ['Software Engineer', 'AI Engineer', 'Data Scientist'],
    'Medical': ['Doctor', 'Pharmacist', 'Nurse'],
    'Business': ['Business Analyst', 'Entrepreneur', 'Marketing Manager'],
    'Arts': ['Graphic Designer', 'Animator', 'Content Writer'],
    'Government': ['Civil Services Officer', 'Police Officer', 'Banking Officer'],
    'Mechanical': ['Mechanical Engineer', 'Automobile Engineer'],
    'Electronics': ['Embedded Engineer', 'Robotics Engineer']
}

def validate_email(email):
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_career_recommendations(interest, skills_selected, work_style):
    """
    Get career recommendations based on user input.
    Uses multi-factor analysis for better recommendations.
    """
    # Get base careers from interest
    base_careers = CAREER_MAPPING.get(interest, [])
    
    if not base_careers:
        return None
    
    # Score careers based on skills match
    career_scores = {}
    for career in base_careers:
        career_info = CAREER_DATABASE[career]
        required_skills = career_info['skills']
        
        # Calculate skill match percentage
        if skills_selected:
            skill_match = sum(1 for skill in skills_selected if skill.lower() in [s.lower() for s in required_skills])
            skill_score = (skill_match / len(required_skills)) * 100 if required_skills else 0
        else:
            skill_score = 50  # Default score if no skills selected
        
        # Adjust score based on work style preference
        work_style_bonus = 10 if work_style == 'Team-based' else 5
        career_scores[career] = skill_score + work_style_bonus
    
    # Return career with highest score
    if career_scores:
        recommended_career = max(career_scores, key=career_scores.get)
        return recommended_career
    
    return base_careers[0] if base_careers else None

# Routes
@app.route('/')
def index():
    """Render home page"""
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    """Render career assessment form page"""
    return render_template('assessment.html')

@app.route('/submit-assessment', methods=['POST'])
def submit_assessment():
    """Process assessment form submission"""
    try:
        # Get form data
        full_name = request.form.get('fullName', '').strip()
        email = request.form.get('email', '').strip()
        qualification = request.form.get('qualification', '').strip()
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        interest = request.form.get('interest', '').strip()
        skills = request.form.getlist('skills')
        work_style = request.form.get('workStyle', '').strip()
        
        # Validation
        errors = []
        
        if not full_name or len(full_name) < 3:
            errors.append('Full name is required and must be at least 3 characters')
        
        if not email or not validate_email(email):
            errors.append('Valid email is required')
        
        if not qualification:
            errors.append('Highest qualification is required')
        
        if not age or not age.isdigit() or int(age) < 13 or int(age) > 80:
            errors.append('Valid age (13-80) is required')
        
        if not gender:
            errors.append('Gender is required')
        
        if not interest:
            errors.append('Interest field is required')
        
        if not work_style:
            errors.append('Work style preference is required')
        
        if errors:
            return jsonify({'success': False, 'errors': errors}), 400
        
        # Get career recommendation
        recommended_career = get_career_recommendations(interest, skills, work_style)
        
        if not recommended_career:
            return jsonify({'success': False, 'errors': ['Unable to find suitable career. Please try again.']}), 400
        
        # Store data in session-like structure (in production, use database)
        career_info = CAREER_DATABASE.get(recommended_career)
        
        result_data = {
            'success': True,
            'career': recommended_career,
            'fullName': full_name,
            'email': email,
            'interest': interest,
            'skillsSelected': ', '.join(skills) if skills else 'None',
            'description': career_info['description'],
            'skills': career_info['skills'],
            'higher_studies': career_info['higher_studies'],
            'salary': career_info['salary'],
            'scope': career_info['scope'],
            'resources': career_info['resources']
        }
        
        return jsonify(result_data)
    
    except Exception as e:
        return jsonify({'success': False, 'errors': [f'Server error: {str(e)}']}), 500

@app.route('/result')
def result():
    """Render result page with career recommendation"""
    return render_template('result.html')

@app.route('/contact')
def contact():
    """Render contact page"""
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Process contact form submission"""
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validation
        errors = []
        
        if not name or len(name) < 3:
            errors.append('Name is required and must be at least 3 characters')
        
        if not email or not validate_email(email):
            errors.append('Valid email is required')
        
        if not message or len(message) < 10:
            errors.append('Message must be at least 10 characters')
        
        if errors:
            return jsonify({'success': False, 'errors': errors}), 400
        
        # In production, save to database and send email
        # For now, just return success
        response_data = {
            'success': True,
            'message': 'Thank you for contacting us! We will get back to you soon.',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'success': False, 'errors': [f'Server error: {str(e)}']}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='localhost', port=5000)
