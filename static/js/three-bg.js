// Three.js Animated 3D Particle Network Background
document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('threejs-container');
    if (!container) return;

    // Scene setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000);

    // Camera
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 1, 1000);
    camera.position.z = 400;

    // Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // Particle system
    const particleCount = 300;
    const particles = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const velocities = [];

    // Create random particle positions
    for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 600;     // x
        positions[i * 3 + 1] = (Math.random() - 0.5) * 600; // y
        positions[i * 3 + 2] = (Math.random() - 0.5) * 600; // z

        velocities.push({
            x: (Math.random() - 0.5) * 0.5,
            y: (Math.random() - 0.5) * 0.5,
            z: (Math.random() - 0.5) * 0.5
        });
    }

    particles.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    // Particle material - white dots
    const particleMaterial = new THREE.PointsMaterial({
        color: 0xffffff,
        size: 3,
        transparent: true,
        opacity: 0.9,
        sizeAttenuation: true
    });

    // Create particle system
    const particleSystem = new THREE.Points(particles, particleMaterial);
    scene.add(particleSystem);

    // Lines for connections
    const lineMaterial = new THREE.LineBasicMaterial({
        color: 0xffffff,
        transparent: true,
        opacity: 0.15
    });

    // Create a group to hold all connection lines
    const linesGroup = new THREE.Group();
    scene.add(linesGroup);

    // Maximum distance for connections
    const maxDistance = 120;

    // Mouse tracking
    let mouseX = 0;
    let mouseY = 0;
    let targetRotationX = 0;
    let targetRotationY = 0;

    container.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect();
        mouseX = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
        mouseY = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
    });

    // Animation
    function animate() {
        requestAnimationFrame(animate);

        const positionArray = particles.attributes.position.array;

        // Update particle positions
        for (let i = 0; i < particleCount; i++) {
            // Move particles
            positionArray[i * 3] += velocities[i].x;
            positionArray[i * 3 + 1] += velocities[i].y;
            positionArray[i * 3 + 2] += velocities[i].z;

            // Bounce off boundaries
            if (Math.abs(positionArray[i * 3]) > 300) velocities[i].x *= -1;
            if (Math.abs(positionArray[i * 3 + 1]) > 300) velocities[i].y *= -1;
            if (Math.abs(positionArray[i * 3 + 2]) > 300) velocities[i].z *= -1;
        }

        particles.attributes.position.needsUpdate = true;

        // Clear old lines
        while (linesGroup.children.length > 0) {
            linesGroup.remove(linesGroup.children[0]);
        }

        // Create new connections
        const linePositions = [];
        for (let i = 0; i < particleCount; i++) {
            const x1 = positionArray[i * 3];
            const y1 = positionArray[i * 3 + 1];
            const z1 = positionArray[i * 3 + 2];

            for (let j = i + 1; j < particleCount; j++) {
                const x2 = positionArray[j * 3];
                const y2 = positionArray[j * 3 + 1];
                const z2 = positionArray[j * 3 + 2];

                const distance = Math.sqrt(
                    Math.pow(x2 - x1, 2) +
                    Math.pow(y2 - y1, 2) +
                    Math.pow(z2 - z1, 2)
                );

                if (distance < maxDistance) {
                    linePositions.push(x1, y1, z1, x2, y2, z2);
                }
            }
        }

        // Create line geometry
        if (linePositions.length > 0) {
            const lineGeometry = new THREE.BufferGeometry();
            lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
            const lines = new THREE.LineSegments(lineGeometry, lineMaterial);
            linesGroup.add(lines);
        }

        // Smooth rotation based on mouse
        targetRotationX = mouseY * 0.5;
        targetRotationY = mouseX * 0.5;

        particleSystem.rotation.x += (targetRotationX - particleSystem.rotation.x) * 0.02;
        particleSystem.rotation.y += (targetRotationY - particleSystem.rotation.y) * 0.02;
        linesGroup.rotation.x = particleSystem.rotation.x;
        linesGroup.rotation.y = particleSystem.rotation.y;

        // Auto-rotate slowly
        particleSystem.rotation.y += 0.001;
        linesGroup.rotation.y += 0.001;

        renderer.render(scene, camera);
    }

    animate();

    // Handle resize
    function onResize() {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    }

    window.addEventListener('resize', onResize);
});
