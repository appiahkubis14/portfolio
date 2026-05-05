/**
 * PORTFOLIO DATA PATCH
 * =====================
 * Drop this file into your project as assets/portfolio_patch.js
 * Then add ONE line just before </body> in your index.html:
 *
 *   <script src="assets/portfolio_patch.js"></script>
 *
 * This script runs AFTER your main script and injects the two new
 * projects (Kapture + Traccar/AMP) and two new experience entries
 * into the already-rendered DOM — no need to touch index.html beyond
 * the one script tag.
 *
 * It also re-renders the #projectsGrid and #timeline to include them.
 */

(function () {

  /* ─────────────────────────────────────────────
     NEW PROJECT ENTRIES
     ───────────────────────────────────────────── */
  const newProjects = [
    {
      num: "11",
      icon: "fa-solid fa-map-marked-alt",
      img: "assets/kapture.png",          // add a screenshot to assets/
      title: "Kapture — Web GIS Land-Plot Management Platform",
      desc: "Production-grade Django GIS web application for land-plot registration, polygon geometry management, and geospatial administration — serving planners, surveyors, landowners, lawyers, and government agencies.",
      tags: ["Django", "PostGIS", "GeoDjango", "OpenLayers", "GeoJSON", "OGC", "PostgreSQL", "Tailwind", "Jazzmin"],
      impact: "Multi-role GIS platform · OGC-compliant APIs · Ghana Grid ↔ WGS84",
      details: {
        overview:
          "Kapture is a full-stack PostGIS-backed Django GIS application covering the complete software lifecycle — from architecture design through implementation, testing, and deployment. It serves planners, surveyors, landowners, lawyers, and government agencies with polygon geometry management, OGC-compliant geospatial APIs, and a polished admin experience.",
        highlights: [
          "Multi-role user system: agent, surveyor, planner, government, landowner, lawyer, broker — each with scoped data permissions",
          "PostGIS-backed plotDetails geometry with spatial indexing, soft deletion, and Ghana Grid ↔ WGS84 coordinate conversion",
          "Full OGC GeoJSON API surface: land-use, POI, district, region, and basepoint layers with per-user polygon ownership enforcement",
          "Secure auth pipeline: 6-digit OTP verification (15-min expiry), IP-geolocation login audit trail stored as spatial points, token-based password reset",
          "Admin dashboard: live growth analytics (users, plots, country metrics), paginated all-plot management, user suspension controls, team promotion workflows",
          "Interactive web map frontend (OpenLayers / Leaflet) with polygon save/upload/delete and real-time preview",
          "Slug-based resource content system with view-count tracking and related-content recommendations",
          "Tailwind CSS + Jazzmin admin UI; Docker containerised; full system documentation and end-user training materials",
        ],
      },
    },
    {
      num: "12",
      icon: "fa-solid fa-truck-moving",
      img: "assets/amp.png",
      title: "Java GPS Tracking & Fuel Monitoring System (Traccar — AMP Logistics)",
      desc: "Extended the open-source Java Traccar GPS platform to build a production vehicle-tracking and fuel-monitoring system — custom REST APIs, real-time telemetry, geofencing, and an OpenLayers fleet map.",
      tags: ["Java", "Traccar", "REST API", "PostGIS", "OpenLayers", "Geofencing", "Docker", "AWS"],
      impact: "Live fleet tracking · Fuel anomaly detection · Geofenced route alerts",
      details: {
        overview:
          "Built on Traccar — a Java-based open-source GPS tracking platform — to deliver a production fleet management system for AMP Logistics GH. Limited. Customised Java back-end services, designed and consumed REST APIs for real-time telemetry ingestion, and integrated live vehicle data into an OpenLayers-based management dashboard.",
        highlights: [
          "Extended Traccar Java back-end: custom event handlers, REST API endpoints, and real-time data-processing pipelines for vehicle position, speed, and fuel sensor readings",
          "Implemented geofencing logic for route-boundary alerts and arrival/departure notifications via webhook-driven REST callbacks",
          "Built PostGIS spatial queries for trip-history replay, route deviation detection, and distance/fuel-efficiency reporting per vehicle",
          "Designed OpenLayers web-map dashboard showing live vehicle positions, historical tracks, and geofence polygon overlays",
          "Integrated fuel-level sensor feeds with anomaly-detection rules to flag siphoning or excessive consumption events in real time",
          "Containerised Traccar server + custom Java services on Docker; deployed on AWS EC2 with Nginx reverse proxy",
          "Gained direct Java enterprise development experience (service layer, REST controllers, ORM patterns) — directly applicable to Spring Boot / Hibernate environments",
        ],
      },
    },
  ];

  /* ─────────────────────────────────────────────
     NEW EXPERIENCE ENTRIES
     ───────────────────────────────────────────── */
  const newExperiences = [
    {
      role: "Full-Stack GIS Developer",
      company: "Kapture Web GIS Platform",
      site: "",
      period: "2024 – 2025",
      location: "Ghana",
      type: "Contract",
      badge: "Contract Closed",
      achievements: [
        "Architected and delivered Kapture — a production PostGIS/GeoDjango Web GIS platform covering the full SDLC: architecture, implementation, testing, and Docker deployment",
        "Built OGC-compliant GeoJSON REST APIs (land-use, POI, district, region layers), Ghana Grid ↔ WGS84 coordinate conversion, and IP-geolocation login audit trail",
        "Delivered OpenLayers interactive map frontend, multi-role RBAC, 6-digit OTP auth, and live admin analytics dashboard with full system documentation",
      ],
    },
    {
      role: "Java Back-End & GIS Developer — GPS Tracking System",
      company: "AMP Logistics GH. Limited",
      site: "https://amplogisticsgh.com/",
      period: "2024 – 2025",
      location: "Tema, Ghana",
      type: "Hybrid",
      badge: "Contract Closed",
      achievements: [
        "Extended Traccar (Java open-source GPS platform) with custom REST API services, real-time telemetry pipelines, geofencing, and fuel-anomaly detection for live fleet monitoring",
        "Built PostGIS spatial queries for trip history, route deviation detection, and fuel-efficiency reporting; visualised on an OpenLayers fleet-map dashboard",
        "Containerised Java services on Docker/AWS with Nginx; gained hands-on Java enterprise patterns (service layer, REST, ORM) applicable to Spring Boot/Hibernate environments",
      ],
    },
  ];

  /* ─────────────────────────────────────────────
     INJECT INTO PROJECT GRID
     ───────────────────────────────────────────── */
  const grid = document.getElementById("projectsGrid");
  if (grid) {
    // Re-use the same card-building logic as the main script
    newProjects.forEach((p, i) => {
      const card = document.createElement("div");
      card.className = `project-card fu d${(i % 3) + 1}`;
      const topTags = p.tags
        .slice(0, 3)
        .map((t) => `<span class="proj-tech-pill">${t}</span>`)
        .join("");
      card.innerHTML = `
        <div class="proj-img">
          <img src="${p.img}" alt="${p.title}" loading="lazy"/>
          <div class="proj-img-overlay"></div>
          <div class="proj-num-badge">PROJECT ${p.num}</div>
          <div class="proj-tech-preview">${topTags}</div>
        </div>
        <div class="project-body">
          <div class="project-title">${p.title}</div>
          <div class="project-desc">${p.desc}</div>
          <div class="project-impact"><i class="${p.icon}"></i> ${p.impact}</div>
        </div>
        <div class="project-footer">
          <span class="proj-count"><i class="fa-solid fa-microchip" style="color:var(--orange)"></i> ${p.tags.length} technologies</span>
          <span class="view-btn">View Details <i class="fas fa-arrow-right"></i></span>
        </div>`;

      // Modal click
      card.addEventListener("click", () => {
        document.getElementById("modalImg").innerHTML = `<img src="${p.img}" alt="${p.title}"/>`;
        document.getElementById("modalNum").innerHTML = `<i class="${p.icon}"></i> PROJECT ${p.num}`;
        document.getElementById("modalTitle").textContent = p.title;
        document.getElementById("modalBody").innerHTML = `
          <div class="modal-section">
            <div class="modal-section-title">Overview</div>
            <div class="modal-text">${p.details.overview}</div>
          </div>
          <div class="modal-section">
            <div class="modal-section-title">Technologies</div>
            <div style="display:flex;flex-wrap:wrap;gap:7px">
              ${p.tags.map((t) => `<span style="font-family:var(--font-m);font-size:0.73rem;padding:4px 11px;border-radius:7px;background:var(--orange-subtle);color:var(--orange);border:1px solid rgba(249,115,22,.22)">${t}</span>`).join("")}
            </div>
          </div>
          <div class="modal-section">
            <div class="modal-section-title">Key Highlights</div>
            <ul class="modal-list">${p.details.highlights.map((h) => `<li>${h}</li>`).join("")}</ul>
          </div>
          <div class="modal-section" style="margin-bottom:0">
            <div class="modal-section-title">Impact</div>
            <div class="modal-text" style="color:var(--orange);font-weight:700;font-family:var(--font-h)">${p.impact}</div>
          </div>`;
        document.getElementById("modalOverlay").classList.add("open");
        document.body.style.overflow = "hidden";
      });

      grid.appendChild(card);

      // Trigger intersection observer on new cards
      if (window.__portfolioObs) window.__portfolioObs.observe(card);
    });
  }

  /* ─────────────────────────────────────────────
     INJECT INTO TIMELINE
     ───────────────────────────────────────────── */
  const timeline = document.getElementById("timeline");
  if (timeline) {
    newExperiences.forEach((exp, i) => {
      const item = document.createElement("div");
      item.className = `timeline-item fu d${(i % 3) + 1}`;
      const badgeClass = exp.badge === "current" ? "badge-current" : "badge-past";
      const badgeLabel =
        exp.badge === "current"
          ? '<i class="fa-solid fa-circle fa-xs"></i> Active'
          : "Contract Closed";
      const siteLink = exp.site
        ? `<a href="${exp.site}" target="_blank" rel="noopener noreferrer"
              onclick="event.stopPropagation()"
              style="display:inline-flex;align-items:center;gap:4px;margin-left:10px;
                     font-family:var(--font-m);font-size:0.68rem;color:var(--tx3);
                     border:1px solid var(--bdr);border-radius:6px;padding:2px 8px;
                     transition:all .2s;text-decoration:none"
              onmouseover="this.style.color='var(--orange)';this.style.borderColor='var(--orange)'"
              onmouseout="this.style.color='var(--tx3)';this.style.borderColor='var(--bdr)'">
              <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.6rem"></i> Visit site
           </a>`
        : "";
      item.innerHTML = `
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <div>
              <div class="timeline-role">${exp.role}</div>
              <div class="timeline-company"><i class="fa-solid fa-building fa-sm"></i> ${exp.company}</div>
              <div class="timeline-meta">
                <span><i class="fa-solid fa-calendar-alt"></i> ${exp.period}</span>
                <span><i class="fa-solid fa-map-marker-alt"></i> ${exp.location}</span>
                <span><i class="fa-solid fa-laptop-house"></i> ${exp.type}</span>
              </div>
            </div>
            <span class="${badgeClass}">${badgeLabel}${siteLink}</span>
          </div>
          <ul class="timeline-achievements">
            ${exp.achievements.map((a) => `<li>${a}</li>`).join("")}
          </ul>
        </div>`;
      timeline.appendChild(item);
      if (window.__portfolioObs) window.__portfolioObs.observe(item);
    });
  }

})();