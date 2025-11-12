// Sample data for the website

// FAQ Data
const faqData = [
    { "q": "Is FreeSkillz really free?", "a": "Yes, all courses are 100% free to access." },
    { "q": "Do I get a certificate?", "a": "Yes, you can download your certificate after completing a course." },
    { "q": "Do I need to create an account?", "a": "No, you can enroll in courses without creating an account. Your data is stored locally in your browser." },
    { "q": "What kind of courses are offered?", "a": "We offer courses in Web Development, Programming, Design, and more. All courses are curated from high-quality free resources." },
    { "q": "Can I access courses offline?", "a": "Courses that are videos can be downloaded for offline viewing. Document-based courses require internet access." }
];

// Reviews Data
const reviewsData = [
    { "name": "Riya", "comment": "Loved the free learning experience! The courses are well-curated and easy to follow.", "rating": 5 },
    { "name": "Karan", "comment": "Simple and clean interface. I was able to learn Python without any distractions.", "rating": 4 },
    { "name": "Priya", "comment": "The web development course helped me land my first internship. Highly recommended!", "rating": 5 },
    { "name": "Arjun", "comment": "Great platform for beginners. The course materials are top-notch.", "rating": 4 }
];

// Courses Index Data
const coursesIndexData = [
    {
        "id": "webdev",
        "title": "Full Stack Web Development",
        "description": "Learn HTML, CSS, JavaScript, and backend basics to build complete websites.",
        "image": "assets/img/webdev.jpg",
        "category": "Web Development",
        "level": "Beginner"
    },
    {
        "id": "python",
        "title": "Python for Everyone",
        "description": "Master Python programming from basics to data handling.",
        "image": "assets/img/python.jpg",
        "category": "Programming",
        "level": "Beginner"
    },
    {
        "id": "design",
        "title": "UI/UX Design Fundamentals",
        "description": "Learn design principles and create stunning user interfaces.",
        "image": "assets/img/design.jpg",
        "category": "Design",
        "level": "Beginner"
    }
];

// Course Detail Data
const webdevCourseData = {
    "id": "webdev",
    "title": "Full Stack Web Development",
    "lessons": [
        { "title": "HTML Basics", "type": "video", "url": "https://www.youtube.com/embed/hQVTIJBZook" },
        { "title": "CSS Layouts", "type": "doc", "url": "https://docs.google.com/document/d/1uWDPhFdwGxJioi5DkEGRQpXyJUQqvjZF/edit" },
        { "title": "JavaScript Fundamentals", "type": "video", "url": "https://www.youtube.com/embed/W6NZfCO5SIk" },
        { "title": "DOM Manipulation", "type": "doc", "url": "https://docs.google.com/document/d/1W9VPUi5aN0_gb1NfjBbYlhkNMiuziO2_/edit" },
        { "title": "Backend with Node.js", "type": "video", "url": "https://www.youtube.com/embed/TlB_eWDSMt4" }
    ]
};

const pythonCourseData = {
    "id": "python",
    "title": "Python for Everyone",
    "lessons": [
        { "title": "Python Introduction", "type": "video", "url": "https://www.youtube.com/embed/rfscVS0vtbw" },
        { "title": "Variables and Data Types", "type": "doc", "url": "https://docs.google.com/document/d/1uWDPhFdwGxJioi5DkEGRQpXyJUQqvjZF/edit" },
        { "title": "Control Structures", "type": "video", "url": "https://www.youtube.com/embed/4OCd7Je12II" },
        { "title": "Functions and Modules", "type": "doc", "url": "https://docs.google.com/document/d/1W9VPUi5aN0_gb1NfjBbYlhkNMiuziO2_/edit" }
    ]
};

const designCourseData = {
    "id": "design",
    "title": "UI/UX Design Fundamentals",
    "lessons": [
        { "title": "Design Principles", "type": "video", "url": "https://www.youtube.com/embed/QeTbD3XEjhI" },
        { "title": "Color Theory", "type": "doc", "url": "https://docs.google.com/document/d/1uWDPhFdwGxJioi5DkEGRQpXyJUQqvjZF/edit" },
        { "title": "Typography Basics", "type": "video", "url": "https://www.youtube.com/embed/sByzHoiYFX0" }
    ]
};