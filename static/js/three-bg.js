// Three.js Animated 3D Particle Network that forms "DESARKA" text
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

    // Create canvas to generate text points
    function getTextPoints(text, fontSize = 80) {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = 800;
        canvas.height = 200;

        ctx.fillStyle = 'white';
        ctx.font = `bold ${fontSize}px Arial, sans-serif`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(text, canvas.width / 2, canvas.height / 2);

        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const points = [];
        const density = 4; // Sample every nth pixel

        for (let y = 0; y < canvas.height; y += density) {
            for (let x = 0; x < canvas.width; x += density) {
                const index = (y * canvas.width + x) * 4;
                if (imageData.data[index + 3] > 128) { // Check alpha
                    points.push({
                        x: (x - canvas.width / 2) * 1.2,
                        y: -(y - canvas.height / 2) * 1.2,
                        z: 0
                    });
                }
            }
        }
        return points;
    }

    // Get target positions for "DESARKA"
    const textPoints = getTextPoints('DESARKA');
    const particleCount = Math.max(textPoints.length, 400);

    // Particle arrays
    const particles = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const targetPositions = new Float32Array(particleCount * 3);
    const randomPositions = new Float32Array(particleCount * 3);
    const velocities = [];

    // Initialize positions
    for (let i = 0; i < particleCount; i++) {
        // Random starting positions (scattered)
        const randomX = (Math.random() - 0.5) * 800;
        const randomY = (Math.random() - 0.5) * 400;
        const randomZ = (Math.random() - 0.5) * 200;

        randomPositions[i * 3] = randomX;
        randomPositions[i * 3 + 1] = randomY;
        randomPositions[i * 3 + 2] = randomZ;

        positions[i * 3] = randomX;
        positions[i * 3 + 1] = randomY;
        positions[i * 3 + 2] = randomZ;

        // Target positions (text shape or random for extra particles)
        if (i < textPoints.length) {
            targetPositions[i * 3] = textPoints[i].x;
            targetPositions[i * 3 + 1] = textPoints[i].y;
            targetPositions[i * 3 + 2] = textPoints[i].z + (Math.random() - 0.5) * 20;
        } else {
            targetPositions[i * 3] = (Math.random() - 0.5) * 800;
            targetPositions[i * 3 + 1] = (Math.random() - 0.5) * 400;
            targetPositions[i * 3 + 2] = (Math.random() - 0.5) * 200;
        }

        velocities.push({
            x: (Math.random() - 0.5) * 2,
            y: (Math.random() - 0.5) * 2,
            z: (Math.random() - 0.5) * 2
        });
    }

    particles.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    // Particle material
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
        opacity: 0.12
    });

    const linesGroup = new THREE.Group();
    scene.add(linesGroup);

    // Connection distance
    const maxDistance = 60;

    // Mouse tracking
    let mouseX = 0;
    let mouseY = 0;
    let isHovering = false;
    let morphProgress = 0; // 0 = scattered, 1 = text form

    container.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect();
        mouseX = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
        mouseY = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
    });

    container.addEventListener('mouseenter', () => {
        isHovering = true;
    });

    container.addEventListener('mouseleave', () => {
        isHovering = false;
    });

    // Animation
    function animate() {
        requestAnimationFrame(animate);

        // Smooth transition for morph (INVERTED: form text on hover, scatter when not)
        if (isHovering) {
            // Form text on hover
            morphProgress = Math.min(1, morphProgress + 0.03);
        } else {
            // Scatter when not hovering
            morphProgress = Math.max(0, morphProgress - 0.02);
        }

        const positionArray = particles.attributes.position.array;

        // Update particle positions
        for (let i = 0; i < particleCount; i++) {
            const idx = i * 3;

            // Interpolate between random and target positions
            const targetX = morphProgress * targetPositions[idx] + (1 - morphProgress) * randomPositions[idx];
            const targetY = morphProgress * targetPositions[idx + 1] + (1 - morphProgress) * randomPositions[idx + 1];
            const targetZ = morphProgress * targetPositions[idx + 2] + (1 - morphProgress) * randomPositions[idx + 2];

            // Smooth easing towards target
            positionArray[idx] += (targetX - positionArray[idx]) * 0.05;
            positionArray[idx + 1] += (targetY - positionArray[idx + 1]) * 0.05;
            positionArray[idx + 2] += (targetZ - positionArray[idx + 2]) * 0.05;

            // Add floating motion when scattered (not hovering)
            if (!isHovering) {
                randomPositions[idx] += velocities[i].x * 0.3;
                randomPositions[idx + 1] += velocities[i].y * 0.3;
                randomPositions[idx + 2] += velocities[i].z * 0.3;

                // Bounce off boundaries
                if (Math.abs(randomPositions[idx]) > 400) velocities[i].x *= -1;
                if (Math.abs(randomPositions[idx + 1]) > 200) velocities[i].y *= -1;
                if (Math.abs(randomPositions[idx + 2]) > 100) velocities[i].z *= -1;
            }
        }

        particles.attributes.position.needsUpdate = true;

        // Clear old lines
        while (linesGroup.children.length > 0) {
            const mesh = linesGroup.children[0];
            if (mesh.geometry) mesh.geometry.dispose();
            linesGroup.remove(mesh);
        }

        // Create new connections (optimized - only connect nearby particles)
        const linePositions = [];
        const step = isHovering ? 2 : 1; // More connections when scattered (not hovering)

        for (let i = 0; i < particleCount; i += step) {
            const x1 = positionArray[i * 3];
            const y1 = positionArray[i * 3 + 1];
            const z1 = positionArray[i * 3 + 2];

            for (let j = i + 1; j < particleCount; j += step) {
                const x2 = positionArray[j * 3];
                const y2 = positionArray[j * 3 + 1];
                const z2 = positionArray[j * 3 + 2];

                const dx = x2 - x1;
                const dy = y2 - y1;
                const dz = z2 - z1;
                const distance = Math.sqrt(dx * dx + dy * dy + dz * dz);

                if (distance < maxDistance) {
                    linePositions.push(x1, y1, z1, x2, y2, z2);
                }
            }
        }

        if (linePositions.length > 0) {
            const lineGeometry = new THREE.BufferGeometry();
            lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
            const lines = new THREE.LineSegments(lineGeometry, lineMaterial);
            linesGroup.add(lines);
        }

        // Smooth rotation based on mouse
        const targetRotationX = mouseY * 0.3;
        const targetRotationY = mouseX * 0.3;

        particleSystem.rotation.x += (targetRotationX - particleSystem.rotation.x) * 0.02;
        particleSystem.rotation.y += (targetRotationY - particleSystem.rotation.y) * 0.02;
        linesGroup.rotation.x = particleSystem.rotation.x;
        linesGroup.rotation.y = particleSystem.rotation.y;

        // Subtle auto-rotate when in text form (hovering)
        if (isHovering) {
            particleSystem.rotation.y += 0.0005;
            linesGroup.rotation.y += 0.0005;
        }

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
