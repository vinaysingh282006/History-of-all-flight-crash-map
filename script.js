let map = L.map("map").setView([20, 0], 2);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 6,
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

let crashData = [];
let markersLayer = L.layerGroup().addTo(map);
let chart;

async function loadData() {
  const res = await fetch("data/crashes.json");
  crashData = await res.json();
  renderMarkers(crashData);
  updateAnalytics(crashData);
}

function renderMarkers(data) {
  markersLayer.clearLayers();
  data.forEach((crash) => {
    if (crash.Latitude && crash.Longitude) {
      const marker = L.circleMarker([crash.Latitude, crash.Longitude], {
        radius: 5,
        fillColor: "red",
        color: "#f03",
        fillOpacity: 0.7,
      }).bindPopup(`
        <b>${crash.Location}</b><br>
        Year: ${crash.Year}<br>
        Type: ${crash.Type}<br>
        Fatalities: ${crash.Fatalities}<br>
        Country: ${crash.Country}
      `);
      markersLayer.addLayer(marker);
    }
  });
}

function updateAnalytics(data) {
  const total = data.length;
  const totalFatal = data.reduce((sum, d) => sum + (d.Fatalities || 0), 0);
  const avgFatal = total ? (totalFatal / total).toFixed(1) : 0;

  document.getElementById("count").textContent = total;
  document.getElementById("fatalities").textContent = totalFatal;
  document.getElementById("avg").textContent = avgFatal;

  // Chart - crashes by decade
  const grouped = {};
  data.forEach((d) => {
    const decade = Math.floor(d.Year / 10) * 10;
    grouped[decade] = (grouped[decade] || 0) + 1;
  });

  const labels = Object.keys(grouped).sort();
  const values = labels.map((l) => grouped[l]);

  if (chart) chart.destroy();
  chart = new Chart(document.getElementById("chart"), {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "Crashes per Decade",
          data: values,
          backgroundColor: "rgba(255,99,132,0.6)",
        },
      ],
    },
    options: { scales: { y: { beginAtZero: true } } },
  });
}

document.getElementById("applyFilter").addEventListener("click", () => {
  const minY = +document.getElementById("yearMin").value || 0;
  const maxY = +document.getElementById("yearMax").value || 9999;
  const type = document.getElementById("typeFilter").value;
  const region = document.getElementById("regionFilter").value.toLowerCase();
  const minF = +document.getElementById("fatalFilter").value || 0;

  const filtered = crashData.filter(
    (c) =>
      c.Year >= minY &&
      c.Year <= maxY &&
      (type === "All" || c.Type === type) &&
      (!region || (c.Country && c.Country.toLowerCase().includes(region))) &&
      (c.Fatalities || 0) >= minF
  );

  renderMarkers(filtered);
  updateAnalytics(filtered);
});

loadData();
