// Dotted world globe for the homepage contact section.
// Land dots are sampled once from an equirectangular land mask; each frame only rotates
// and projects those points (orthographic), so the globe can spin and be dragged smoothly.
// Location cards and markers follow their real coordinates and hide on the far side.
(function () {
    const el = document.querySelector('.contact-globe');
    if (!el) return;
    const canvas = el.querySelector('canvas');
    if (!canvas || !window.d3 || !window.d3.geoEquirectangular || !window.topojson) {
        el.classList.add('globe-ready', 'globe-failed');
        return;
    }

    const LAND_URL = 'https://cdn.jsdelivr.net/npm/world-atlas@2/land-110m.json';
    const RAD = Math.PI / 180;
    const ctx = canvas.getContext('2d');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const pinned = [...el.querySelectorAll('[data-lat][data-lng]')].map((node) => ({
        node,
        lat: Number(node.dataset.lat),
        lng: Number(node.dataset.lng),
    }));

    // Rotation state: lambda = longitude facing the viewer, phi = latitude tilt.
    let lambda = Number(el.dataset.centerLng) || 72;
    let phi = Number(el.dataset.centerLat) || 16;
    const AUTO_SPEED = 8; // degrees per second, about one turn every 45 s
    let velocity = 0; // inertia after a drag, degrees per second
    let dragging = false;
    let lastPointer = null;
    let lastInteraction = -Infinity;
    let visible = true;

    let dots = []; // [lngRad, latRad] for every land dot
    let size = 0, dpr = 1, radius = 0, cx = 0, cy = 0;

    function sampleLand(land) {
        const W = 1440, H = 720;
        const mask = document.createElement('canvas');
        mask.width = W;
        mask.height = H;
        const mctx = mask.getContext('2d', { willReadFrequently: true });
        const projection = d3.geoEquirectangular().fitSize([W, H], { type: 'Sphere' });
        const path = d3.geoPath(projection, mctx);
        mctx.beginPath();
        path(land);
        mctx.fillStyle = '#000';
        mctx.fill();
        const data = mctx.getImageData(0, 0, W, H).data;

        const step = 1.25;
        const points = [];
        for (let lat = -84; lat <= 84; lat += step) {
            const lngStep = step / Math.max(Math.cos(lat * RAD), 0.2);
            for (let lng = -180; lng < 180; lng += lngStep) {
                const xy = projection([lng, lat]);
                const x = Math.min(W - 1, Math.max(0, Math.round(xy[0])));
                const y = Math.min(H - 1, Math.max(0, Math.round(xy[1])));
                if (data[(y * W + x) * 4 + 3] > 127) points.push([lng * RAD, lat * RAD]);
            }
        }
        return points;
    }

    function resize() {
        size = Math.round(el.clientWidth);
        if (!size) return;
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = size * dpr;
        canvas.height = size * dpr;
        canvas.style.width = size + 'px';
        canvas.style.height = size + 'px';
        radius = size / 2 - 6;
        cx = size / 2;
        cy = size / 2;
    }

    function draw() {
        if (!size) return;
        const l0 = lambda * RAD;
        const p0 = phi * RAD;
        const sinP0 = Math.sin(p0);
        const cosP0 = Math.cos(p0);

        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        ctx.clearRect(0, 0, size, size);
        ctx.beginPath();
        ctx.arc(cx, cy, radius, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(22, 22, 22, 0.08)';
        ctx.lineWidth = 1;
        ctx.stroke();

        ctx.fillStyle = '#262626';
        const dotBase = size < 420 ? 1.1 : 1.5;
        for (let i = 0; i < dots.length; i++) {
            const lng = dots[i][0];
            const lat = dots[i][1];
            const cosLat = Math.cos(lat);
            const dl = lng - l0;
            const cosDl = Math.cos(dl);
            const facing = sinP0 * Math.sin(lat) + cosP0 * cosLat * cosDl;
            if (facing <= 0.02) continue;
            const x = cx + radius * cosLat * Math.sin(dl);
            const y = cy - radius * (cosP0 * Math.sin(lat) - sinP0 * cosLat * cosDl);
            const s = dotBase * (0.45 + 0.55 * facing);
            ctx.globalAlpha = 0.25 + 0.7 * facing;
            ctx.fillRect(x - s / 2, y - s / 2, s, s);
        }
        ctx.globalAlpha = 1;

        for (const p of pinned) {
            const lat = p.lat * RAD;
            const dl = p.lng * RAD - l0;
            const cosLat = Math.cos(lat);
            const facing = sinP0 * Math.sin(lat) + cosP0 * cosLat * Math.cos(dl);
            p.node.style.left = cx + radius * cosLat * Math.sin(dl) + 'px';
            p.node.style.top = cy - radius * (cosP0 * Math.sin(lat) - sinP0 * cosLat * Math.cos(dl)) + 'px';
            p.node.classList.toggle('is-back', facing < 0.2);
        }
    }

    let previous = 0;
    function frame(now) {
        const dt = previous ? Math.min((now - previous) / 1000, 0.05) : 0;
        previous = now;
        if (visible && !document.hidden && dots.length) {
            if (!dragging) {
                if (Math.abs(velocity) > 0.5) {
                    lambda += velocity * dt;
                    velocity *= Math.pow(0.04, dt); // ease out over roughly a second
                } else if (!reducedMotion.matches && now - lastInteraction > 1500) {
                    lambda += AUTO_SPEED * dt;
                }
            }
            draw();
        }
        requestAnimationFrame(frame);
    }

    // Drag to rotate (mouse, pen or touch). Listen on the whole globe, including the location
    // cards that sit on top of the canvas, but let clicks on their phone links through.
    el.addEventListener('pointerdown', (event) => {
        if (event.button !== undefined && event.button !== 0) return;
        if (event.target.closest('a')) return;
        dragging = true;
        velocity = 0;
        lastPointer = { x: event.clientX, y: event.clientY, t: performance.now() };
        el.setPointerCapture(event.pointerId);
        el.classList.add('is-dragging');
        event.preventDefault();
    });
    el.addEventListener('pointermove', (event) => {
        if (!dragging || !lastPointer) return;
        const now = performance.now();
        const degPerPx = 180 / (Math.PI * Math.max(radius, 1));
        const dx = event.clientX - lastPointer.x;
        const dy = event.clientY - lastPointer.y;
        lambda -= dx * degPerPx;
        phi = Math.max(-60, Math.min(60, phi + dy * degPerPx));
        const dtMove = Math.max((now - lastPointer.t) / 1000, 0.001);
        velocity = (-dx * degPerPx) / dtMove;
        lastPointer = { x: event.clientX, y: event.clientY, t: now };
        lastInteraction = now;
    });
    function endDrag(event) {
        if (!dragging) return;
        dragging = false;
        lastInteraction = performance.now();
        if (lastPointer && performance.now() - lastPointer.t > 80) velocity = 0;
        velocity = Math.max(-240, Math.min(240, velocity));
        el.classList.remove('is-dragging');
        if (event && el.hasPointerCapture && el.hasPointerCapture(event.pointerId)) {
            el.releasePointerCapture(event.pointerId);
        }
    }
    el.addEventListener('pointerup', endDrag);
    el.addEventListener('pointercancel', endDrag);

    // Only animate while the globe is on screen.
    if ('IntersectionObserver' in window) {
        new IntersectionObserver((entries) => {
            visible = entries[0].isIntersecting;
        }, { rootMargin: '120px' }).observe(el);
    }

    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            resize();
            draw();
        }, 120);
    });

    fetch(LAND_URL)
        .then((response) => response.json())
        .then((topology) => {
            dots = sampleLand(topojson.feature(topology, topology.objects.land));
            resize();
            draw();
            el.classList.add('globe-ready');
            requestAnimationFrame(frame);
        })
        .catch(() => el.classList.add('globe-ready', 'globe-failed'));
})();
