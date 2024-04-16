var ctx = document.getElementById('chart');

var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'],
        datasets: [{
            label: '',
            data: [risk_low, risk_medium, risk_high, risk_critical],
            backgroundColor: [
                '#77cc00',
                '#ff9d00',
                '#e74a3b',
                '#1a0000',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    fontSize: 15
                }
            }],
            xAxes: [{
                ticks:{
                    fontSize: 16,
                    display:false

                }
            }]
        },
        legend: {
            display: false
          },
        responsive: false,
    }
});

