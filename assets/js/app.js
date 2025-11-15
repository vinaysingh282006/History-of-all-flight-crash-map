// Main application JavaScript for FreeSkillz

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    checkLoginStatus();
    setupEventListeners();
});

// Set up event listeners
function setupEventListeners() {
    // Add event listener for Enter key in login input
    const userNameInput = document.getElementById('user-name-input');
    if (userNameInput) {
        userNameInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                loginUser();
            }
        });
    }
}

// Check if user is logged in
function checkLoginStatus() {
    const userName = localStorage.getItem('userName');
    const loginBtn = document.getElementById('login-btn');
    const profileBtn = document.getElementById('profile-btn');
    const userGreeting = document.getElementById('user-greeting');
    
    if (userName && loginBtn && profileBtn && userGreeting) {
        loginBtn.style.display = 'none';
        profileBtn.style.display = 'inline-block';
        userGreeting.textContent = `Hello, ${userName}!`;
        userGreeting.style.display = 'inline-block';
    } else if (loginBtn && profileBtn && userGreeting) {
        loginBtn.style.display = 'inline-block';
        profileBtn.style.display = 'none';
        userGreeting.style.display = 'none';
    }
}

// Show login modal
function showLoginModal() {
    const modal = document.getElementById('login-modal');
    if (modal) {
        modal.style.display = 'flex'; // Changed from 'block' to 'flex' for better centering
    }
}

// Close login modal
function closeLoginModal() {
    const modal = document.getElementById('login-modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Login user
function loginUser() {
    const userNameInput = document.getElementById('user-name-input');
    if (userNameInput) {
        const userName = userNameInput.value.trim();
        
        if (userName) {
            localStorage.setItem('userName', userName);
            closeLoginModal();
            checkLoginStatus();
            userNameInput.value = '';
            
            // If on profile page, refresh the profile display
            if (window.location.pathname.includes('profile.html')) {
                displayUserProfile();
            }
        } else {
            alert('Please enter your name');
        }
    }
}

// Logout user
function logoutUser() {
    if (confirm('Are you sure you want to log out?')) {
        localStorage.removeItem('userName');
        localStorage.removeItem('enrollments');
        // Remove all course progress data
        Object.keys(localStorage).forEach(key => {
            if (key.startsWith('completedLessons_')) {
                localStorage.removeItem(key);
            }
        });
        checkLoginStatus();
        // Redirect to home page if on profile page
        if (window.location.pathname.includes('profile.html')) {
            window.location.href = 'index.html';
        }
    }
}

// Enroll in a course
function enrollInCourse(courseId) {
    // Check if user has already provided their name
    let userName = localStorage.getItem('userName');
    
    if (!userName) {
        userName = prompt('Please enter your name to enroll in this course:');
        if (!userName) return;
        localStorage.setItem('userName', userName);
        checkLoginStatus(); // Update UI after setting user name
    }
    
    // Get current enrollments
    let enrollments = JSON.parse(localStorage.getItem('enrollments') || '[]');
    
    // Add course to enrollments if not already enrolled
    if (!enrollments.includes(courseId)) {
        enrollments.push(courseId);
        localStorage.setItem('enrollments', JSON.stringify(enrollments));
        alert(`Successfully enrolled in the course! Welcome, ${userName}!`);
    } else {
        alert(`You are already enrolled in this course, ${userName}!`);
    }
    
    // Redirect to course page
    window.location.href = `course.html?course=${courseId}`;
}

// Display user profile
function displayUserProfile() {
    const userName = localStorage.getItem('userName');
    const enrollments = JSON.parse(localStorage.getItem('enrollments') || '[]');
    
    if (!userName) {
        // Redirect to home page if not logged in
        window.location.href = 'index.html';
        return;
    }
    
    document.getElementById('user-name').textContent = userName;
    
    // Display enrolled courses
    const enrolledCoursesList = document.getElementById('enrolled-courses');
    if (enrollments.length === 0) {
        enrolledCoursesList.innerHTML = '<p>You have not enrolled in any courses yet.</p>';
        return;
    }
    
    // Load courses index to get course details
    fetch('courses/index.json')
        .then(response => response.json())
        .then(coursesIndexData => {
            // Filter courses that user is enrolled in
            const enrolledCourses = coursesIndexData.filter(course => 
                enrollments.includes(course.id)
            );
            
            enrolledCoursesList.innerHTML = '';
            enrolledCourses.forEach(course => {
                const courseElement = document.createElement('div');
                courseElement.className = 'profile-course-card';
                courseElement.innerHTML = `
                    <h3>${course.title}</h3>
                    <p>${course.description}</p>
                    <button class="btn btn-primary" onclick="window.location.href='course.html?course=${course.id}'">Continue Learning</button>
                `;
                enrolledCoursesList.appendChild(courseElement);
            });
        })
        .catch(error => {
            console.error('Error loading courses index:', error);
            // Fallback to hardcoded data
            const enrolledCourses = coursesIndexData.filter(course => 
                enrollments.includes(course.id)
            );
            
            enrolledCoursesList.innerHTML = '';
            enrolledCourses.forEach(course => {
                const courseElement = document.createElement('div');
                courseElement.className = 'profile-course-card';
                courseElement.innerHTML = `
                    <h3>${course.title}</h3>
                    <p>${course.description}</p>
                    <button class="btn btn-primary" onclick="window.location.href='course.html?course=${course.id}'">Continue Learning</button>
                `;
                enrolledCoursesList.appendChild(courseElement);
            });
        });
}

// Clear user profile
function clearProfile() {
    if (confirm('Are you sure you want to clear your profile data? This will remove all your enrollments.')) {
        localStorage.removeItem('userName');
        localStorage.removeItem('enrollments');
        // Remove all course progress data
        Object.keys(localStorage).forEach(key => {
            if (key.startsWith('completedLessons_')) {
                localStorage.removeItem(key);
            }
        });
        alert('Profile data cleared successfully!');
        location.reload();
    }
}