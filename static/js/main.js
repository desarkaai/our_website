// Desarka Main JavaScript

document.addEventListener('DOMContentLoaded', function () {
    // ========== THEME TOGGLE (Light Bulb) ==========
    const themeToggle = document.getElementById('theme-toggle');
    const pullCord = document.getElementById('pull-cord');
    const body = document.body;

    // Check for saved theme preference or default to light
    const savedTheme = localStorage.getItem('desarka-theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-theme');
    }

    if (themeToggle) {
        let isPulling = false;

        themeToggle.addEventListener('click', function () {
            if (isPulling) return;
            isPulling = true;

            // Animate the pull cord
            if (pullCord) {
                pullCord.classList.add('pulled');

                // Play a subtle "click" animation
                setTimeout(() => {
                    pullCord.classList.remove('pulled');
                }, 200);
            }

            // Toggle theme after pull animation
            setTimeout(() => {
                body.classList.toggle('dark-theme');

                // Save preference
                if (body.classList.contains('dark-theme')) {
                    localStorage.setItem('desarka-theme', 'dark');
                } else {
                    localStorage.setItem('desarka-theme', 'light');
                }

                isPulling = false;
            }, 150);
        });

        // Add hover effect for pull cord
        themeToggle.addEventListener('mouseenter', function () {
            if (pullCord) {
                pullCord.style.transform = 'translateY(3px)';
            }
        });

        themeToggle.addEventListener('mouseleave', function () {
            if (pullCord && !pullCord.classList.contains('pulled')) {
                pullCord.style.transform = 'translateY(0)';
            }
        });
    }
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const mobileMenuClose = document.querySelector('.mobile-menu-close');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.add('active');
        });
    }

    if (mobileMenuClose) {
        mobileMenuClose.addEventListener('click', function () {
            mobileMenu.classList.remove('active');
        });
    }

    // Close mobile menu when clicking outside
    if (mobileMenu) {
        mobileMenu.addEventListener('click', function (e) {
            if (e.target === mobileMenu) {
                mobileMenu.classList.remove('active');
            }
        });
    }

    // Active Navigation Highlighting
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath ||
            (currentPath === '/' && linkPath === '/') ||
            (currentPath !== '/' && linkPath !== '/' && currentPath.includes(linkPath))) {
            link.classList.add('active');
        }
    });

    // Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add scroll animation observer for elements
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe elements with fade-in class if added
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });

    // Observe WOW animation elements
    document.querySelectorAll('.reveal-up, .scale-on-view, .rotate-in').forEach(el => {
        observer.observe(el);
    });

    // Custom Cursor Implementation
    const cursor = document.createElement('div');
    cursor.classList.add('custom-cursor');
    document.body.appendChild(cursor);
    document.body.classList.add('custom-cursor-active');

    // Track mouse movement - just move cursor, no smoke
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });

    // Add hover effect on interactive elements
    const interactiveElements = document.querySelectorAll('a, button, .flip-card, [role="button"], input, textarea');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.classList.add('hover');
        });
        el.addEventListener('mouseleave', () => {
            cursor.classList.remove('hover');
        });
    });

    // Hide cursor when leaving window
    document.addEventListener('mouseleave', () => {
        cursor.style.opacity = '0';
    });
    document.addEventListener('mouseenter', () => {
        cursor.style.opacity = '1';
    });
});
