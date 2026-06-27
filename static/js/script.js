// ============================================
// CAREER GUIDANCE SYSTEM - JAVASCRIPT
// ============================================

// Initialize animations and event listeners when DOM loads
document.addEventListener('DOMContentLoaded', function() {
    initializeNavbar();
    initializeSmoothScroll();
    initializeScrollAnimations();
    initializeButtonAnimations();
});

// ============= NAVBAR FUNCTIONALITY =============

/**
 * Initialize navbar toggle and active link highlighting
 */
function initializeNavbar() {
    const navLinks = document.querySelectorAll('.nav-link-custom');
    
    // Set active link based on current page
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        const currentPath = window.location.pathname;
        
        if (href === currentPath || (href === '/' && currentPath === '/')) {
            link.classList.add('active');
        }
    });
    
    // Handle navbar link clicks
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            // Add active class to clicked link
            this.classList.add('active');
        });
    });
}

// ============= SMOOTH SCROLLING =============

/**
 * Initialize smooth scrolling for anchor links
 */
function initializeSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Don't prevent default if href is just '#'
            if (href === '#') {
                return;
            }
            
            const target = document.querySelector(href);
            
            if (target) {
                e.preventDefault();
                
                // Calculate offset for fixed navbar
                const navHeight = document.querySelector('.navbar-custom').offsetHeight;
                const targetPosition = target.offsetTop - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ============= SCROLL ANIMATIONS =============

/**
 * Initialize animations on scroll using Intersection Observer
 */
function initializeScrollAnimations() {
    // Create observer options
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    // Create intersection observer
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add animation class
                entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements with data-aos attribute
    document.querySelectorAll('[data-aos]').forEach(element => {
        observer.observe(element);
    });
}

// ============= BUTTON ANIMATIONS =============

/**
 * Initialize button hover animations
 */
function initializeButtonAnimations() {
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
        
        button.addEventListener('click', function() {
            // Add ripple effect
            createRipple(this, event);
        });
    });
}

/**
 * Create ripple effect on button click
 * @param {HTMLElement} button - The button element
 * @param {Event} event - The click event
 */
function createRipple(button, event) {
    const ripple = document.createElement('span');
    
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');
    
    button.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 600);
}

// ============= FORM VALIDATION =============

/**
 * Validate email format
 * @param {string} email - Email address to validate
 * @returns {boolean} - True if email is valid
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validate full name
 * @param {string} name - Name to validate
 * @returns {boolean} - True if name is valid
 */
function validateName(name) {
    return name.trim().length >= 3;
}

/**
 * Validate age
 * @param {number} age - Age to validate
 * @returns {boolean} - True if age is valid (13-80)
 */
function validateAge(age) {
    const ageNum = parseInt(age);
    return !isNaN(ageNum) && ageNum >= 13 && ageNum <= 80;
}

/**
 * Validate message length
 * @param {string} message - Message to validate
 * @returns {boolean} - True if message is valid (min 10 chars)
 */
function validateMessage(message) {
    return message.trim().length >= 10;
}

// ============= FORM INPUT HANDLING =============

/**
 * Real-time form field validation
 */
function setupFormValidation() {
    // Validate email on change
    const emailInput = document.getElementById('email');
    if (emailInput) {
        emailInput.addEventListener('change', function() {
            const error = document.getElementById('emailError');
            if (error) {
                if (!validateEmail(this.value)) {
                    error.textContent = 'Please enter a valid email address';
                    this.classList.add('is-invalid');
                } else {
                    error.textContent = '';
                    this.classList.remove('is-invalid');
                }
            }
        });
    }
    
    // Validate age on change
    const ageInput = document.getElementById('age');
    if (ageInput) {
        ageInput.addEventListener('change', function() {
            const error = document.getElementById('ageError');
            if (error) {
                if (!validateAge(this.value)) {
                    error.textContent = 'Please enter a valid age (13-80)';
                    this.classList.add('is-invalid');
                } else {
                    error.textContent = '';
                    this.classList.remove('is-invalid');
                }
            }
        });
    }
    
    // Validate name on change
    const nameInput = document.getElementById('fullName');
    if (nameInput) {
        nameInput.addEventListener('change', function() {
            const error = document.getElementById('fullNameError');
            if (error) {
                if (!validateName(this.value)) {
                    error.textContent = 'Please enter a name with at least 3 characters';
                    this.classList.add('is-invalid');
                } else {
                    error.textContent = '';
                    this.classList.remove('is-invalid');
                }
            }
        });
    }
}

// ============= FORM SUBMISSION HANDLING =============

/**
 * Handle form submission with AJAX
 */
function handleFormSubmit(formId, endpoint) {
    const form = document.getElementById(formId);
    
    if (!form) return;
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading spinner
        const loadingSpinner = document.getElementById('loadingSpinner');
        if (loadingSpinner) {
            loadingSpinner.style.display = 'flex';
        }
        
        // Disable submit button
        const submitBtn = form.querySelector('[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
        }
        
        try {
            // Send form data
            const response = await fetch(endpoint, {
                method: 'POST',
                body: new FormData(form)
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Handle success
                handleFormSuccess(formId, data);
            } else {
                // Handle errors
                handleFormErrors(formId, data.errors);
            }
        } catch (error) {
            console.error('Error:', error);
            handleFormErrors(formId, ['An error occurred. Please try again.']);
        } finally {
            // Hide loading spinner
            if (loadingSpinner) {
                loadingSpinner.style.display = 'none';
            }
            
            // Enable submit button
            if (submitBtn) {
                submitBtn.disabled = false;
            }
        }
    });
}

/**
 * Handle successful form submission
 * @param {string} formId - ID of the form
 * @param {Object} data - Response data
 */
function handleFormSuccess(formId, data) {
    // Assessment form - redirect to results
    if (formId === 'assessmentForm') {
        sessionStorage.setItem('careerResult', JSON.stringify(data));
        window.location.href = '/result';
    }
    
    // Contact form - show success message
    if (formId === 'contactForm') {
        document.getElementById('contactForm').reset();
        const successMessage = document.getElementById('successMessage');
        if (successMessage) {
            successMessage.style.display = 'block';
            window.scrollTo(0, 0);
        }
    }
}

/**
 * Handle form validation errors
 * @param {string} formId - ID of the form
 * @param {Array} errors - Array of error messages
 */
function handleFormErrors(formId, errors) {
    // Assessment form errors
    if (formId === 'assessmentForm') {
        const errorsList = document.getElementById('errorsList');
        if (errorsList) {
            errorsList.innerHTML = '';
            errors.forEach(error => {
                const li = document.createElement('li');
                li.textContent = error;
                errorsList.appendChild(li);
            });
            document.getElementById('formErrors').style.display = 'block';
            window.scrollTo(0, 0);
        }
    }
    
    // Contact form errors
    if (formId === 'contactForm') {
        const errorText = document.getElementById('errorText');
        if (errorText) {
            errorText.textContent = errors.join(', ');
            document.getElementById('errorMessage').style.display = 'block';
            window.scrollTo(0, 0);
        }
    }
}

// ============= PROGRESS BAR HANDLING =============

/**
 * Update form progress bar based on filled fields
 */
function updateProgressBar() {
    const progressBar = document.getElementById('formProgress');
    
    if (!progressBar) return;
    
    const form = document.getElementById('assessmentForm');
    if (!form) return;
    
    // Count filled fields
    const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="number"], select');
    const radios = form.querySelectorAll('input[type="radio"]:checked');
    const checkboxes = form.querySelectorAll('input[type="checkbox"]:checked');
    
    const filledFields = inputs.length + radios.length + checkboxes.length;
    
    // Calculate percentage
    const totalFields = form.querySelectorAll('input[type="text"], input[type="email"], input[type="number"], select, input[type="radio"], input[type="checkbox"]').length;
    const percentage = (filledFields / totalFields) * 100;
    
    progressBar.style.width = Math.min(percentage, 100) + '%';
}

// ============= MODAL FUNCTIONALITY =============

/**
 * Close alerts and modals
 */
function initializeAlertClosing() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        const closeBtn = alert.querySelector('.btn-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                alert.style.display = 'none';
            });
        }
        
        // Auto-hide success messages after 5 seconds
        if (alert.classList.contains('alert-success')) {
            setTimeout(() => {
                alert.style.display = 'none';
            }, 5000);
        }
    });
}

// ============= KEYBOARD NAVIGATION =============

/**
 * Handle keyboard navigation
 */
function setupKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        // Close alerts on Escape key
        if (e.key === 'Escape') {
            const alerts = document.querySelectorAll('.alert.show');
            alerts.forEach(alert => alert.classList.remove('show'));
        }
        
        // Tab key for form navigation
        if (e.key === 'Tab') {
            // Allow default tab behavior
        }
    });
}

// ============= ACCESSIBILITY ENHANCEMENTS =============

/**
 * Improve form accessibility
 */
function improveAccessibility() {
    // Add aria-labels to form inputs
    document.querySelectorAll('.form-control-custom, .textarea-custom').forEach(input => {
        const label = input.previousElementSibling;
        if (label && !input.getAttribute('aria-label')) {
            input.setAttribute('aria-label', label.textContent);
        }
    });
    
    // Add focus indicators
    document.querySelectorAll('input, select, textarea, button').forEach(element => {
        element.addEventListener('focus', function() {
            this.style.boxShadow = '0 0 0 3px rgba(99, 102, 241, 0.1)';
        });
        
        element.addEventListener('blur', function() {
            this.style.boxShadow = 'none';
        });
    });
}

// ============= PAGE-SPECIFIC INITIALIZATION =============

/**
 * Initialize assessment page
 */
function initializeAssessmentPage() {
    setupFormValidation();
    handleFormSubmit('assessmentForm', '/submit-assessment');
    initializeAlertClosing();
    setupKeyboardNavigation();
    improveAccessibility();
}

/**
 * Initialize contact page
 */
function initializeContactPage() {
    setupFormValidation();
    handleFormSubmit('contactForm', '/submit-contact');
    initializeAlertClosing();
    setupKeyboardNavigation();
    improveAccessibility();
}

/**
 * Initialize result page
 */
function initializeResultPage() {
    // Results page uses sessionStorage data populated in HTML
    initializeAlertClosing();
}

// ============= RESPONSIVE DESIGN HELPERS =============

/**
 * Detect if device is mobile
 * @returns {boolean} - True if device width is less than 768px
 */
function isMobileDevice() {
    return window.innerWidth < 768;
}

/**
 * Handle window resize events
 */
window.addEventListener('resize', function() {
    // Update progress bar on resize
    if (document.getElementById('assessmentForm')) {
        updateProgressBar();
    }
});

// ============= FEATURE DETECTION =============

/**
 * Check for required browser features
 */
function checkBrowserSupport() {
    // Check for Fetch API
    if (!window.fetch) {
        console.warn('Fetch API is not supported. Some features may not work.');
    }
    
    // Check for sessionStorage
    if (!window.sessionStorage) {
        console.warn('sessionStorage is not supported. Result page may not work.');
    }
    
    // Check for Intersection Observer
    if (!window.IntersectionObserver) {
        console.warn('Intersection Observer is not supported. Scroll animations may not work.');
    }
}

// ============= PERFORMANCE OPTIMIZATION =============

/**
 * Debounce function for performance-heavy operations
 * @param {Function} func - Function to debounce
 * @param {number} delay - Delay in milliseconds
 * @returns {Function} - Debounced function
 */
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

/**
 * Throttle function for performance optimization
 * @param {Function} func - Function to throttle
 * @param {number} limit - Limit in milliseconds
 * @returns {Function} - Throttled function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ============= INITIALIZATION =============

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePages);
} else {
    initializePages();
}

/**
 * Initialize page-specific functionality
 */
function initializePages() {
    checkBrowserSupport();
    
    // Initialize assessment page
    if (document.getElementById('assessmentForm')) {
        initializeAssessmentPage();
    }
    
    // Initialize contact page
    if (document.getElementById('contactForm')) {
        initializeContactPage();
    }
    
    // Initialize result page
    if (document.querySelector('.career-result-card')) {
        initializeResultPage();
    }
    
    // Common initialization
    initializeNavbar();
    initializeSmoothScroll();
    initializeScrollAnimations();
    initializeButtonAnimations();
    initializeAlertClosing();
    setupKeyboardNavigation();
    improveAccessibility();
}

// ============= POLYFILLS =============

/**
 * Polyfill for Object.entries (for older browsers)
 */
if (!Object.entries) {
    Object.entries = function(obj) {
        var ownProps = Object.keys(obj),
            i = ownProps.length,
            resArray = new Array(i);
        while (i--)
            resArray[i] = [ownProps[i], obj[ownProps[i]]];
        return resArray;
    };
}

/**
 * Console logging for debugging (can be removed in production)
 */
const log = {
    info: function(msg) {
        if (process.env.NODE_ENV === 'development') {
            console.info('[CareerGuide]', msg);
        }
    },
    error: function(msg) {
        console.error('[CareerGuide Error]', msg);
    },
    warn: function(msg) {
        console.warn('[CareerGuide Warning]', msg);
    }
};

// Log initialization
if (window.location.pathname === '/') {
    log.info('Career Guidance System loaded successfully');
}
