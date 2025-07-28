// Modern Portfolio JavaScript

// Navigation functionality
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Navbar scroll effect
    function handleScroll() {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.8)';
        }
    }

    window.addEventListener('scroll', handleScroll);

    // Mobile menu toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });

        // Close menu when clicking on a link
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            }
        });
    }

    // Animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                
                // Animate skill bars
                if (entry.target.classList.contains('skill-item')) {
                    const skillProgress = entry.target.querySelector('.skill-progress');
                    if (skillProgress) {
                        const width = skillProgress.style.width;
                        skillProgress.style.width = '0%';
                        setTimeout(() => {
                            skillProgress.style.width = width;
                        }, 200);
                    }
                }

                // Animate counters
                if (entry.target.classList.contains('stat')) {
                    animateCounter(entry.target.querySelector('.stat-number'));
                }
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.project-card, .skill-category, .timeline-item, .stat').forEach(el => {
        observer.observe(el);
    });

    // Counter animation
    function animateCounter(element) {
        if (!element || element.dataset.animated) return;
        
        const finalNumber = parseInt(element.textContent.replace('+', ''));
        let currentNumber = 0;
        const increment = finalNumber / 50;
        const suffix = element.textContent.includes('+') ? '+' : '';
        
        element.dataset.animated = 'true';
        
        const timer = setInterval(() => {
            currentNumber += increment;
            if (currentNumber >= finalNumber) {
                element.textContent = finalNumber + suffix;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(currentNumber) + suffix;
            }
        }, 50);
    }

    // Parallax effect for hero section
    function parallaxEffect() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.hero-particles');
        
        parallaxElements.forEach(element => {
            const speed = 0.5;
            element.style.transform = `translateY(${scrolled * speed}px)`;
        });
    }

    window.addEventListener('scroll', parallaxEffect);

    // Floating icons animation
    function animateFloatingIcons() {
        const floatingIcons = document.querySelectorAll('.floating-icon');
        floatingIcons.forEach((icon, index) => {
            icon.style.animationDelay = `${index * 0.5}s`;
            icon.style.animationDuration = `${6 + index}s`;
        });
    }

    animateFloatingIcons();

    // Utility functions
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#10b981' : '#ef4444'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);
        
        // Remove after 5 seconds
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 5000);
    }

    // Performance optimization: Throttle scroll events
    function throttle(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Apply throttling to scroll events
    window.addEventListener('scroll', throttle(handleScroll, 10));
    window.addEventListener('scroll', throttle(parallaxEffect, 10));
});

console.log('Portfolio website loaded successfully!');
