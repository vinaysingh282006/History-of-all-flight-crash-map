// Main application JavaScript for FreeSkillz

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
        modal.style.display = 'block';
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

// Enroll in a course
function enrollInCourse(courseId) {
    // Check if user has already provided their name
    let userName = localStorage.getItem('userName');
    
    if (!userName) {
        userName = prompt('Please enter your name to enroll in this course:');
        if (!userName) return;
        localStorage.setItem('userName', userName);
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
        document.getElementById('user-name').textContent = 'No profile data found';
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
        alert('Profile data cleared successfully!');
        location.reload();
    }
}

// Load course details from JSON (updated to handle nested topics structure)
function loadCourseDetails(courseId) {
    // Fetch course data from JSON file
    return fetch(`courses/${courseId}.json`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Course not found');
            }
            return response.json();
        })
        .then(courseData => {
            // Process the course data to ensure it has the correct structure
            if (courseData.topics) {
                // Already has topics structure, return as is
                return courseData;
            } else if (courseData.lessons) {
                // Convert flat lessons structure to topics structure
                return {
                    ...courseData,
                    topics: [
                        {
                            title: "Course Content",
                            lessons: courseData.lessons
                        }
                    ]
                };
            } else {
                // No lessons or topics, return empty structure
                return {
                    ...courseData,
                    topics: []
                };
            }
        });
}