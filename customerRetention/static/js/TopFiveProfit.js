new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
        labels: ["Cold-Drink", "Cosmetics", "Vegies", "Beverage", "Home Decor"],
        datasets: [
            {
                label: "Amount (Rupees)",
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                data: [24780, 52670, 7340, 7840, 4330]
            }
        ]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: 'Top 5 Profit Category Chart',
            fontColor: 'black'
        },
        scales: {
            yAxes: [{
                ticks: {

                    fontColor: 'black'
                },
            }],
            xAxes: [{
                ticks: {
                    fontColor: 'black'
                },
            }]
        }
    },


});
