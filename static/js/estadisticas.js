Highcharts.chart("graph1", {
  chart: {
    type: "line",
  },
  title: {
    text: "Actividades por día",
  },
  xAxis: {
    type: "datetime",
    dateTimeLabelFormats: {
      month: "%b %e, %Y",
    },
    title: {
      text: "Fecha",
    },
  },
  yAxis: {
    title: {
      text: "Valores",
    },
  },
  series: [
    {
      name: "Actividades",
    },
  ],
});

Highcharts.chart("graph2", {
  chart: {
    type: "pie",
  },
  title: {
    text: "Cantidad de Actividades por tipo",
  },
  series: [
    {
      name: "Actividades",
      colorByPoint: true,
      data: [],
    },
  ],
});

Highcharts.chart("graph3", {
  chart: {
    type: "column",
  },
  title: {
    text: "Actividades por Mes",
  },
  xAxis: {
    categories: [
      "Enero",
      "Febrero",
      "Marzo",
      "Abril",
      "Mayo",
      "Junio",
      "Julio",
      "Agosto",
      "Septiembre",
      "Octubre",
      "Noviembre",
      "Diciembre",
    ],
  },
  yAxis: {
    min: 0,
    title: {
      text: "Cantidad de Actividades",
    },
  },
  legend: {
    align: "right",
    verticalAlign: "top",
    layout: "vertical",
  },
  series: [
    {
      name: "Mañana",
      data: [5, 3, 4, 7, 2, 6],
    },
    {
      name: "Mediodía",
      data: [2, 2, 3, 2, 1, 4],
    },
    {
      name: "Tarde",
      data: [3, 4, 4, 2, 5, 3],
    },
  ],
});

fetch("http://127.0.0.1:5000/get-stats-date")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    let parsedData = data.map((item) => {
      const [year, month, day] = item.fecha
        .split("-")
        .map((part) => parseInt(part, 10));
      return [Date.UTC(year, month - 1, day), item.cantidad];
    });

    console.log(parsedData);

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "graph1"
    );

    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  })
  .catch((error) => {
    console.error("Error fetching statistics:", error);
    const statsContainer = document.getElementById("graph1");
    statsContainer.innerHTML = "<p>Error al cargar las estadísticas.</p>";
  });

fetch("http://127.0.0.1:5000/get-stats-type")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "graph2"
    );

    chart.update({
      series: [
        {
          data: data.map((item) => ({
            name: item.tema,
            y: item.cantidad,
          })),
        },
      ],
    });
  })
  .catch((error) => {
    console.error("Error fetching statistics:", error);
    const statsContainer = document.getElementById("graph2");
    statsContainer.innerHTML = "<p>Error al cargar las estadísticas.</p>";
  });

fetch("http://127.0.0.1:5000/get-stats-activities")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "graph3"
    );

    const data_manana = data.map((item) => item.cantidad_mañana);
    const data_tarde = data.map((item) => item.cantidad_tarde);
    const data_noche = data.map((item) => item.cantidad_noche);

    chart.update({
      series: [
        {
          name: "Mañana",
          data: data_manana,
        },
        {
          name: "Mediodía",
          data: data_tarde,
        },
        {
          name: "Tarde",
          data: data_noche,
        },
      ],
    });
  });
